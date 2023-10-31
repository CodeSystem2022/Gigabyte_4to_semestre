
// la palabra async no es necesaria en la funciones, porque ya son asincronas
// igual proyectan una syncronia visual

async function hola(nombre) {
    return new Promise(function (resolve, reject) {
        setTimeout(function() {
            console.log('hola ' + nombre);
            resolve(nombre);
           
        }, 1000);
    })
}

async function hablar(nombre){
    return new Promise((resolve, reject) => { // usamos la sintaxis ES6
    setTimeout(function(){
        console.log('bla bla bla bla');
        //resolve(nombre);
        resolve(nombre)
        
    }, 1000);
    })

}

async function adios(nombre) {
    return new Promise( (resolve, reject) => {
        setTimeout(function() {
        console.log('adios ' + nombre);
        resolve();
    }, 1500);
})


}

//await hola('Ariel'); // esto es mala syntaxis 
// await es solo es válido dentro de una función asincrona 

async function main(){
    let nombre = await hola('Ariel');
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
    console.log('terminamos el proceso....')    
}
console.log('empezamos el proceso....')    
main();
console.log('esto va a ser la segunda instrucción....')    

//------------------------------------------------------------



// la palabra async no es necesaria en la funciones, porque ya son asincronas
// igual proyectan una syncronia visual

async function hello(name) {
    return new Promise(function (resolve, reject) {
        setTimeout(function() {
            console.log('hello ' + name);
            resolve(name);
           
        }, 1000);
    })
}

async function talk(name){
    return new Promise((resolve, reject) => { // usamos la sintaxis ES6
    setTimeout(function(){
        console.log('bla bla bla bla');
        //resolve(nombre);
        resolve(name)
        
    }, 1000);
    })

}

async function godbye(name) {
    return new Promise( (resolve, reject) => {
        setTimeout(function() {
        console.log('godbye ' + name);
        resolve();
    }, 1500);
})


}

//await hola('Ariel'); // esto es mala syntaxis 
// await es solo es válido dentro de una función asincrona 
// en ingles
async function main(){
    let name = await hello('Ariel');
    await talk();
    await talk();
    await talk();
    await godbye(name);
    console.log('process completed....')    
}
console.log('starting asyn process....')    
main();
