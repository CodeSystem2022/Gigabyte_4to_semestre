// this === global = true

// mostarr en consola
//console.log();

//mostrar un mensaje en forma de error
//console.error();

//ejecutar un código después de un intervalo de tiempo
//seTimeout(() => {});

//Ejecutar un código cada intervalo de tiempo
//setInterval(() => {});

// da prioridad de ejecución a una función asincronica 
//setImmediate(() => {});


console.log(global);

console.log(setInterval);

let i = 0;
let intervalo = setInterval(() => {
   console.log('hola');
   if (i === 3){
       clearInterval(intervalo); //detenemos la función

   }
   i++;
}, 1000);


setImmediate(() =>{
    console.log('saludo inmediato');
});


//require();

//console.log(process);

//console.log(__dirname);

console.log(__filename);


global.miVariable = 'mi variable global';
console.log(miVariable);




