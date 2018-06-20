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
		if(text1.search(entrada) >= 0){
			elemts[i].setAttribute("class", "mostrar well");
		}else{
			elemts[i].setAttribute("class", " well ocultar");
		}
		
	}
		

};
/*Llamar a la función e imprimir por pantalla / mensaje de alerta*/


function OnSucess(data){
	

} 
(function() {
    $.ajax({
        url: "data/citas.xml",
        type:"GET",    
        dataType : 'xml',
     
        success : function(xml) {
        var parseXml = xml.getElementsByTagName('cita');
        // var parseXml = $(xml).find('cita'); 
        var cites = document.getElementById("quotes"); 
        for (i = 0; i < parseXml.length; i++) {
            var node = document.createElement("div");
            node.setAttribute("class","well text-info");
            node.setAttribute("author",parseXml[i].childNodes[1].textContent);  
            var textP = document.createElement("p");    
            textP.textContent = parseXml[i].childNodes[3].textContent;
            node.appendChild(textP);                    
            cites.appendChild(node);
            }  
         },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema');
        },
        complete : function(xhr, status) {
            //alert('código a ejecutar sin importar si la petición falló o no');
        }
    });
    

     $.ajax({
        url: "data/clasicos.json",
        type:"GET",    
        dataType : 'json',
        success : function(json) {
        var cites = document.getElementById("quotes"); 
        for (i = 0; i < json.libros.length; i++) {
            var node = document.createElement("div");
            node.setAttribute("class","well text-success");
            node.setAttribute("author",json.libros[i].autor);
            var titulo = document.createElement("h3");  
            titulo.textContent = json.libros[i].titulo;
            var textP = document.createElement("p");   
            textP.textContent = json.libros[i].resumen ;
            node.appendChild(titulo);  
            node.appendChild(textP);                    
            cites.appendChild(node);
            }  
         },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema');
        },
        complete : function(xhr, status) {
            //alert('código a ejecutar sin importar si la petición falló o no');
        }
    });


})();

