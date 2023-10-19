function hola(nombre) {
    return new Promise(function (resolve, reject) {
        setTimeout(function() {
            console.log('hola ' + nombre);
            resolve(nombre);
           
        }, 1000);
    })
}

function adios(nombre) {
    return new Promise( (resolve, reject) => {
        setTimeout(function() {
        console.log('adios ' + nombre);
        resolve();
    }, 1500);
})


}

function hablar(nombre){
    return new Promise((resolve, reject) => { // usamos la sintaxis ES6
    setTimeout(function(){
        console.log('bla bla bla bla');
        //resolve(nombre);
        reject('hay un error')
        
    }, 1000);
    })

}

// llamamos a la función
console.log('iniciando el proceso....');

hola('Ariel')
    .then(hablar)
    .then(hablar)
    .then(hablar)
    .then(adios)
    .then((nombre) => {
        console.log('Terminando el proceso');
    })
    .catch(error => {
        console.log('ha habido un error: ');
        console.log(error)
    })