private int min_cut_cost_imp(int i, int[] m, int n) {
   int cl = 0, cr = 0;
   if (m.length == 1) 
     return n;
   if (i > 0) {
      cl = Integer.MAX_VALUE;
      int[] ml = Arrays.copyOfRange(m, 0, i);
      int nl = m[i];
      for (int j=0; j<ml.length; j++) {
         cl = Math.min(min_cut_cost_imp(ml, nl, j), cl);
      }
   } else if (i < m.length - 1) {
      cr = Integer.MAX_VALUE;
      int[] mr = Arrays.copyOfRange(m, i + 1, m.length);
      int nr = n - m[i];
      for (int j=0; j<mr.length; j++) {
         mr[j] = mr[j] - m[i];
      }
      for (int j=0; j<mr.length; j++) {
         cr = Math.min(min_cut_cost_imp(mr, nr, j), cr);
      }
   }
   return n + cl + cr;
}

public int min_cut_cost(int[] m, int n) {
   int cost = n * m.length;
   for (int i=0; i<m.length; i++) {
      cost = Math.min(min_cut_cost_imp(m, n, i), cost);
   }
   return cost;
}
