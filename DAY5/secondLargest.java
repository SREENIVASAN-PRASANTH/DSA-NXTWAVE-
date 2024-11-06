import java.util.Arrays;

public class secondLargest {
    static int getSecondLargest(int arr[]){
        int arrLen = arr.length;

        Arrays.sort(arr);
        for(int i = arrLen-2; i >=0; i--){
            if(arr[i] != arr[arrLen - 1]){
                return arr[i];
            }
        }
        return -1;
    }

    public static void main(String args[]){
        int arr[] = {1,2,3,4,55,66,66,77};
        int secondLargest = getSecondLargest(arr);
        System.out.println(secondLargest);;
    }
}
