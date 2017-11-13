const agent = require('superagent');
const async = require('async');

bookTitles =[
  '编程珠玑',
  'Java语言程序设计',
  '怎样解题',
  '重构与模式',
  '新概念计算机英语',
  '自控力',
  '把时间当作朋友',
]


function requestTags(bookTitle, done) {
  agent.get(encodeURI(`https://api.douban.com/v2/book/search?q="${bookTitle}"&count=1`))
       .end((err, res) => {
           if (err) {
             console.log(err);
           } else {
             const tag = res.body.books[0].tags
             done(null, tag);
           }
         }
       );
}

async.map(bookTitles, requestTags, (err, tags) => {
  tags.forEach(tag => {
    console.log(tag);
  })
})
