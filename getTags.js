const agent = require('superagent');
const async = require('async');
const _ = require('underscore');
const bookTitleList = require('./book_title_list');

function sleep(milliseconds) {
  let start = new Date().getTime();
  for (let i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds) {
      break;
    }
  }
}

function random_sleep(second) {
  sleep(Math.floor((Math.random() * second) + 1) * 1000)
}

function requestTags(bookTitle, done) {
  random_sleep(5);
  agent.get(encodeURI(`https://api.douban.com/v2/book/search?q="${bookTitle}"&count=1`))
       .end((err, res) => {
           if (err) {
             console.log(err);
           } else {
             const tag = res.body.books[0].tags;
             done(null, tag);
           }
         }
       );
}


function partition(items, size) {
  let result = _.groupBy(items, function(item, i) {
    return Math.floor(i/size);
  });
  return _.values(result);
}

const milliseconds_of_one_hour = 60 * 60 * 1000;

partition(bookTitleList, 80).forEach(subList => {
  async.map(subList, requestTags, (err, tags) => {
    tags.forEach(tag => {
      console.log(tag);
    })
  });
  sleep(milliseconds_of_one_hour);
})

