program Ljflisp;
uses sysutils,crt;

var pi : double= 3.0;

procedure calculate(number : int64);
var v:int64;
var s: double  = 1.0;
var c: double = 2.0;

(* Here the main program block starts *)
begin
   for v:= 1 to number do
   begin
   pi:= pi+(s*(4.0/(c*(2.0+(c*(c+3.0))))));
   s := -s;
   c := c+2;
   //#writeln('Hello, World!!!');
   //readkey;
   end;
  end;
begin
  ClrScr;
  calculate(1000000);
  writeln('pi= ',formatFloat('',pi));
end.
//ohYey!!!program Ljflisp;