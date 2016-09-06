import java.util.Arrays;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.HashSet;
import java.util.Random;
import java.util.Collections;
import java.lang.StringBuilder;

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

	public static void mode1(int depth){
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
		System.out.println("Count: " + count);
	}

	public static void mode2(int depth){
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
		System.out.println("Count: " + count);
	}

	public static void mode3(int depth){
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
		System.out.println("Count: " + count);
	}
}
