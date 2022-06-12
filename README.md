# Reflected Cross Site Scripting (R-XSS) Automation Tool
This simple python script will take URLs and payloads through stdin and checks if the payload is getting reflected back in the response, and that way it is finding reflected XSS.

# Usage
<img src="/uploads/xss-automation.gif" width="80%" alt="xss automation">
<pre><code>
usage: xss-automation [-h] [-u] [-l] [-p] [-P]

Reflected Cross Site Scripting (R-XSS) Autotmation Tool

options:
  -h, --help            show this help message and exit
  -u , --url            enter the URL (URL should be provided in proper format)
  -l , --list           enter the path to file of list of URLs
  -p , --payload        enter the payload you want to inject
  -P , --payload_list   enter the path to file of list of payloads
</pre></code>

# Installation
Clone the repository
<pre><code>git clone https://github.com/mmbverse/xss-automation.git
cd xss-automation
</pre></code>
Python
<pre><code>pip install -r requirements.txt
python xss-automation.py
</pre></code>
Bash
<pre><code>pip3 install -r requirements.txt
chmod +x xss-automation.py

# copy to /usr/local/bin to access the tool from anywhere
sudo cp xss-automation.py /usr/local/bin/xss-automation
</pre></code>
