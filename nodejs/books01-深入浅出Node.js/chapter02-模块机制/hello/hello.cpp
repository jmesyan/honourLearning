#include <node.h>

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Object;
using v8::String;
using v8::Value;
 
void CAMOpen(const FunctionCallbackInfo<Value>& args) {
  Isolate* isolate = args.GetIsolate();
  args.GetReturnValue().Set(String::NewFromUtf8(isolate, "cam_open..."));
}
 
void init(Local<Object> exports) {
  NODE_SET_METHOD(exports, "CAMOpen", CAMOpen);
}
 
NODE_MODULE(FaceRecognition, init)