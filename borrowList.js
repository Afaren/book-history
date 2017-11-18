const history = require("./history")

const borrowHistory = history.filter(h => h.operation === '借书')
                 .map(h => h.name)
                 .map(h => h.split('=')[0].trim())

const distinctBorrowHistory = Array.from(new Set(borrowHistory));

module.exports = distinctBorrowHistory;