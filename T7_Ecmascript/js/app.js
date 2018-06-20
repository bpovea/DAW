/*
	Mi EcmaScript

	consola web
	2+2
	'hola'
	console.log('hola')
	alert('Pop Up!')
*/

/*
* Conversión de tipos
*/

/*console.log('Comentario '+100)
console.log(52+ ' Comentario ')
console.log("37" + 7)
console.log("37" - 7)

console.log(parseInt("37") + 7)
console.log(parseInt("37") - 7)
*/

function saludar(nombre) {
  return "Intro a " + nombre; //Cuando se llama, esta funcion devuelve "Hola " y el nombre que se le ha pasado como argumento.
}

/*Llamar a la función e imprimir por pantalla / mensaje de alerta*/

/*
* Funciones
* var, let y const
* BOM y DOM
* Eventos
*/

(function() {
	/*Mostrar un mensaje de alerta al cargar*/
	//alert('mensaje al cargar')

	/* Obtener el elemento con el id quote1 */
	//var elemt = document.getElementById('quote1')
	//console.log(elemt)

	/* Obtener el elemento con el id quotes */
	//elemt = document.getElementById('quotes')
	//console.log(elemt)

	/* Obtener los elementos con la etiqueta div y mostrar el contenido*/
	/*
	var elemts = document.getElementsByTagName('div')
	for(indice in elemts){
		console.log(elemts[indice])
	}

	for(elemt of elemts){
		console.log(elemt)
	}
	*/

	/* Obtener los elementos con la clase well */
	/*
	var elemts = document.querySelectorAll('div[class="well"]')
	for(elemt of elemts){
		console.log(elemt)
	}
	*/

	/* Query Selector para los div's con clase well dentro del div con id quotes */
	/*
	elemts = document.querySelectorAll('div#quotes > div[class="well"]')
	for(elemt of elemts){
		console.log(elemt)
	}
	*/

	/* Mostrar los autores de las frases */
	/*
	elemts = document.querySelectorAll('div#quotes > div[class="well"]')
	for(elemt of elemts){
		console.log(elemt.getAttribute('author'))
	}
	*/

	/* Mostrar el texto de los div's cuyo autor termine en ous */
	/*
	elemts = document.querySelectorAll('div#quotes > div[author$="ous"]')
	for(elemt of elemts){
		console.log(elemt.textContent)
	}
	*/

	/* Crear un h3 con el autor de cada div con clase well */
	/*
	elemts = document.querySelectorAll('div#quotes > div[author$="ous"]')
	for(elemt of elemts){
		var newElemt = document.createElement('h3')
		newElemt.textContent = elemt.getAttribute('author')
		console.log(newElemt)
	}
	*/

	/* Insertar el h3 antes del p dentro de la cita */
	elemts = document.querySelectorAll('div#quotes > div[class="well"]')
	for(elemt of elemts){
		var newElemt = document.createElement('h3')
		newElemt.textContent = elemt.getAttribute('author')
		elemt.insertBefore(newElemt,elemt.firstChild)
	}
	/* Obtener el texto del input con id texto */

	/* Al dar clic en el botón buscar debe ocultar las citas que no contengan el texto ingresado en input (id='texto')*/

})();

