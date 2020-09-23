import java.util.*;

class LongestValidSubstring{
public static void main(String[] args)throws Exception{
Stack<Character> str = new Stack<Character>();
String s = "()(()))))";
int count=0;
int i=0;
int value=0;
while(i<s.length()){
	if(s.charAt(i)=='('){
	System.out.println("pushing: "+s.charAt(i));
	str.push(s.charAt(i));
	}
	if(s.charAt(i)==')' && !str.isEmpty()){
		System.out.println("Found: "+s.charAt(i));
		str.push(s.charAt(i));
		count++;
//		str.push(s.charAt(i));
		while(str.pop()!='('){
		count++;
		}
	}
i++;
}
System.out.println(count);
}}
