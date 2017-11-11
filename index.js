let history = require("./history")


history = history.filter(h => h.operation !== '还书')
                 .map(h => h.name)
                 .map(h => h.split('=')[0].trim())


// history = Array.from( new Set(history));


history.forEach(h => console.log(h))
