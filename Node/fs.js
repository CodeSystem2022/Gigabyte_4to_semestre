const fs = require('fs');

// primero leemos el archivo
// function leer(ruta, cb){
//     fs.readFile(ruta, (err, data) => {
//         console.log(data.toString());
//     })
// }

// leer(__dirname + '/archivo.txt');


function leer(ruta, cb){
    fs.readFile(ruta, (err, data) => {
        cb(data.toString());
    })
}

leer(`${__dirname}/archivo.txt`, console.log);


// segundo escribimos archivo1.txt creandolo

function escribir(ruta, contenido, cb) {
    fs.writeFile(ruta, contenido, function (err){
        if (err) {
            console.log (' no se ha podido escribir');
        }else {
            console.log('se ha escrito correctamente');
        }
    })

}

// Tercero eliminamos el archivo1.txt
function borrar(ruta, cb) {
    fs.unlink(ruta, cb); // elemina de manera asincrona 
}

borrar(`${__dirname}/archivo1.txt`, console.log);

//sintaxis ES6
// escribir(`${__dirname}/archivo1.txt`,'reescribimos el archivo', console.log);


