class insertion {


public static int[] insertionsort(int[] arr){
int value = 0;
int index=0;
int temp =0
;for(int i=0;i<arr.length;i++){
value = arr[i];
index = i;
while(index>0){
if(arr[index]<arr[index-1]){
temp =arr[index];
arr[index]=arr[index-1];
arr[index-1]=temp;
}
index--;
}
}
return arr;
}

public static void main(String[] args){
int[] arr={7,2,4,1,5,3};
arr = insertionsort(arr);

for(Integer i:arr)
System.out.println(i);
}}
