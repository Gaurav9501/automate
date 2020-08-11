
class test{

public static int top;
public static  char[]  arr ;
test(int size){
top = -1;
arr = new char[size];
}


public static void pushh(char i){
if(top==-1){
top+=1;
arr[top]=i;
}
else
top+=1;
arr[top]=i;
}

public static void printing(){
for(int i=0;i<arr.length;i++)
System.out.println(arr[i]);	
}

//[()]
public static int checking(char c){
try{
	if(c!=')' && c!='}'&& c!= ']'){
	top+=1;
	arr[top]=c;
	}

	else{
		switch(c){
			case ')':
					while(arr[top]!='('){
					 	top-=1;
					}
						top-=1;

				break;	
			case ']':
					while(arr[top]!='['){
					top-=1;					
					}
					top-=1;
					break;

			case '}':
                                        while(arr[top]!='{'){
                                        top-=1;
                                        }
                                        top-=1;
                                        break;

	}

	}

}catch(Exception e){System.out.println("not balanced");}
return top;
}


public static void main(String[] args){
String s = "[()] ";
int check=0;
int size = s.length();
test par = new test(size);
String[] ss = s.split("");

for(int i=0;i<s.length();i++)
 check=par.checking(s.charAt(i));
if(check==-1)
System.out.println("balanced");
}
}
