import java.util.*;

class Balance{
public static void main(String[] args){

Stack<Character> str = new Stack<Character>();
String s = "[ ( ] ) ] { } ";
int i = 0;

while(i<s.length()){
    if(str.isEmpty() && s.charAt(i)=='(' ||  s.charAt(i)=='['){
    System.out.println("not balanced");
    System.exit(0);}
	if(s.charAt(i)=='(' ||  s.charAt(i)=='[')
	str.push(s.charAt(i));

	if(s.charAt(i)==')'){                  
	str.push(s.charAt(i));
	while(str.pop()!=')'){}
	str.pop();
	}

	if(s.charAt(i)==']'){
	str.push(s.charAt(i));
	while(str.pop()!=']');{}
	str.pop();
	}
	i++;
}

if(str.isEmpty())
System.out.println("Balanced");
else
System.out.println("Not balanced");


for(Character t:str)
System.out.println(t);

}}

