## uses turtle;

loop 2 do begin
  down;
  loop 2 do begin
    forw(10); turn(90); forw(10); turn(90);
  end;
  up;
  forw(8); turn(360-270); forw(8); turn(360-90);
end;
turn(180); forw(6);
down;
loop 4 do begin
  forw(10); turn(270)
end;