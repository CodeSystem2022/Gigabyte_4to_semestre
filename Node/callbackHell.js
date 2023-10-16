
function hola(nombre, miCallback){
    setTimeout(function () {
        console.log('hola ' + nombre);
        miCallback(nombre);
    }, 1000);
}

function hablar(callbackHablar) {
    setTimeout(function() {
        console.log('bla bla bla bla');
        callbackHablar();
        
    }, 1000);
}

function adios(nombre, otroCallback) {
    setTimeout(function(){
        console.log('adios ' + nombre);
        otroCallback();
    }, 1500);
    
}

// Funcion recursiva
function conversacion(nombre, veces, miCallback){
    if (veces> 0) {
        hablar( function () {
            conversacion(nombre, --veces, miCallback); 

            });
         } else {
            miCallback(nombre, miCallback);
    }
 
}


// *** Proceso Principal *** 

console.log('iniciando el proceso...')
hola('Ariel', function(nombre) {
    conversacion(nombre, 6, function(){
        console.log('terminado el proceso.....');  
        });
    });
       


// hola('carlos', function(nombre) {
//      hablar(function(){
//         hablar( function() {
//             hablar( function() {
//                 adios(nombre, function(){
//                     console.log('terminado el proceso.....');  
//                 }); 
//             });
//         });                         
//     });
// });
 
