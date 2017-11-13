let history = require("./history")


history = history.filter(h => h.operation === '借书')
                 .map(h => h.name)
                 .map(h => h.split('=')[0].trim())


history = Array.from(new Set(history));

// console.log(history.length);
history.forEach(h => console.log(h))
