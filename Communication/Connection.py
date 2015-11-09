import socket
import re

from Communication.PingObservable import PingObservable
from Model import ConnectionDetails

class Connection(object):

    details = None
    irc = None

    def send(self):
        """
        Send to network
        :return:
        """

    def raw_send(self, message):
        self.irc.send(message.encode() + '\r\n'.encode())

    def receive(self):
        """
        receive from Network
        """
        data = self.irc.recv(4096).decode('UTF-8')
        data = data.rstrip()
        print(data)
        if data.find('PING') != -1:
            self._ping.input(data)

    def establish(self):
        """
        establish the connection
        """
        global details
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.irc.connect((details.get_server(), details.get_port()))
        print(self.irc.recv(4096))
        self.irc.send("NICK ".encode() + details.get_nick().encode() + "\r\n".encode())
        self.irc.send("USER botty botty botty :IRC Bot\r\n".encode())
        self.irc.send("JOIN ".encode() + details.get_channel().encode() + '\r\n'.encode())

    def __init__(self, set_details: ConnectionDetails):
        global details
        details = set_details
        self._ping = PingObservable()

    def observePing(self, observer):
        """
        add observer to the observers of the ping-observable
        :param observer: observer to add
        """
        self._ping.addObserver(observer)
