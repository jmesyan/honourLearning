(function (name, definition) {
// 检测上 文环境是否为AMD CMD
var hasDefine = typeof define === 'function',
// 检查上 文环境是否为Node
hasExports = typeof module !== 'undefined' && module.exports;
if (hasDefine) {
// AMD环境 CMD环境 
    define(definition);
    console.log(1111);
} else if (hasExports) {
// 定义为 通Node模块 
    module.exports = definition();
    console.log(2222);
} else {
// 将模块的执行结  在window 量中 在  器中this  window对象 
    this[name] = definition();
    console.log(3333);
}
})('hello', function () {
var hello = function () {console.log("hello")};
return hello; });

console.log(module.exports);
module.exports();

