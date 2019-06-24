import requests
import configparser

allTrackerUrl = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt'
allTrackerIpUrl = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt'
cccaTrackerUrl = 'https://api.xiaoz.org/trackerslist/'

from configparser import ConfigParser

class UnixConfigParser(ConfigParser):

    def read(self, filenames, encoding=None):
        from io import StringIO
        try:
            text = open(filenames).read()
        except IOError:
            pass
        else:
            file = StringIO("[shell]\n" + text)
            self.read_file(file, filenames)

def getTrackers(url:str,sep='\n\n')->list:
    ret = requests.get(url)
    ret.encoding = ret.apparent_encoding
    trackersStr = ret.text
    trackers = []
    if trackersStr:
        trackers = trackersStr.split(sep=sep)

    return trackers

def readConfig(path):
    from configparser import ConfigParser
    config = ConfigParser()
    config.read(path)
    trackerPart = None
    try:
        trackerPart = config['Trackers']
    except:
        pass
    trackers = []
    if trackerPart:
        trackersStr = trackerPart.get('bt-tracker','')
        trackers = trackersStr.split(sep=',')
    return trackers

def main():
    import argparse

    parser = argparse.ArgumentParser(description='aria2 btTracker update')
    parser.add_argument('--conf', dest='confPath',
                        action='store', default='aria.conf')
    parser.add_argument('--out', dest='out',
                        action='store', default='aria.conf')
    parser.add_argument('--token', dest='token',
                        action='store', default='')
    args = parser.parse_args()

    trackers = []
    # trackers.extend(readConfig(args.confPath))
    trackers.extend(getTrackers(allTrackerIpUrl))
    # trackers.extend(getTrackers(allTrackerUrl))
    trackers.extend(getTrackers(cccaTrackerUrl,sep=','))

    trackers = set(trackers)
    try:
        trackers.remove('')
    except:
        pass

    ariaTrackerConf = ",".join(trackers)
    print(ariaTrackerConf)

    config = ConfigParser()
    config.read(args.confPath)
    config['RPC']['rpc-secret'] = args.token
    config['Trackers']['bt-tracker'] = ariaTrackerConf
    with open(args.out, 'w') as configfile:
        config.write(configfile)



    return


if __name__ == '__main__':
    main()