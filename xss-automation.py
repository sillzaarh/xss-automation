#!/usr/bin/env python3

import os, requests, urllib3, threading, argparse, urllib.parse as urlparse
urllib3.disable_warnings()

# Required arguments are set
parser = argparse.ArgumentParser(description="Reflected Cross Site Scripting (R-XSS) Autotmation Tool")
parser.add_argument("-u", "--url", type=str, metavar="",  help="enter the URL (URL should be provided in proper format)")
parser.add_argument("-l", "--list", type=str, metavar="", help="enter the path to file of list of URLs")
parser.add_argument("-p", "--payload", type=str, metavar="", help="enter the payload you want to inject")
parser.add_argument("-P", "--payload_list", type=str, metavar="", help="enter the path to file of list of payloads")
args = parser.parse_args()


# Get modified URL with payload
def modified_url(url, payload):
    parsed = urlparse.urlparse(url)
    u = list(urlparse.parse_qs(parsed.geturl()))
    req = ""
    if u:
        for i in u:
            req = req + i + "=" + payload + "&"
    
        return req
    else:
        return None

def find_xss(url, payload):
    mod_url = modified_url(url, payload)
    res = requests.get(mod_url, allow_redirects=False)
    
    if payload in res.text:
        print(res.url)

# Checks if the --url argument is set or not
if args.url:
    
    # Checkss if --payload_list argument is set or not
    if args.payload_list:
        
        # Checks if the paylods file exist or not
        if os.path.isfile(args.payload_list):
            file = open(args.payload_list, "r")
            payloads = file.readlines()
            file.close()
            
            # Send request to the provided URL with each payloads
            for payload in payloads:
                payload = payload.strip()
                try:
                    t = threading.Thread(target=find_xss, args=(args.url, payload,))
                    t.start()
                except:
                    pass
        else:
            print("File {file} is not present.".format(file=args.payload_list))
    
    # Checks is --payload argument is set or not
    elif args.payload:
        find_xss(args.url, args.payload)
    else:
        print("Please provide payload or list of payloads file.")

# Checks if the --list argument is set or not
if args.list:
    
    # Checks if URLs file exist or not
    if os.path.isfile(args.list):
        file = open(args.list, "r")
        urls = file.readlines()
        file.close()

        # Checks if --payload_list argument is set or not
        if args.payload_list:
            
            # Checks if payloads file exist or not
            if os.path.isfile(args.payload_list):
                file = open(args.payload_list, "r")
                payloads = file.readlines()
                file.close()

                # Send request to each URL with each and every payloads
                for url in urls:
                    url = url.strip()
                    for payload in payloads:
                        payload = payload.strip()
                        try:
                            t = threading.Thread(target=find_xss, args=(url, payload,))
                            t.start()
                        except:
                            pass
            else:
                print("File {file} is not present.".format(file=args.payload_list))
        
        # Checks if --payload argument is set or not
        elif args.payload:
            for url in urls:
                url = url.strip()
                try:
                    t = threading.Thread(target=find_xss, args=(url, args.payload,))
                    t.start()
                except: pass
        else: print("Please provide payload or list of payloads file.")
    else:
        print("URL list file is not present")
