package iSudoku.grille;

import iSudoku.itf.IGrille;

public class Grille implements IGrille {

	private final int[][] values = new int[9][9];
	private final boolean[][] fixed = new boolean[9][9];

	@Override
	public void setCellValue(int x, int y, int value) {
		testVal(value);
		values[x][y] = value;
	}

	private void testVal(int value) {
		if (value < 0 || value > 9) {
			throw new ArrayIndexOutOfBoundsException(
					"Value in cells shouldbe in 0..9");
		}
	}

	@Override
	public int getCellValue(int x, int y) {
		return values[x][y];
	}

	@Override
	public boolean isFixed(int x, int y) {
		return fixed[x][y];
	}

	@Override
	public void setFixed(int x, int y, boolean isFixed) {
		fixed[x][y] = isFixed;
	}

	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder(1024);

		for (int y = 0; y < 9; y++) {
			for (int x = 0; x < 9; x++) {
				int val = getCellValue(y, x);
				if (val == 0) {
					sb.append(" . ");
				} else {
					sb.append(" " + val + " ");
				}
				if (x == 2 || x == 5) {
					sb.append("|");
				}
				if (x == 8) {
					sb.append("\n");
				}
			}
			if (y == 2 || y == 5) {
				sb.append("-----------------------------\n");
			}
		}

		return sb.toString();
	}
}
