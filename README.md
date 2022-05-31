# rxss
This simple python script will take URLs and payloads through stdin and checks if the payload is getting reflected back in the response, and that way it is finding reflected XSS.

# Usage
<pre><code>
usage: rxss [-h] [-u] [-l] [-p] [-P]

Cross Site Scripting (XSS) Autotmation Tool

options:
  -h, --help            show this help message and exit
  -u , --url            enter the URL (URL should be provided in proper format)
  -l , --list           enter the path to file of list of URLs
  -p , --payload        enter the payload you want to inject
  -P , --payload_list   enter the path to file of list of payloads
  
  </pre></code>
