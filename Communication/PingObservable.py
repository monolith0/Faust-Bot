import _thread

from Communication.Observable import Observable


class PingObservable(Observable):

    def input(self, raw_data):
        data = {}
        data['raw'] = raw_data
        data['server'] = ''
        if (raw_data.find('PING') == 0):
            data['server'] = raw_data.split('PING ')[1]
        else:
            return
        # hier kann noch gecheckt werden, ob data wirklich ein server ist, der ping haben will, oder sonstwas
        # finde heraus, wer zurückgepingt werden muss, und ob das überhaupt ein ping-request ist oder ein user sich
        # einen spass erlaubt hat
        self.notifyObservers(data)

    def notifyObservers(self, data):
        for observer in self._observers:
            _thread.start_new_thread(observer.__class__.update_on_ping, (observer, data))