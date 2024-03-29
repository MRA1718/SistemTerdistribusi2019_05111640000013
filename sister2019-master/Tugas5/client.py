import Pyro4
import base64
import json
import sys

if len(sys.argv) > 1:
    namainstance = sys.argv[1]
else:
    namainstance = "fileserver1"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    fserver.pyro_connect()
    return fserver

if __name__=='__main__':

    s = get_fileserver_object()
    file = ""
    while True:
        print("1. create | 2. read | 3. update | 4. delete | 5. ls | 0. exit")
        cmd = raw_input("list ops : ")

        if (cmd == '1'):
            filename = raw_input("filename : ")
            data_cmd = raw_input("content : ")
            print '\n'
            print s.create(filename, data_cmd)
            print '\n'

        elif (cmd == '2'):
            filename = raw_input("filename : ")
            print '\n'
            print s.read(filename)
            print '\n'

        elif (cmd == '3'):
            filename = raw_input("filename : ")
            value = raw_input("content : ")
            print '\n'
            print s.update(filename, value)
            print '\n'

        elif (cmd == '4'):
            filename = raw_input("filename : ")
            print '\n'
            print s.delete(filename)
            print '\n'

        elif (cmd == '5'):
            print '\n'
            print '\n'.join(s.list())
            print '\n'

        elif (cmd == '0'):
            print "Exit"
            exit()
        else:
            print("Wrong input, please try again")

