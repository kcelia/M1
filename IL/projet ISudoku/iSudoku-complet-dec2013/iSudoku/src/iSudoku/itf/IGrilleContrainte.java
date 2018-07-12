package iSudoku.itf;

import java.util.Collection;

public interface IGrilleContrainte extends IGrille {

	boolean computeGrilleIsValid();

	Collection<Integer> getSuggestions(int lig, int col);

	boolean isCaseValid(int lig, int col);

	boolean estPleine();
}
