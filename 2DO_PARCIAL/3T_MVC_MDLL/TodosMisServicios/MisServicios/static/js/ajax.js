//apertura del modal para agregar
function agregar(){
    //botones para ver/eliminar
    $('a[type="submit"]').remove();
    $('input').attr("readonly",false);
    $('#nombre').attr("readonly",true);
    $("#registro").attr('type','date');
    selectInput();
    $('div.modal-body').append($('<a type="submit" class="btn btn-primary" onclick="guardar()">Crear servicios</a>'));
    $("#mostrarmodal").modal("show");
    $(".modal-dialog").attr("style","height: 378px; z-index: 2;");
}

//despues de eliminar/editar se actualizar la tabla de servicios 
function actualizarListaServicios(){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: "/usuario/"+$("#id").val(),
        type:"GET",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        success :function(lista) {
            html = "";
            for (var i = 0; i < lista.servicios.length; i++) {
                var fecha = new Date(lista.servicios[i].fecha);
                html += '<tr id="row' + lista.servicios[i].id + '">';
                html += '<td> ' + lista.servicios[i].servicio.nombre +'</td>';
                html += ' <td> ' + lista.servicios[i].direccion + '</td>';
                html += '<td> ' + (fecha.getDate() + 1) + "-" + (fecha.getMonth()+1) + "-" + fecha.getFullYear() + '</td>';  //|date:"d-m-Y"
                html += '<td><a class="btn btn-primary " onclick="ver(row' + lista.servicios[i].id + ')">ver</a></td></tr>';
            }
            $("tr[id]").remove();
            $("table").append(html);
        },
        error : function(xhr, status) {
            alert(xhr['responseJSON']);
        }
    });
}

function editarServicioDeUsuario(element){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={
        "servicio":$("#servicio").val(),
        "direccion":$("#direccion").val(),
    }
    $.ajax({
        url: "/usuario_servicio/"+$("#id").val(),
        type:"PUT",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
            alert("Servicio asociado al usuario modificado con éxito");
            $("#mostrarmodal").modal("hide");
            actualizarListaServicios();
        },
        error : function(xhr, status) {
            alert(xhr['responseJSON']);
        }
    });
}

function eliminarServicioDeUsuario(element){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={
        "servicio":$("#servicio").val(),
    }
    $.ajax({
        url: "/usuario_servicio/"+$("#id").val(),
        type:"DELETE",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
            alert("Servicio asociado al usuario eliminado con éxito");
            $("#mostrarmodal").modal("hide");
            actualizarListaServicios();
        },
        error : function(xhr, status) {
            alert(xhr['responseJSON']);
        }
    });
}

//modal para editar/eliminar un servicio asociado a un usuario
function ver(element){
    $('#servicio option').remove();
    $('#servicio').append('<option>' + $(element)[0].getElementsByTagName('td')[0].textContent + '</option>').attr('readonly',true);
    $("#registro").attr('type','text');
    $("#registro").val($(element)[0].getElementsByTagName('td')[2].textContent).attr('readonly',true);
    $("#direccion").val($(element)[0].getElementsByTagName('td')[1].textContent);
    $('a[type="submit"]').remove();
    $('div.modal-body').append($('<a type="submit" class="btn btn-primary" onclick="guardar()">Crear servicios</a>'));

    btneditar = $('a[type="submit"]').attr('onclick','editarServicioDeUsuario(this)');
    btneditar[0].text ='Editar editar';
    btnEliminar = $('<a type="submit" class="offset-md-5 btn btn-primary" onclick="eliminarServicioDeUsuario(this)">Eliminar servicio</a>');
    btneditar.after(btnEliminar);
    $("#mostrarmodal").modal("show");
    $(".modal-dialog").attr("style","height: 378px; z-index: 2;");
}


//para crear un nuevo servicios asociado a un usuario
function guardar(){
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    info ={
        "nombre":$("#nombre").val(),
        "servicio":$("#servicio").val(),
        "registro":$("#registro").val(),
        "direccion":$("#direccion").val(),
    }
    //guardar
    $.ajax({
        url: "/usuario/"+$("#id").val(),
        type:"PUT",    
        dataType : 'json',
        headers:{"X-CSRFToken": crf_token},
        data:info,
        success :function(respuesta) {
            alert("servicio cargado con éxito");
            $("#mostrarmodal").modal("hide");
            actualizarListaServicios();
        },
        error : function(xhr, status) {
            alert(xhr['responseJSON']);
        }
    });
};
//cargar elementos del select
function selectInput(){
    $.ajax({
        url: "servicios/",
        type:"GET",    
        dataType : 'json',
        success: function(lista) {
            $('#servicio option').remove();
            html = "";
            for (var i = 0; i < lista.length; i++) {
                html += '<option>' + lista[i].nombre + '</option>';
            }
            $('#servicio').append(html);
        },
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar la lista de servicios.');
        }
    });
}
$(document).ready(function() {
    selectInput();
    
    
});
