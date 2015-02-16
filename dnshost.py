#!/usr/bin/env python

import flask

app = flask.Flask(__name__)


def checkForHost(hostname):
    f = open('/etc/dns.conf', 'r')

    for line in f:
        if hostname in line:
            big = line.split('=')

            little = big[1].split(',')
            f.close()
            return tuple(little)
        else:
            f.close()
            return None


def updateHost(hostname, ip):
    f = open('/etc/dns.conf', 'r')

    lines = f.readlines()

    index = 0

    for line in lines:
        if hostname in line:
            lines[index] = ip + '\t' + hostname + '.cloud.pro\t' + hostname
            break
        index = index + 1

    f.close()
    f = open('/etc/dns.conf', 'w')

    f.writelines(lines)

    f.close()


def insertHost(hostname, ip):
    f = open('/etc/dns.conf', 'a')

    print >>f, ip + '\t' + hostname + '.cloud.pro\t' + hostname
    f.close()


@app.route('/add/<hostname>/<ip>')
def add_dns(hostname, ip):
    result = checkForHost(hostname)

    if result != None:
        updateHost(hostname, ip)
    else:
        insertHost(hostname, ip)

    return 'success'


@app.route('/')
def index():
    return 'invalid parameters: format is /add/<em>hostname</em>/<em>ip</em>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
