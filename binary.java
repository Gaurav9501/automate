class binary{

public static void search(int element, int[] arr,int start,int end){
int mid = (start+end)/2;
if(arr[mid]==element){
System.out.println("Found");
return;
}

else if(arr[mid]<element)
search(element,arr,mid+1,arr.length);
else if(arr[mid]>element)
search(element,arr,0,mid-1);
}

public static void main(String[] args){
int[] arr = {2,5,8,12,16,23,38,56,72,91};
int start=0;
int end = arr.length-1;
search(8,arr,start,end);
}}
