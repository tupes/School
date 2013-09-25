public class Tilecoder {
	final static int numOfTilings = 8;
	final static int length = 11;
	final static int numTiles = length * length;
	final static double offset = -1.0 / numOfTilings;
	final static int max_x = 6;

	public static void tilecode(double x1, double x2, int[] tilecodeIndices) {
		double base = 0.0;
		int tileNum; int tileNumX1; int tileNumX2;
		double standardX1 = (x1 / max_x) * (length - 1);
		double standardX2 = (x2 / max_x) * (length - 1);
		
		// compute the tile numbers
		for (int i = 0; i < numOfTilings; i++) {
			
			// find coordinates of activated tile in the tiling space
			tileNumX1 = (int) Math.floor(standardX1 - base);
			tileNumX2 = ((int) Math.floor(standardX2 - base)) * length;
			tileNum = tileNumX1 + tileNumX2;
			tilecodeIndices[i] = tileNum + (i * numTiles);
			// compute offset for next tiling
			base += offset;
		}
	}

	public static void main(String[] args) {
		int[] tilecodeIndices = new int[numOfTilings];

		printTileCoderIndices(0.1, 0.1, tilecodeIndices);
		printTileCoderIndices(4.0, 2.0, tilecodeIndices);
		printTileCoderIndices(5.99, 5.99, tilecodeIndices);
		printTileCoderIndices(4.0, 2.1, tilecodeIndices);
	}

	private static void printTileCoderIndices(double x1, double x2, int[] tilecodeIndices) {
		tilecode(x1, x2, tilecodeIndices);
		System.out.print("Tile indices for input (" + x1 + ", " + x2 + ") are: ");
		for (int i = 0; i < numOfTilings; i++)
			System.out.print(tilecodeIndices[i] + " ");
		System.out.println();
	}
}

