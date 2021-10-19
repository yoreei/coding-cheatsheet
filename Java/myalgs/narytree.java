package myalgs;

import java.lang.reflect.Array;

/*
   2
  3 4
   5 6
    7 8
     9 10
      11

    2
   3 4 6 8
    5 7 9 10
         11

    2
   3 4
    5 6
     7 8
      9 10
       11

    e
   e o
  e o
 o o

   e
  e       e
 e   e   e e
o o o o o o o o
 */
class TreeNode {
    public int value=0;
    public TreeNode sibling=null;
    public TreeNode firstChild=null;
    public TreeNode(){

    }

    @Override
    public String toString() {
        if (this.firstChild==null){
            return value + " leaf";
        }
        return value+"";
    }
}
public class narytree {
    public TreeNode lastchild(TreeNode node, int n){
        node=node.firstChild;
        while(true) {
            if (node.sibling == null) {
                return node;
            }
            node = node.sibling;
        }
    }
    public TreeNode nthchild(TreeNode node, int n){
        for(int i=1; i<n; i++){
            node=node.firstChild.sibling;
        }
        return node.firstChild;
    }

    public static void printpreorder(TreeNode root){
        if(root==null){
            return;
        }
        System.out.println(root);
        System.out.println(root+"->");printpreorder(root.firstChild);
        System.out.println(root+"--");printpreorder(root.sibling);
    }

    public static void solveIter(int m, int[] arr1){
        TreeNode root = new TreeNode();
        root.value = arr1[0];
        TreeNode lastodd = root;
        TreeNode lastchild = null;
        for (int i = 1; i < m; i++) {
            TreeNode newnode = new TreeNode();
            newnode.value = arr1[i];
            if (lastchild==null){
                lastchild = newnode;
                lastodd.firstChild=lastchild;
            }
            else{
                lastchild.sibling=newnode;
                lastchild=lastchild.sibling;
            }

            if (newnode.value % 2 == 1) { //odd
                lastodd = newnode;
                lastchild=null;
            }
        }
        printpreorder(root);
    }

    public static boolean notleaf(TreeNode node){
        return node.value % 2 == 1;
    }
    public static void addChild(TreeNode node, int value){
        TreeNode oc = node.firstChild;
        node.firstChild=new TreeNode();
        node.firstChild.value=value;
        node.firstChild.sibling=oc;
    }
    public static TreeNode _preorderRec(int m, int[] arr1, int arrCur, TreeNode cur, TreeNode root) {
        if (arrCur>=m) {
            return root;
        }
        addChild(cur,arr1[arrCur]);
        if (notleaf(cur.firstChild)) {
            return _preorderRec(m, arr1, arrCur+1, cur.firstChild, root);
        }
        else{
            return _preorderRec(m,arr1,arrCur+1, cur, root);
        }

    }
    public static void preorderRec(int m, int[] arr1){
        TreeNode root = new TreeNode();
        root.value=arr1[0];
        TreeNode result = _preorderRec(m, arr1, 1, root, root);
        printpreorder(result);
    }
    public static void main(String[] arg) {
        int[] arr1 ={3, 1, 4, 48, 2, 5, 7, 6, 18};
        //int[] arr1 = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
        int m = Array.getLength(arr1);
        //solveIter(m, arr1);
        preorderRec(m,arr1);


    }
}
