const fs = require('fs')

/**
 * Genera un string con la tabla de multiplicar
 * de 'base' desde 1 hasta 'limit'.
 * 
 * Retorna un objeto que contiene:
 *  - Una variable 'data', con el string generado.
 *  - La variable 'base'
 * 
 * 
 * @param {number} base 
 * @param {number} limit
 */
const generedTable = (base, limit) => {
    let data = '';
    for (let n = 1; n <= limit; n++) {
        data += `${base} x ${n} = ${base*n}\n`;
    }

    return {
        base,
        data
    };
}


/**
 * Crea e Imprime en un archivo txt el contenido de
 * una tabla de multiplicar de base => 'base' y limite =>'limit'.
 * 
 * 
 * @param {number} base
 * @param {number}limit
 * 
 * @returns {string} Retorna un String con el nombre del fichero creado.
 */
const createTable = (base, limit) => new Promise ( (resolve, reject) => {
    if (!Number(base) | !Number(limit)) {
        reject(`Alguno de los parametros('${limit}' o '${base}') no es un numero.`);
        return;
    }   
    const table = generedTable(base, limit)

    fs.writeFile(`tables/tabla-del-${table.base}.txt`, table.data, (err) => {
        if (err)
            reject(err)
        else
            resolve(`tabla-del-${table.base}.txt`);
    });

});

module.exports = {
    createTable
};