import asyncio
import argparse

def input_parser():
    parser = argparse.ArgumentParser(prog='nc-python', usage="%(prog)s [ options ]")
    parser.add_argument('-c', help="specify shell commands to exec after connect (use  with  caution).   The  string  is  passed  to
                    /bin/sh  -c  for  execution.   See  the -e option if you don't have a working /bin/sh (Note that
                    POSIX-conformant system must have one).
")
    parser.add_argument('-e',help="specify filename to exec after connect (use with caution).  See the -c option for enhanced func‐
                    tionality.
")
    parser.add_argument('-g',nargs=1,help="source-routing hop point[s], up to 8")
    parser.add_argument('-G',nargs=1,help="source-routing pointer: 4, 8, 12, ...")
    parser.add_argument('-h',help="display help")
    parser.add_argument('-i',nargs=1,help="delay interval for lines sent, ports scanned")
    parser.add_argument('-l',action='store_true',help="listen mode, for inbound connects")
    parser.add_argument('-n',nargs=1,help="numeric-only IP addresses, no DNS")
    parser.add_argument('-o',nargs=?,help="hex dump of traffic")
    parser.add_argument('-p',nargs=1,help="local port number (port numbers can be individial or ranges: lo-hi [inclusive]")
    parser.add_argument('-q',nargs=1,help="after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.")
    parser.add_argument('-b',action='store_true',help="allow UDP broadcasts")
    parser.add_argument('-C',action='store_true',help="Send CRLF as line-ending")
    parser.add_argument('-z',action='store_true',help="zero-I/O mode [used for scanning]")
    #parser.add_argument('-T',help="set TOS flag (type may be one of 'Minimize-Delay', 'Maximize-Throughput', 'Maximize-Reliability', or 'Minimize-Cost'.")  
    parser.add_argument('-t',action='store_true',help="enable telnet negotiation")
    parser.add_argument('-r',action='store_true',help="randomize local and remote ports")
    parser.add_argument('-s',nargs=1,help="local source address")
    parser.add_argument('-u',action='store_true',help="UDP Mode")  
    parser.add_argument('-v',action='store_true',help="verbose [only one mode]")  
    parser.add_argument('-w',nargs=1,help="timeout for connects and final net reads")  
    args=parser.parse_args()
    return args
async def main():
    data = input_parser()
    #Need to implement server serve with websockets or sockets
    await asyncio.Future()
    

if __name__ == "__main__":
    asyncio.run(main())
