#include <cstdio>

void hello(int a) {
  printf("Hello world: %i\n", a);
}

#include <cbind_example.h>

void init(v8::Handle<v8::Object> exports) {
  
  cbind::init_example(exports);
}

NODE_MODULE(tov8_example, init);