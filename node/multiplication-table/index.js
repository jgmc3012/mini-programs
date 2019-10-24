// Requireds
const {createTable, printTable} = require('./genered-tables')
const argv = require('./config-yargs').argv

function valideParam(number1, number2) {
    if (!Number(number2) | !Number(number1)) {
        console.log(`Alguno de los parametros('${number1}' o '${number2}') no es un numero.`);
    }
    return (Number(number2) | Number(number1))
}
let command = argv._[0];

switch (command) {
    case 'crear':
        if (valideParam(argv.base,argv.limite)) {
            createTable(argv.base,argv.limite)
                .then( fichero => console.log(`Fue creado con exito ${fichero}`))
                .catch( e => console.log(e))
        }
        break;
    
    case 'listar':
        console.log(valideParam(argv.base, argv.limite));
        
        if (valideParam(argv.base, argv.limite)) {
            printTable(argv.base, argv.limite)
        }
        break;
    
    default:
        console.log(`${command} no es un comando reconocido.`);        
        break;
}