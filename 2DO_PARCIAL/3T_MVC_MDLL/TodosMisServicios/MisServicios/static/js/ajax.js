function crearServicio(mensaje){
    alert("servicio cargado con exito");

}

function agregar(){
    $(document).ready(function(){
        $("#mostrarmodal").modal("show");
        $(".modal-dialog").attr("style","height: 378px; z-index: 2;")
        });
}


function guardar(){
    info ={
        "nombre":$("#nombre").val(),
        "servicio":$("#servicio").val(),
        "registro":$("#registro").val(),
        "direccion":$("#direccion").val(),

    }
    //guardar
    $.ajax({
        url: "/usuarios/",
        type:"POST",    
        dataType : 'json',
        data:info,
        success :crearServicio,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos de las preguntas.');
        }
    });


};