// Requireds
const {createTable} = require('./genered-tables')


const argv = process.argv;

/* Leyendo los argumentos y buscando las variables que necesitamos
 NOTA: debe existir ya una libreria que haga esto mejor.
 Buscarla cuando haya internet */
let params = {};
argv.forEach( (element) => {
//    Filtramos los elementos por aquellos que comienzon con '--'
    if  (element.slice(0,2) == '--') {
        // Dividimos el argumento en 'clave' y 'valor'
        param = element.slice(2).split('=');
        let key = param[0];
        let value = param[1];

        // Creamos un JSON con los valores y lo retornamos
        params[`${key}`] = value
    }
})
console.log(params)
createTable(params.base,params.limit)

    .then( fichero => console.log(`Fue creado con exito ${fichero}`))
    .catch( e => console.log(e))