var k,k1,k2,k3,i:integer; 
begin 
repeat 
readln(k); 
until (k>=1) and (k<=180); 
if k>99 then begin 
k1:=k div 100; 
k2:=k mod 100 div 10; 
k3:=k mod 100 mod 10; 
for i:=10 to 99  
if (i mod 10=k1) or (i mod 10=k2) or (i mod 10=k3) 
or (i div 10=k1) or (i div 10=k2) or (i div 10=k3) 
then write(i:3); 
end; 
if k<10 then begin 
for i:=10 to 99 do 
if (i mod 10=k) or (i div 10=k) 
then write(i:3); 
end; 
end.

