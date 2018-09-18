import java.util.*;

public class Main {
    private final int INFINITY = 6000 * 99 + 1;
    public int dijkstra(int[][] times, int N, int K) {
        HashMap<Integer, Node> nodes = new HashMap<Integer, Node>();
        Node start = new Node(K, 0);

        nodes.put(K, start);

        for (int i = 1; i < N+1; i++) {
            if (i != K) {
                Node n = new Node(i, INFINITY);
                nodes.put(i, n);
            }
        }

        for (int[] time : times) {
            int from = time[0];
            int to = time[1];
            int cost = time[2];
            Edge e = new Edge(cost, from, to);
            Node n = nodes.get(from);
            n.addEdge(e);
        }

        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        for (Edge e : start.edges) {
            Node n = nodes.get(e.to);
            if (n.cost > e.cost) {
                n.cost = e.cost;
            }
            pq.add(n);
        }

        HashSet<Integer> exploredNums = new HashSet<Integer>();
        exploredNums.add(K);

        int ans = 0;
        while (!pq.isEmpty()) {
            Node minNode = pq.poll();
            if (exploredNums.contains(minNode.number)) {
                continue;
            }
            exploredNums.add(minNode.number);
            ans = Math.max(ans, minNode.cost);
            for (Edge e: minNode.edges) {
                if (exploredNums.contains(e.to)) {
                    continue;
                }
                int candidateCost = e.cost + minNode.cost;
                Node changeableNode = nodes.get(e.to);
                if (changeableNode.cost > candidateCost) {
                    changeableNode.cost = candidateCost;
                }
                pq.add(changeableNode);
            }
        }
        if (exploredNums.size() != N) {
            return -1;
        }
        return ans;
    }

    class Node implements Comparable<Node> {
        private int number;
        private int cost;
        private HashSet<Edge> edges;

        public Node(int number, int cost) {
            this.number = number;
            this.cost = cost;
            edges = new HashSet<Edge>();
        }

        public void addEdge(Edge e) {
            edges.add(e);
        }

        public int compareTo(Node another) {
            return cost - another.cost;
        }

    }

    class Edge {
        private int cost;
        private int from;
        private int to;
        public Edge(int cost, int from, int to) {
            this.cost = cost;
            this.from = from;
            this.to = to;
        }
    }

    public static void main(String[] args) {
        Main m = new Main();
        int[][] times = new int[20][3];
        times[0] = new int[]{4, 2, 76};
        times[1] = new int[]{1,3,79};
        times[2] = new int[]{3,1,81};
        times[3] = new int[]{4,3,30};
        times[4] = new int[]{2,1,47};
        times[5] = new int[]{1,5,61};
        times[6] = new int[]{1,4,99};
        times[7] = new int[]{3,4,68};
        times[8] = new int[]{3,5,46};
        times[9] = new int[]{4,1,6};
        times[10] = new int[]{5,4,7};
        times[11] = new int[]{5,3,44};
        times[12] = new int[]{4,5,19};
        times[13] = new int[]{2,3,13};
        times[14] = new int[]{3,2,18};
        times[15] = new int[]{1,2,0};
        times[16] = new int[]{5,1,25};
        times[17] = new int[]{2,5,58};
        times[18] = new int[]{2,4,77};
        times[19] = new int[]{5,2,74};
        int result = m.dijkstra(times, 5, 3);
        System.out.println(result);
    }
}
