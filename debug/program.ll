; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
main_entry:
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %".4" = alloca i32
  store i32 3, i32* %".4"
  ret i32 69
}
