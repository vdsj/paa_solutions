public int findMinCutCost(int[] m, int n) {
   int cost = n * m.length;
   for (int i=0; i<m.length; i++) {
      cost = Math.min(findMinCutCostImpl(m, n, i), cost);
   }
   return cost;
}

private int findMinCutCostImpl(int[] m, int n, int i) {
   if (m.length == 1) 
     return n;
   int cl = 0, cr = 0;
   if (i > 0) {
      cl = Integer.MAX_VALUE;
      int[] ml = Arrays.copyOfRange(m, 0, i);
      int nl = m[i];
      for (int j=0; j<ml.length; j++) {
         cl = Math.min(findMinCutCostImpl(ml, nl, j), cl);
      }
   }
   if (i < m.length - 1) {
      cr = Integer.MAX_VALUE;
      int[] mr = Arrays.copyOfRange(m, i + 1, m.length);
      int nr = n - m[i];
      for (int j=0; j<mr.length; j++) {
         mr[j] = mr[j] - m[i];
      }
      for (int j=0; j<mr.length; j++) {
         cr = Math.min(findMinCutCostImpl(mr, nr, j), cr);
      }
   }
   return n + cl + cr;
}
