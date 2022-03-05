const lineReader = require('line-reader');
var index = 0;
lineReader.eachLine('heart.csv',(line,last)=>{
    console.log(index + "," + line);
    index++;
})