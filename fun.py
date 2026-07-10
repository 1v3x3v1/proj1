import subprocess
import sys
import platform
import urllib.parse
global domain
domain=input('Domain Name: ')
if len(domain)<1 or domain==False:
	domain= 'google.com'
##########################
def check_connection(domain, count=3):
    try:
        result = subprocess.run(
            ['ping', '-c', str(count), '-W', '2', domain],
            #''stdout=subprocess.PIPE,
            #stderr=subprocess.PIPE,
            timeout=10
        )
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⚠️  Ping timed out")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

###################################
if len(sys.argv)<2:
	print("USE: python weather.py '<location>'")
	city=""
else:
	city = sys.argv[1]

encoded_query=urllib.parse.quote(city)

searchUrl =f"'https://www.{domain}/maps/place/{encoded_query}';"

with open("script.js","r") as f:
	d=f.readlines()
	
	modified=False
	for i,l in enumerate(d):
    		if 'window.location=' in l:
    			d[i]= f'\twindow.location= {searchUrl}\n'
    			modified= True
    			break
	if not modified:
    		print("Warning: No line found in script.js")
with open("script.js", "w") as f:
    f.write(''.join(d))
print(f"URL: {searchUrl}")

if check_connection(domain):
    print("CONNECTION UP")
    
else:
    print("X CONNECTION DOWN")
    sys.exit(1)
	
###############################################################################################
if platform.system() == 'Darwin':  # macOS
    subprocess.run(['open', 'index.html'])
elif platform.system() == 'Windows':
    subprocess.run(['start', 'index.html'], shell=True)
else:  # Linux
    subprocess.run(['xdg-open', 'index.html'])
########################################################################################

