// 加入  nextTick()的回调函数
process.nextTick(function () { 
    console.log('nextTick  执行1'); 
});
process.nextTick(function () { 
    console.log('nextTick  执行2');
}); 
// 加入  setImmediate()的回调函数
setImmediate(function () {
  console.log('setImmediate  执行1'); // 进入  循环 
  process.nextTick(
    function () {
        console.log(' 势 入'); 
    });
});
setImmediate(function () {
    console.log('setImmediate  执行2'); 
});
console.log('正常执行');

// 正常执行
// nextTick  执行1
// nextTick  执行2
// setImmediate  执行1
// setImmediate  执行2
//  势 入