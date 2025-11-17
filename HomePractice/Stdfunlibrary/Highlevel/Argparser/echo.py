import argparse

parser=argparse.ArgumentParser()
parser.add_argument("message",help="Message to be echoed")
parser.add_argument("-c","--capitalize",action="store_true")
arg_s=parser.parse_args()
if arg_s.capitalize:
    print(arg_s.message.capitalize())
else:
    print(arg_s.message)