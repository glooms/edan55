import java.util.Arrays;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.HashSet;
import java.util.Random;
import java.util.Collections;
import java.lang.StringBuilder;

import java.math.MathContext;
import java.math.BigDecimal;

public class Tree {

	private final int N;
	private boolean[] nodes;
	private HashSet<Integer> unmarked;

	public Tree(int depth) {
		N = (1 << depth) - 1;
		nodes = new boolean[N + 1];
		unmarked = new HashSet<Integer>();
		for(int i = 1; i <= N; i++)
			unmarked.add(i);
	}

	public boolean mark(int index) {
		if (nodes[index])
			return false;
		markDown(index);
		markUp(index / 2);
		return true;
	}


	private void markUp(int index) {
		if (index == 0)
			return;
		int c1, c2;
		c1 = index * 2;
		c2 = c1 + 1;
		if (nodes[index]) {
			markDown(index);
		} else if (nodes[c1] && nodes[c2]) {
			markNode(index);
			markUp(index / 2);
		}
	}

	private void markDown(int index) {
		markNode(index);

		int c1, c2;
		c1 = index * 2;
		c2 = c1 + 1;
		if (c2 <= N) {
			if (nodes[c1])
				markDown(c2);
			else if (nodes[c2])
				markDown(c1);
		}
	}

	private void markNode(int index) {
		if (!nodes[index]) {
			nodes[index] = true;
			unmarked.remove(index);
		}
	}

	public String toString() {
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			sb.append(nodes[i] ? '1' : '0');
		}
		return sb.toString();
	}

	public int size() {
		return N;
	}

	public boolean halt() {
		return unmarked.isEmpty();
	}


	public static void main(String[] args) {
        if (args.length == 3) {
            if (args[0].equals("stat")) {
                int m = Integer.parseInt(args[1]);
                int n = Integer.parseInt(args[2]);
                statistics(m, n);
            }
        }
		if (args.length != 2)
			return;
		int mode = Integer.parseInt(args[0]);
		int depth = Integer.parseInt(args[1]);
		switch (mode) {
			case 1: mode1(depth);
				break;
			case 2: mode2(depth);
				break;
			case 3: mode3(depth);
				break;
			default:
				return;
		}
	}

    public static void statistics(int m, int n) {
        double[][] dev1, dev2, dev3;
        dev1 = new double[m][2];
        dev2 = new double[m][2];
        dev3 = new double[m][2];
        double[] a1, a2, a3;
        for (int i = 2; i <= m; i++) {
            a1 = new double[n];
            a2 = new double[n];
            a3 = new double[n];
            for (int j = 0; j < n; j++) {
                a1[j] = mode1(i);
                a2[j] = mode2(i);
                a3[j] = mode3(i);
            }
            dev1[i - 2] = standardDev(a1);
            dev2[i - 2] = standardDev(a2);
            dev3[i - 2] = standardDev(a3);
        }
        int N;
        for (int j = 2; j <= m; j++) {
            N = (int) Math.pow(2, j) - 1;
            System.out.print(N + " & ");
            System.out.print(dev1[j - 2][0] + " \\pm " + dev1[j - 2][1] + " & ");
            System.out.print(dev2[j - 2][0] + " \\pm " + dev2[j - 2][1] + " & ");
            System.out.println(dev3[j - 2][0] + " \\pm " + dev3[j - 2][1] + " \\\\");
        }

        /*
        System.out.println("R1");
        for (int j = 2; j <= m; j++)
                System.out.println(j + ":  " + dev1[j - 2][0] + "  +/-  " + dev1[j - 2][1]);
        System.out.println("R2");
        for (int j = 2; j <= m; j++)
                System.out.println(j + ":  " + dev2[j - 2][0] + "  +/-  " + dev2[j - 2][1]);
        System.out.println("R3");
        for (int j = 2; j <= m; j++)
                System.out.println(j + ":  " + dev3[j - 2][0] + "  +/-  " + dev3[j - 2][1]); */
    }

    public static double[] standardDev(double[] a) {
        double mean, stdDev;
        int sum = 0;
        for (int i = 0; i < a.length; i++)
            sum += a[0];
        mean = (double) sum / a.length;
        double temp = 0;
        for (int i = 0; i < a.length; i++)
            temp += Math.pow(a[i] - mean, 2);
        temp /= (a.length - 1);
        stdDev = round(Math.sqrt(temp), 1);
        if (stdDev != 0) {
                int digits = (int) Math.log10(mean / stdDev) + 1;
                mean = round(mean, digits);
        }
        double[] d = {mean, stdDev};
        return d;
    }

    private static double round(double d, int digits) {
        BigDecimal bd = new BigDecimal(d);
        bd = bd.round(new MathContext(digits));
        return bd.doubleValue();
    }

	public static double mode1(int depth){
		Tree t = new Tree(depth);
		Random r = new Random();
		int count = 0;
		while (!t.halt()) {
			count++;
			int index = r.nextInt(t.size()) + 1;
			t.mark(index);
//			System.out.format("%02d: ", index);
//			System.out.println(t.toString());
		}
//		System.out.println("Count: " + count);
        return (double) count;
	}

	public static double mode2(int depth){
		Tree t = new Tree(depth);
		ArrayList<Integer> order = new ArrayList<Integer>();
		for (int i = 1; i <= t.size(); i++)
			order.add(i);
		Collections.shuffle(order);
		int count = 0;
		while (!t.halt()) {
			count++;
			int index = order.remove(order.size() - 1);
			t.mark(index);
//			System.out.format("%02d: ", index);
//			System.out.println(t.toString());
		}
//		System.out.println("Count: " + count);
        return (double) count;
	}

	public static double mode3(int depth){
		Tree t = new Tree(depth);
		ArrayList<Integer> order = new ArrayList<Integer>();
		for (int i = 1; i <= t.size(); i++)
			order.add(i);
		Collections.shuffle(order);
		int count = 0;
		while (!t.halt()) {
			int index = order.remove(order.size() - 1);
			if (t.mark(index))
				count++;
	//			System.out.format("%02d: ", index);
	//			System.out.println(t.toString());
		}
	//	System.out.println("Count: " + count);
        return (double) count;
	}
}
