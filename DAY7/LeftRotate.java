package DAY7;
import java.util.Arrays;

public class LeftRotate {
    static int[] rotateArray(int arr[]) {
        int firstHalf[] = Arrays.copyOfRange(arr,1,arr.length);
        int firstElement = arr[0];
        for(int i = 0;i < arr.length;i++){
            if(i != arr.length - 1){
                arr[i] = firstHalf[i];
            }
            else{
                arr[i] = firstElement;
            }
        }
        return arr;

        
    }
    public static void main(String args[]){
        int arr[] = {1,2,3,4,5};

        // int firstElement = arr[0];

        // for(int i = 1;i < arr.length;i ++){
        //     arr[i - 1] = arr[i];
        // }
        // arr[arr.length - 1] = firstElement;

        // for(int j = 0;j < arr.length;j++){
        //     System.out.println(arr[j]);
        // }

        System.out.println(Arrays.toString(rotateArray(arr)));
        

    }
}
