from xml.dom.minidom import parse
import xml.dom.minidom

def ultimoNodo(node) :
	# obtengo los atributos y los muestro
	if node.hasChildNodes() :
		for key in node.attributes.keys() :
			print "%s" % (node.attributes[key].nodeValue)
			
	# verifico si no tiene mas hijos, en ese caso muestro su información
	if (node.hasChildNodes() and node.childNodes.length == 1) :
		print "%s" % (node.childNodes[0].data)
		return
	
	# si tiene mas nodos hijos, vuelvo a llamar a la funcion
	for hijoNode in node.childNodes :
		ultimoNodo(hijoNode)

archivo = raw_input("Ingrese el archivo a parsear:")
domTree = xml.dom.minidom.parse(archivo)
collection = domTree.documentElement
for node in collection.childNodes :
	ultimoNodo(node)
