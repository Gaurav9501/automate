//class Tree{
//int data;
//Tree left;
//Tree right;
//Tree(int data){
//this.data = data;
//left = right=null;
//}
//}



//Main class
class post{

//inner class
static class Tree {
        static int data;
        Tree left, right;
        public Tree(int data){
            this.data = data;
        }
    }


static int[] first = new int[10];
static int[] second = new int[10];
static int top;
post(){
top=-1;
}


//Traversing post order
public static void populate(int data){

}




//Main function
public static void main(String[] args){
post pos = new post();
Tree root = null;
root = new Tree(1);
root.left = new Tree(2);
root.right = new Tree(3);
root.left.left = new Tree(4);
root.left.right = new Tree(5);
root.right.left = new Tree(6);
root.right.right = new Tree(7);
pos.push(root.data);
}
}
