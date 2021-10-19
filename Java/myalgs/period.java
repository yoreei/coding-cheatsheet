package myalgs;
/*
1 2 3 4 1 2 3 4
  1 2 3 4 1 2 3
    1 2 3 4 1 2
      1 2 3 4 5
        1 2 3 4

 */

import java.util.*;

import static java.lang.Math.sqrt;

public class period {
//    public static void fperiod(int[] arr, int n){
//        int T=n;
//        for (int i=1; i<n/2;i++){
//            boolean found=true;
//            for (int j=i; j<n/2-1;j++){
//                if(arr[i]!=arr[j]){
//                    found=false;
//                    break;
//                }
//            }
//            if (found==true){
//                T=i;
//            }
//        }
//        System.out.println(T);
//    }
    public static boolean isequal(int[] arr1, int from1, int to1, int[] arr2, int from2){
        for (int i=0; i<=to1-from1;i++){
            if(arr1[from1+i]!=arr2[from2+i]){
                return false;
            }
        }
        return true;
    }
    public static DataStructures.Lists.DoublyLinkedList divisors(int n){
        DataStructures.Lists.DoublyLinkedList smalldivs = new DataStructures.Lists.DoublyLinkedList();
        DataStructures.Lists.DoublyLinkedList bigdivs = new DataStructures.Lists.DoublyLinkedList() {
        };
        smalldivs.insertTail(1);
        for (int i=2; i<=sqrt(n); i++)
        {
            if (n%i == 0)
            {
                if (n/i == i)
                    smalldivs.insertTail(i);

                else // Otherwise print both
                    smalldivs.insertTail(i);
                    bigdivs.insertHead(n/i);
            }
        }
        smalldivs.union(bigdivs);
        return smalldivs;
    }

    public static void fperiod(int[] arr, int n) {
        DataStructures.Lists.DoublyLinkedList divs=divisors(n);
        //no getter
        for(int i : divisors(n)){
            int ntimes=(n/i)-1;
            boolean isperiod=true;
            for (int j=ntimes; j>=1; j--){
                if(!isequal(arr, 0, i-1, arr, i*j)){
                    isperiod=false;
                }
            }
            if (isperiod){
                System.out.println(i);
                return;
            }
        }
        System.out.println(n);
        return;

}
    public static void main(String[] arg){
        int[] arr1={2, 5, 3, 4, 2, 5, 3, 4};
        int[] arr2={2, 5, 3, 2, 5, 3, 2, 5};
        int[] arr3={1, 1, 1, 1, 1, 1, 1, 1};
        int[] arr4={1, 2, 3, 1, 2, 3, 1, 2};
        int[] arr5={1, 2, 1, 2, 1, 2, 1, 2};
        int[] arr6={1, 1, 1, 1, 1, 1, 0};
        int[] arr7={0, 2, 2, 2, 2, 2};
        int[] arr8={1};
        int[] arr9={1,1,1};
        //true
        //System.out.println(isequal(arr1, 0, 3, arr1, 0));
        //System.out.println(isequal(arr1, 0, 3, arr1, 4));
        //System.out.println(isequal(arr1, 0, 7, arr1, 0));
        ////false
        //System.out.println(isequal(arr1, 0, 2, arr1, 2));
        //System.out.println(isequal(arr1, 0, 2, arr1, 2));
        //System.out.println(isequal(arr1, 3, 5, arr1, 4));
        fperiod(arr1, arr1.length); //4
        fperiod(arr2, arr2.length); //8
        fperiod(arr3, arr3.length); //4
        fperiod(arr4, arr4.length); //8
        fperiod(arr5, arr5.length); //4
        fperiod(arr6, arr6.length); //7
        fperiod(arr7, arr7.length); //6
        fperiod(arr8, arr8.length); //1
        fperiod(arr9, arr9.length); //1
    }
}
