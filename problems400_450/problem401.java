import java.lang.reflect.Array;

public class problem401 {
    

    public <T> T[] applyPermutation(Class<T> clazz, T[] orgArr, int[] permutation) throws Exception {
        if (orgArr.length != permutation.length) throw new Exception();
        T[] newArr = (T[]) Array.newInstance(clazz, orgArr.length);
        for (int i = 0; i < permutation.length; i++) {
            newArr[i] = orgArr[permutation[i]];
        }
        return newArr;
    }

    public <T> T[] applyPermutation2(Class<T> clazz, T[] orgArr, int[] permutation) throws Exception {
        if (orgArr.length != permutation.length) throw new Exception();
        for (int i = 0; i < permutation.length; i++) {
            while (i != permutation[i]) {
                int orgLoc = permutation[i];
                T orgVal = orgArr[i];
                int tarLoc = permutation[permutation[i]];
                T tarVal = orgArr[permutation[i]];
                permutation[tarLoc] = orgLoc;
                permutation[orgLoc] = tarLoc;
                orgArr[tarLoc] = orgVal;
                orgArr[orgLoc] = tarVal;
            }
        }
        return orgArr;
    }

}
