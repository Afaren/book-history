let history = require("./history")


history = history.filter(h => h.operation === '借书')
                 .map(h => h.name)
                 .map(h => h.split('=')[0].trim())


history = Array.from(new Set(history));

history = history.map(h => `"${h}"`)
       .join(',\n')


console.log("module.exports = [")
console.log(history);
console.log("]")
