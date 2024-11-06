package DAY7;
import java.util.Arrays;

public class rotatePlacesK {
    static int[] rotate(int arr[], int k){
        k = k % 5;
        for(int i = 1; i <= k;i++){
            int firstElement = arr[0];
            for(int j = 1;j < arr.length;j ++){
                arr[j - 1] = arr[j];
            }
            arr[arr.length - 1] = firstElement;
        }

        return arr;
    }

    public static void main(String args[]){
        int k = 3;
        int arr[] = {1,2,3,4,5};
        arr = rotate(arr,k);
        System.out.println(Arrays.toString(arr));
    }
}
