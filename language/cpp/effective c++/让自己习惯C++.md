# 让自己习惯C++

## 条款01：视C++为一个语言联邦

C++次语言：C, Object-Oriented C++, Template C++, STL



## 条款02：尽量以`const`, `enum`, `inline`替换`#define`

原因：所使用的的名称可能并未进入记号表(symbol table)

```c++
// #define ASPECT_RATIO 1.653
// should be below
const double AspectRatio = 1.653;
```

使用常量替换`#define`的时候有两种情况

1. 定义常量指针

   ```c++
   // char*-based string:
   const char* const authorName = "Scott Meyers";
   // or should be better below
   const std::string authorName("Scott Meyers");
   ```

2. clss专属常量

   ```c++
   class GamePlayer {
   private:
     static const int NumTurns = 5; // 声明式而非定义式
     int scores[NumTurns];
   };
   
   class CostEstimate {
   private:
     static const double FudgeFactor;  //static class 常量声明 位于头文件内
   };
   const double
     CostEstimate::FludgeFactor = 1.35;  // static class 常量定义位于实现文件内
   
   // 一个属于枚举类型的数值可以充当ints被使用
   class GamePlayer {
   private:
     enum { NumTurns = 5 };
     int scores[NumTurns];
   }
   ```

取一个`const`地址合法，取`enum`和`#define`地址不合法（可以用在不想让别人获得一个`pointer`或`reference`指向某个整数常量）

```c++
template<typename T>
inline void callWithMax(const T& a, const T& b) {
  f(a > b ? a : b);
}
```

+ 对于单纯常量，最好以`const`对象或`enums`替换`#defines`
+ 对于形似函数的宏，最好改用`inline`函数替换`#defines`



## 条款03：尽可能使用const

```c++
char greeting[] = "Hello";
char* p = greeting;							// non-const pointer, non-const data
const char* p = greeting;				// non-const pointer, const data
char* const p = greeting;				// const pointer, non-const data
const char* const p = greeting;	// const pointer, const data
```

**如果关键字`const`出现在星号左边，表示被指物是常量；如果出现在星号右边，表示指针自身是常量；如果出现在星号两边，表示被指物和指针两者都是常量**。如果被指物是常量，`const`写到类型之前或者写到类型之后、星号之前都ok

```c++
void f1(const Widget* pw);
void f2(Widget const * pw);
```

**STL迭代器系以指针为根据塑模出来，所以迭代器的作用就像个`T*`指针。声明迭代器为`const`就像声明指针为`const`一样(即声明一个`T* const`指针)，表示这个迭代器不得指向不同的东西，但它所指的东西的值是可以改动的。如果你希望迭代器所指的东西不可被改动(即希望STL模拟一个`const T*`指针)，你需要的是`const_iterator`。**

```c++
std::vector<int> vec;

const std::vector<int>::iterator iter = vec.begin(); // iter作用像T* const
*iter = 10;
// ++iter;																					 // 这个是错误的，iter是const
std::vector<int>>:const_iterator cIter = vec.begin();
// *cIter = 10;																			// 这个是错误的，*cIter是const
++cIter;
```



