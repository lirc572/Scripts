#!/usr/bin/env python3

import sys

try:
    import pyperclip
except:
    pass

disclaimer = '''
NAME:
    clkgen.py

SYNOPSIS: 
    [python3] clkgen.py [-s source_frequency] [-t target_frequency] [--code] [-h/--help]

DESCRIPTION:
    clkgen.py generates the verilog code of a module that takes a clock input and convert it to a clock output of a different frequency. If the output frequency provided is not a multiple of the input frequency, a rounded result would be given.

    clkgen.py was written for NUS EE2026 Digital Design.

OPTIONS:
    -s source_frequency
            Indicate the frequency of the source clock in Hz, usually the frequency of the clock source of the development board.

    -t target_frequency
            Indicate the frequency of the output clock in Hz, put the desired frequency for your use.

    --code  Show the Verilog code for the module

    -h/--help
            Show this help page

NOTE:
    The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement, in no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
'''

mod_code = '''//%.2fHz
module Clk%s(
    input cin,
    output reg cout
    );
    reg [%d:0] counter = %s'b0;
    always @ (posedge cin) begin
        counter <= (counter==%s) ? %s'b0 : counter + 1;
    end
    always @ (posedge cin) begin
        cout <= counter == %s'b0;
    end
endmodule
'''

calcounter = lambda freq, cin: (lambda b: str(len(b))+"'b"+b)(bin(int(1/freq*cin))[2:])

get_code = lambda freq, cin: (lambda x: mod_code % (freq, 'p'.join(("%.2f" % (freq,)).split('.'))+"hz", int(x.split('\'')[0])-1, x.split('\'')[0], x, x.split('\'')[0], x.split('\'')[0]))(calcounter(freq, cin))

def main():
    source = 100000000
    target = 1.75
    showcode = False
    reset_pin = False
    for v in range(len(sys.argv)):
        if sys.argv[v] == '-s':
            src = int(sys.argv[v+1])
        elif sys.argv[v] == '-t':
            target = float(sys.argv[v+1])
        elif sys.argv[v] == '--code':
            showcode = True
        elif sys.argv[v] in ('-h', '--help'):
                print(disclaimer)
                return 0
    print("Your input:")
    print("  input freq: " + str(source) + "Hz")
    print("  output freq: " + str(target) + "Hz")
    print()
    if showcode:
        print("Verilog Code:\n")
        code = get_code(target, source)
        print(code)
        try:
            pyperclip.copy(code)
            print("\n\\\\Code copied to clipboard")
        except:
            print("\n\\\\To automatically copy code to clipboard, do `pip install pyperclip`")
    else:
        print("Counter upper bound:")
        print(calcounter(target, source))
    return 0

if __name__ == '__main__':
    main()
