import java.util.*;

public class Problem152 { 
	public static void main(String[] args) { 

		if (args.length == 0) { 
 			System.out.println(usageError());
        	System.exit(0);
		}

		int size = 0;

		try { 
			size = Integer.parseInt(args[0]);
		} 
		catch (Exception ex) { 
			System.out.println(usageError());
			System.exit(0);
		}

		Set set = new Set(size);

		System.out.print("\n");
		System.out.println(size + " x " + size + " Lattice"); 

		System.out.println("Corners are:");

		System.out.println(set); 
		System.out.print("\n");

		System.out.println("Press any key to continue..."); 

		try { 
			System.in.read();
		} 
		catch(Exception ex) { 
			System.out.println("I guess something went wrong!");
			ex.printStackTrace(System.out);
		}


		List<List<Node>> paths = set.findPathsToLastNode();
	}

	public static String usageError() { 
		StringBuilder sb = new StringBuilder(); 

		sb.append("Proper Usage is: java Problem15 size\n"); 
 		sb.append("Ex: java Problem15 20\n");

 		return sb.toString();
	}
}

class Node { 

	public int x; 
	public int y;
	public int id; 

	public Node down; 
	public Node right;

	Node(int x, int y, int id) { 
		this.x = x; 
		this.y = y;
		this.id = id;
	}

	@Override 
	public String toString() { 
		StringBuilder sb = new StringBuilder(); 

		sb.append(id);

		return sb.toString();
	}
}

class Set { 

	public List<Node> nodes; 
	public int width; 
	public int height;

	Set(int size) { 
		this.width = size; 
		this.height = size;

		nodes = new ArrayList<Node>();

		// populate the map, counting corners
		for (int i = 0; i <= width; i++) { 
			for (int j = 0; j <= height; j++) { 
				nodes.add(new Node(i, j, ((i * (width + 1)) + j))); 
			}
		}

		// create connections to right 
		for (int i = 0; i < nodes.size(); i++) { 

			// create connection to right neighbor
			if(((nodes.get(i).id + 1) % (width + 1)) != 0) { 
				nodes.get(i).right = nodes.get(i + 1);
			}

			// create connection with neighbor below
			int first_last_row = ((width + 1) * (width + 1)) - (width + 1);
	
			if (nodes.get(i).id < first_last_row) {
				nodes.get(i).down = nodes.get(i + width + 1);
			}
		}
	}

	public List<List<Node>> findPathsToLastNode() { 
		List<List<Node>> paths = new ArrayList<List<Node>>();

		List<Node> path = new ArrayList<Node>(); 

		traverseTree(paths, path, nodes.get(0));

		System.out.print("\n");
		System.out.println(paths.size() + " paths found"); 

		return paths; 
	}

	// where the magic happens
	// this is a recursive method that will traverse the tree until it finds the bottom right corner 
	private void  traverseTree(List<List<Node>> paths, List<Node> path, Node node) {

		path.add(node);

		if (node.right != null) { 
			traverseTree(paths, path, node.right); 
		}

		if (node.down != null) { 
			traverseTree(paths, path, node.down); 
		}

		if (node.right == null && node.down == null) { 
			// got to the corner 
			paths.add(new ArrayList<Node>(path));

			System.out.print("Path Found: ");

			for (int i = 0; i < path.size(); i++) { 
				System.out.print(path.get(i).id);

				if (i != path.size() - 1) 
					System.out.print("=>"); 

			}

			System.out.println(); 
		}

		path.remove(path.size() - 1); 	
	}

	@Override 
	public String toString() { 
		StringBuilder sb = new StringBuilder(); 

		for (Node node : nodes) { 
			if (node.id % (width + 1) == 0) { 
				sb.append("\n");
			}

			sb.append("|" + node + "|"); 
		}

		return sb.toString();
	}
}