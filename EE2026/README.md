# EE2026

EE2026 Related Stuff

## clkgen.py

Installation:
```bash
$ git clone https://github.com/lirc572/EE2026.git
$ cd EE2026/scripts
$ pip3 install pyperclip #if you want to automatically copy the generated code to clipboard
$ chmod +x ./clkgen.py
```

How-to:
```bash
$ ./clkgen.py -h
```

Example:

```bash
$ ./clkgen.py -s 100000000 -t 3.00 --code
Your input:
  input freq: 100000000Hz
  output freq: 3.0Hz

Verilog Code:

//3.00Hz
module Clk3p00hz(
    input cin,
    output reg cout
    );
    reg [24:0] counter = 25'b0;
    always @ (posedge cin) begin
        counter <= (counter==25'b1111111001010000001010101) ? 25'b0 : counter + 1;
    end
    always @ (posedge cin) begin
        cout <= counter == 25'b0;
    end
endmodule


\\Code copied to clipboard
```
