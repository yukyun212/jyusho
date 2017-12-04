# -*- coding: utf-8 -*-
from flask import Flask
import geocoder
app = Flask(__name__)
def main():
	address4 = "こちらは南越消防組合です。１３：０１頃、発生した越前市高瀬１丁目付近の防火地域建物火災は、１３：１７鎮火しました。以上。"
	#Localname = u"越前市北府２丁目付近"
	city = address4.find('越前市')
	city2 = address4.find('付近')

	str=address4
	slice = str[city:city2] 
	print (slice.replace('◆',''))
	Localname = slice.replace('◆','')
	g = geocoder.google(Localname)
	a=g.latlng
	print (a)
@app.route('/')
def index():
	main()
	return print(a)

if __name__ == '__main__':
	app.run()