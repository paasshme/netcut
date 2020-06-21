import nmap
from flask import Flask, jsonify


app = Flask(__name__)
apiPath = '/api/'

@app.route('/')
@app.route(f'{apiPath}')
def test():
	return "Page de base"
	
@app.route(f'{apiPath}getIp')
def get_all_connected_devices():

	print("no")
	nmScan=nmap.PortScanner()
	devices = nmScan.scan("192.168.0.1/23","1")


	print(devices["scan"])

	ips=[]
	for k in devices["scan"]:
		ips.append(k)
	#for k in range(int(devices['nmap']['scanstats']['uphosts'])):
	#	continue
		
	return jsonify(ips)

@app.route(f'{apiPath}<string:ip>/<int:nb>')
def cut_ip(ip,nb):
    return f'Ok for {ip}, {nb} times'

@app.route(f'{apiPath}<string:ip>/<string:hw>/<int:nb>')
def cut_ip_mac(ip,hw,nb):
    return f'Ok for {ip} linked with {hw}, {nb} times'



if __name__ == '__main__':
    app.run(debug=True)
