private int min_cut_cost_imp(int i, int[] a, int b) {
   int cl = 0, cr = 0;
   if (a.length == 1) 
     return b;
   if (i > 0) {
      int bl = a[i];
      cl = Integer.MAX_VALUE;
      int[] al = Arrays.copyOfRange(a, 0, i);
      for (int j=0; j<ml.length; j++) {
         cl = Math.min(min_cut_cost_imp(al, bl, j), cl);
      }
   } else if (i < a.length - 1) {
      int br = b - a[i];
      cr = Integer.MAX_VALUE;
      int[] ar = Arrays.copyOfRange(a, i + 1, a.length);
      for (int j=0; j<ar.length; j++) {
         ar[j] = ar[j] - a[i];
      }
      for (int j=0; j<ar.length; j++) {
         cr = Math.min(min_cut_cost_imp(ar, br, j), cr);
      }
   }
   
   return b + cr + cl;
}

public int min_cut_cost(int[] a, int b) {
   int cost = b * a.length;
   for (int i=0; i<a.length; i++) {
      cost = Math.min(min_cut_cost_imp(a, b, i), cost);
   }
   return cost;
}
