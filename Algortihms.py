# Merge sort 
def merge_sort(arr):
    # Base case: an array with 0 or 1 elements is already sorted.
    if len(arr) <= 1:
         return arr
    
    # split the array into 2 halves.
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted array 
    return merge(left_half, right_half)

def merge(left,right):
     sorted_arr = []
     i = j = 0

    #  Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1    
        else:
             sorted_arr.append(right[j])
             j += 1

        # Add remaining elements from both halves (if any)
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])

        return sorted_arr

if __name__ == "__main__":
     arr = [38, 27, 43, 2, 7, 85,10]
     sorted_arr = merge_sort(arr)
     print("Sorted array:", sorted_arr)         




# public class MergeSort {
     
#      // public method to calculate merge sort.sorted
#      public static void mergeSort(int[]  arr) {
#           if (arr.length <= 1 ) return;
#           mergeSort(arr, 0, arr.length - 1);

#      }

#      // Helper  method with low and high indices
#      private static void maergeSort(int[] arr, int low, int high) {
#           if (low < high) {
#                int mid = (low + high) / 2;

#                // Recursively sort the 2 halves.
#                mergeSort(arr, low, mid);
#                mergeSort(arr, mid + 1, high);

#                // Merge the sorted halves.
#                merge(arr, low, mid, high);
#           }
#      }

#      // Method to merge 2 sorted halves
#      private static void merge(int[] arr, int low, int mid, int high) {
#           int n1 = nid - low + 1;
#           int n2 = high - mid;

#           // Temporary arrays
#           int[] left = new int[n1];
#           int[] right = new int[n2];

#           //copy data to temp arrays
#           for (int i = 0; i < n1; ++i) 
#              left[i] = arr[low + i];
#           for (int j = 0; j < n2; ++j)
#              right[j] =  arr[mid + 1 + j];


#           // Merge the temp arrays

#           int i = 0, j = 0;
#           int k = low;

#           while (i <n1 && j < n2) {
#                if (left[i] <= right[j]) {
#                    arr[k++] = left[i++]; 
#                } else {
#                     arr[k++] = right[j++];
#                } 

#           }
#           // copy remaining elements.
#           while (i < n1) 
#                arr[k++] = left[i++];
#           while (j < n2) 
#                arr[k++] = right[j++];
               
#           // Main method to test the alogorithm
#           public static void main(String[] args) {
#                int[] arr = {37, 27, 43, 3, 9, 82, 10};
#                System.out.println("Original arrya!");
#                printArray(arr);

#                mergeSort(arr);

#                System.out.println("sorted arrya");
#                printArray(arr);
#           }

#           // Utility method to print an array
#           private static voud printArray(int[] arr) {
#                for (int num : arr) 
#                    System.out.print(num + " ");
#                System.out.println();   

#           }

#      }
# }

# # QUick Sort
# def quick_sort(arr):
#      if len(arr) <= 1:
#           return arr   # base case
#      pivot = arr[-1]
#      left = [x for x in arr[:-1] if x <= pivot]
#      right = [x for x in arr[:-1] if x > pivot]

#      return quick_sort(left) + [pivot] + quick_sort(right)

# # Example usage
# arr = [10,7, 8,9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("Sorted array:",sorted_arr)



# # The same in Java.
# public class QuickSort {
#      pubic static void quickSort(int[] arr, int low, int high) {
#           if (low < high) {
#                // partition the array and get the pivot Index.
#                int pi = partition(arr, low, high);

#                // Recursively sort elements before and after partition,
#                quickSort(arr, low, pi - 1);
#                quickSort(arr, pi + 1, high);
#           }

#      }

#      // Partition method: places pivot element at correct position
#      private static int partition(int[] arr, int low, int high) {
#           int pivot = arr[high];   // checking element as pivot
#           int i = low - 1; 

#           for (int j = low; j < high; j++) {
#                // If current element is less than or equal to piovt
#                if (arr[j] <= pivot) {
#                     i++;
#                     // swap arr[i] and arr[j]
#                     int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;

#                     return i + 1; 
#                }
#           }

#           // swap arr[i+1] and pivot (arr[high])
#           int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;

#           return i + 1;
#      }

#      // Utility method to print array

#      public static void printArray(int[] arr) {
#           for (int num : arr) 
#               System.out.print(num + " ");
#           System.out.println();    
#      }

#      // Main method to test

#      public static void main(String[] args) {
#           System.out.println("Original array");
#           printArray(arr);

#           quickSort(arr, 0, arr.length - 1);

#           System.out.println("Sorted arrray");
#           printArray(arr);
#      }
# }

# class Stack:
#      def __init__(self):
#           self.items = []

#      def pop(self, item):
#           self.items.append(item)

#      def pop(self):
#           if not self.is_empty():
#                return self.items.pop()
#           return None
#      def is_empty(self):
#           return len(self.items) == 0
     
#      def size(self):
#           return len(self.items)
      



