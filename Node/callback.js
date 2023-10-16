
// function soyAsincrona(){
//     setTimeout(function () {
//         console.log('soy una función asíncrona');
//     }, 1000);
// }
// console.log('iniciando el proceso...')
// soyAsincrona();
// console.log('terminado el proceso');


// function soyAsincrona(miCallback){
//     setTimeout(function () {
//         console.log('soy una función asíncrona');
//         miCallback();
//     }, 1000);
// }
// console.log('iniciando el proceso...')
// soyAsincrona(function() {
//     console.log('terminado el proceso');
// });


function hola(nombre, miCallback){
    setTimeout(function () {
        console.log('hola ' + nombre);
        miCallback(nombre);
    }, 1000);
}

function adios(nombre, otroCallback) {
    setTimeout(function(){
        console.log('adios ' + nombre);
        otroCallback();
    }, 1500);
    
}


console.log('iniciando el proceso...')
 hola('carlos', function(nombre) {
     adios(nombre, function() {
         console.log('terminado el proceso');    
     });
    
 });


// hola('carlos', function(){});
// adios('carlos', function(){});
    
