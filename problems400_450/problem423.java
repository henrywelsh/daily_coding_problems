public class problem423 {


    public int[][] findTransitiveClosure(int[][] graph) {
        int dim = graph.length;
        int[][] closure = new int[dim][dim];

        //Find all direct connections
        for (int i = 0; i < dim; i++) {
            for (int k = 0; k < graph[i].length; k++) {
                closure[i][graph[i][k]] = 1;
            }
        }

        // Find all connections through intermediary node k
        for (int k = 0; k < dim; k++) {
            for (int i = 0; i < dim; i++) {
                for (int j = 0; j < dim; j++) {
                    closure[i][j] = closure[i][j] | (closure[i][k] & closure[k][j]);
                }
            }
        }
        return closure;
    }

    
}
