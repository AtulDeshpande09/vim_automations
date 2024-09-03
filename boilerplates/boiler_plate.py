import sys

def generate_html_template():
    return """<!DOCTYPE HTML>
<html lang="en">
    
<head>
    <title>MyPage</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
</head>

<body>

    <h1>First heading </h1>

    <!-- Start from here -->


</body>

</html>"""


def generate_java_template():
    return """public class MyClass {

   /* This is java boiler plate.
    * This will print 'Hello World' as the output
    */

   public static void main(String []args) {
      System.out.println("Hello World");
   }
}"""

def generate_cpp_template():
    return """#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}"""

def generate_c_template():
    return """#include <stdio.h>

int main(void) {
    // This is the main function of the program
    printf("Hello, World!\n");

    return 0;
}"""

def generate_cSharp_template():
    return """namespace MyProject;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}"

def generate_css_template():
    return "*{
margin: 10px;

padding: 10px;

box-sizing: border-box;
}

html {
height: 100%;
}
body {
min-height: 100%;
background-color:black;
}"""



if __name__=="__main__":
    if len(sys.argv) >1:
        boilerplate_type = sys.argv[1]

        if boilerplate_type == "cpp":
            print(generate_cpp_template())
            
        elif boilerplate_type=="java":
            print(generate_java_template())
            
        elif boilerplate_type =="html":
            print(generate_html_template())
            
        elif boilerplate_type=="csharp":
            print(generate_cSharp_template())
            
        elif boilerplate_type =="c":
            print(generate_c_template())
        elif boilerplate_type =="css":
            print(generate_css_template())
            
        else:
            print("Look what are you typing fella!")

    else:
        print("Usage : boilerplate.py <type>")
