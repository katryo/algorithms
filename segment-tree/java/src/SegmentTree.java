
// https://www.slideshare.net/iwiwi/ss-3578491

public class SegmentTree {
    private int[] data;
    private int n;

    public SegmentTree(int n) {
        this.n = n;
        data = new int[n * 2 - 1];

        for (int i = 0; i < n * 2 - 1; i++) {
            data[i] = Integer.MAX_VALUE;
        }
    }

    public void update(int i, int x) {
        i += n - 1;
        data[i] = x;

        while (i > 0) {
            i = (i - 1) / 2;
            data[i] = Math.min(data[i * 2 + 1], data[i * 2 + 2]);
        }
    }

    public int at(int i) {
        return data[n - 1 + i];
    }

    public int minInHalfOpenInterval(int a, int b, int node, int nodeLeftIdx, int nodeRightIdx) {
        if (a >= nodeRightIdx || b <= nodeLeftIdx) return Integer.MAX_VALUE;
        if (a <= nodeLeftIdx && b >= nodeRightIdx) return data[node];
        else {
            int vl = minInHalfOpenInterval(a, b, node * 2 + 1, nodeLeftIdx, (nodeLeftIdx + nodeRightIdx) / 2);
            int vr = minInHalfOpenInterval(a, b, node * 2+ 2, (nodeLeftIdx + nodeRightIdx) / 2, nodeLeftIdx);
            return Math.min(vl, vr);
        }
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
