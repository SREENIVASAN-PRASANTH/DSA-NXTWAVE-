package DAY7;
import java.util.Arrays;

public class moveZeroesToEnd {
    static int[] moveZeroEnd(int arr[]){
        int position = 0;
        for(int i : arr){
            if(i != 0){
                arr[position] = i;
                position++;
            }
        }

        for(int k = position;k < arr.length; k++){
            arr[k] = 0;
        }

        return arr;
    }

    public static void main(String args[]){
        int arr[] = {1,0,2,0,3,0,4,5,6};
        System.out.println(Arrays.toString(moveZeroEnd(arr)));
    }
}
