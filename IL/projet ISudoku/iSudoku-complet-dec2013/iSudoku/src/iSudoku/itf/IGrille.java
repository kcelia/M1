package iSudoku.itf;

/**
 * 
 * @author Yann
 * 
 */
public interface IGrille {

	/**
	 * Set the value of a cell. First line has index 0. Leftmost column is
	 * column 0. (0,0) is top left. value 0 means cell is empty.
	 * 
	 * @param line
	 *            in range 0..8
	 * @param col
	 *            in range 0..8
	 * @param value
	 *            in range 0..9
	 * @throws ArrayIndexOutOfBoundsException
	 *             if line, col or value are out of range
	 */
	void setCellValue(int line, int col, int value);

	/**
	 * Get the value of a cell. First line has index 0. Leftmost column is
	 * column 0. (0,0) is top left. value 0 means cell is empty.
	 * 
	 * @param line
	 *            in range 0..8
	 * @param col
	 *            in range 0..8
	 * @return value of cell (x,y) in range 0..9
	 * @throws ArrayIndexOutOfBoundsException
	 *             if line or col are out of range
	 */
	int getCellValue(int line, int col);

	/**
	 * Determine if the cell is an initial cell
	 * 
	 * @param line
	 *            in range 0..8
	 * @param col
	 *            in range 0..8
	 * @return true if cell at position (line,col) is an initial cell
	 * @throws ArrayIndexOutOfBoundsException
	 *             if line or col are out of range
	 */
	boolean isFixed(int line, int col);

	/**
	 * Set a cell to be an initial value.
	 * 
	 * @param line
	 *            in range 0..8
	 * @param col
	 *            in range 0..8
	 * @param isFixed
	 *            to set or unset
	 * @throws ArrayIndexOutOfBoundsException
	 *             if line or col are out of range
	 */
	void setFixed(int line, int col, boolean isFixed);

}
