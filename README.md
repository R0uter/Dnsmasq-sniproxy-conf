## sni.conf
sni.conf is a configuration of dnsmasq.

If you want to use dnsmasq+sniproxy plan to against the "Girl Friend Wall",you will need  `/etc/dnsmasq.d/sni.conf` .


## gfwlist2dnsmasq-sni-conf.py

I didn't wrote this code,it based on https://github.com/cokebar/gfwlist2dnsmasq !

## How to use 
gfwlist2dnsmasq-sni-conf.py is a tool aim to convert gfwlist into sni.conf ,just use `python gfwlist2dnsmasq-sni-conf.py` to start it.

It will automatically download the latest gfwlist and execute convert.

But ensure set your SNI Proxy Server IP before run the code. Edit `gfwlist2dnsmasq-sni-conf.py` find like this:


`sni = '127.0.0.1'`

Change `127.0.0.1` to your SNI Proxy Server IP.

##And

Feel free to download the pre-generated sni.conf if you r not need updated version of gfwlist.

:)


