package iSudoku.itf;

public interface IHelpLevel {

	void doShowInvalid(boolean set);

	boolean shouldShowInvalid();

	boolean shouldShowInvalidCells();

	void doShowInvalidCells(boolean set);

	void doShowSingleSolution(boolean b);

	void doShowSuggestions(boolean b);

	boolean shouldShowSuggestions();

	boolean shouldShowSingleSolution();

}
