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

document.getElementById("buscar").onclick = function(){
	entrada = document.getElementById("texto").value;
	var elemts = document.getElementsByClassName('well');
	for (i = 0; i < elemts.length; i++) { 
		var text1 = elemts[i].textContent;
		if(text1.search(entrada) >= 1){
			elemts[i].setAttribute("class", "mostrar well");
		}else{
			elemts[i].setAttribute("class", " well ocultar");
		}
		
	}
		

};
/*Llamar a la función e imprimir por pantalla / mensaje de alerta*/


function OnSucess(data){
	console.log(data);

} 
(function() {
	$.ajax({
		type:"GET",
		url: "data/citas.xml",
		success: 

		});


})();

