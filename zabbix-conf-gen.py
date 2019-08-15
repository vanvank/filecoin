#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader

hostname="adfhdsgfsdbfnsdf"


env = Environment(loader = FileSystemLoader("./"))
template = env.get_template("zabbix-agent-conf.j2")  

content = template.render(hostname=hostname)

with open('./test.conf','w+') as fp:
	fp.write(content)
