from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from threading import Thread
from tpm import *
import json
import base64

# Used to access the index in the exchanged messages
MESSAGE_TYPE = 0
MESSAGE = 1

# The types of the messages exchanged
TYPE_INPUTS = 0
TYPE_OUTPUT_SERVER = 1
TYPE_OUTPUT_CLIENT = 2
TYPE_ACK = 3
TYPE_TEST = 4
TYPE_TEST_OK = 5
TYPE_MESSAGE = 6

SYNC_THRESHOLD = 20
TEST_MESSAGE = 'SYNCED'

class NeuralCryptography(Protocol):

    def __init__(self):
        self.tpm = TreeParityMachine(4,3);
        self.count = 0
        self.syncronized = False
        self.key = None
        self.cipher = None

    def syncronizer(self, data):
        data = json.loads(data)
        if self.count == SYNC_THRESHOLD:
            self.test_sync()
        elif data[MESSAGE_TYPE] == TYPE_INPUTS:
            self.receive_inputs(data[MESSAGE])
        elif data[MESSAGE_TYPE] == TYPE_OUTPUT_SERVER:
            self.receive_output_from_server(data[MESSAGE])
        elif data[MESSAGE_TYPE] == TYPE_OUTPUT_CLIENT:
            self.receive_output_from_client(data[MESSAGE])
        elif data[MESSAGE_TYPE] == TYPE_ACK:
            self.receive_ack()
        elif data[MESSAGE_TYPE] == TYPE_TEST:
            self.receive_test(data[MESSAGE])
        elif data[MESSAGE_TYPE] == TYPE_TEST_OK:
            self.receive_test_ok()

    def receive_inputs(self, inputs):
        self.tpm(inputs)
        self.transport.write(json.dumps([TYPE_OUTPUT_SERVER, self.tpm.y]))

    def receive_output_from_server(self, output):
        self.transport.write(json.dumps([TYPE_OUTPUT_CLIENT, self.tpm.y]))
        if self.tpm.y == output:
            self.count += 1
            self.tpm.train()
        else:
            self.count = 0

    def receive_output_from_client(self, output):
        if self.tpm.y == output:
            self.count += 1
            self.tpm.train()
        else:
            self.count = 0
        self.transport.write(json.dumps([TYPE_ACK, 0]))

    def receive_ack(self):
        self.tpm.generate_inputs()
        self.tpm(self.tpm.x)
        self.transport.write(json.dumps([TYPE_INPUTS, self.tpm.x]))

    def synced(self):
        return self.syncronized

    def test_sync(self):
        self.count = 0
        self.generate_key()
        self.cipher = AES.new(self.key, AES.MODE_CBC)

        ciphertext = self.cipher.encrypt(self.pad(TEST_MESSAGE.encode('utf-8')))
        ciphertext = base64.b64encode(ciphertext)
        self.transport.write(json.dumps([TYPE_TEST, ciphertext]))
    
    def receive_test(self, ciphertext):
        self.generate_key()
        self.cipher = AES.new(self.key, AES.MODE_CBC)
        ciphertext = base64.b64decode(ciphertext)
        plaintext = self.cipher.decrypt(ciphertext)
        plaintext = self.unpad(plaintext)
        if plaintext == TEST_MESSAGE:
            self.transport.write(json.dumps([TYPE_TEST_OK, TEST_MESSAGE]))
            self.syncronized = True
            print self.tpm.weights()
            self.start_service()
        else:
            self.transport.write(json.dumps([TYPE_ACK, 0]))

    def receive_test_ok(self):
        self.syncronized = True
        self.start_service()
        print self.tpm.weights()

    def generate_key(self):
        seed = str(self.tpm.weights())
        sha = SHA256.new()
        sha.update(seed)
        self.key = sha.digest()
        return self.key

    def pad(self, s):
        BS = 16
        return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    def unpad(self, s):
        return s[0:-ord(s[-1])]

    def call(self, target, args):
        self.thread = Thread(target=target, args=(args))

    def receive(self, target):
        self.data_received = target

    def start_service(self):
        self.thread.start()
    
    def received(self, data):
        data = json.loads(data)
        ciphertext = data[MESSAGE]
        ciphertext = base64.b64decode(ciphertext)
        plaintext = self.cipher.decrypt(ciphertext)
        plaintext = self.unpad(plaintext)
        self.data_received(plaintext)

    def send_message(self, data):
        ciphertext = self.cipher.encrypt(self.pad(data))
        ciphertext = base64.b64encode(ciphertext)
        self.transport.write(json.dumps([TYPE_MESSAGE, ciphertext]))
