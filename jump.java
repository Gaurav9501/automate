class jump{
public static void linear(int x,int start,int[] arr,int step){
for(int i=start;i<start+step;i++)
if(arr[i]==x){
System.out.println("Fond at: "+i);
break;
}
}

public static void jumpsearch(int[] arr, int x){
int n = arr.length;
int step =(int)Math.floor(Math.sqrt(n));
int index = 0;

while(arr[index]!=x){
if(arr[index]>x){
index-=step;
linear(x,index,arr,step);
break;
}
index+=step;
}

}


public static void main(String[] args){
int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610}; 
int x = 55;
jumpsearch(arr,x);
}
}
