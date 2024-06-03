; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
main_entry:
  %".2" = add i32 4, 5
  %".3" = alloca i32
  store i32 %".2", i32* %".3"
  %".5" = alloca i32
  store i32 3, i32* %".5"
  %".7" = load i32, i32* %".3"
  %".8" = load i32, i32* %".5"
  %".9" = add i32 %".7", %".8"
  store i32 %".9", i32* %".3"
  %".11" = load i32, i32* %".3"
  %".12" = load i32, i32* %".5"
  %".13" = mul i32 %".12", 2
  %".14" = add i32 %".11", %".13"
  store i32 %".14", i32* %".3"
  ret i32 69
}
