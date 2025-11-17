import argparse

parser=argparse.ArgumentParser(description="""
Prints out the words pass in,capitalizes them if required
and repeat them in as many lines as requested.                               
""")
parser.add_argument("message",help="Message to be echoed",nargs="+")
parser.add_argument("-c","--capitalize",action="store_true")
parser.add_argument("-r","--repeat",type=int,default=1)
arg_s=parser.parse_args()
if arg_s.capitalize:
    messages=[m.capitalize() for m in arg_s.message]
else:
    messages=arg_s.message

for i in range(arg_s.repeat):
    print(" ".join(messages))
