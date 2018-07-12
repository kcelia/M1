package iSudoku.contraintes;

import java.awt.Point;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

import iSudoku.itf.IGrille;
import iSudoku.itf.IGrilleContrainte;

public class GrilleContrainte extends GrilleDecorator implements
		IGrilleContrainte {

	private List<Contrainte> contraintes;

	public GrilleContrainte(IGrille grille) {
		super(grille);
		contraintes = new ArrayList<Contrainte>();

		for (int l = 0; l < 9; l++) {
			List<Point> ligne = new ArrayList<Point>();
			for (int c = 0; c < 9; c++) {
				ligne.add(new Point(l, c));
			}
			contraintes.add(new Contrainte(ligne));
		}
		for (int c = 0; c < 9; c++) {
			List<Point> col = new ArrayList<Point>();
			for (int l = 0; l < 9; l++) {
				col.add(new Point(l, c));
			}
			contraintes.add(new Contrainte(col));
		}
		for (int sl = 0; sl < 3; sl++) {
			for (int sc = 0; sc < 3; sc++) {
				List<Point> sub = new ArrayList<Point>();
				for (int dl = 0; dl < 3; dl++) {
					for (int dc = 0; dc < 3; dc++) {
						sub.add(new Point(sl * 3 + dl, sc * 3 + dc));
					} // dc
				} // dl
				contraintes.add(new Contrainte(sub));
			} // sc
		} // sl

	}

	@Override
	public boolean computeGrilleIsValid() {
		for (Contrainte c : contraintes) {
			if (!c.isValid(this)) {
				return false;
			}
		}
		return true;
	}

	@Override
	public boolean isCaseValid(int lig, int col) {
		if (isFixed(lig, col)) {
			return true;
		}
		int val = getCellValue(lig, col);
		if (val != 0)
			return getSuggestions(lig, col).contains(val);
		else 
			return ! getSuggestions(lig, col).isEmpty();
	}

	@Override
	public Set<Integer> getSuggestions(int lig, int col) {
		Set<Integer> remain = new TreeSet<Integer>();
		for (int i = 1; i <= 9; i++)
			remain.add(i);
		for (Contrainte c : getContraintesCase(lig, col)) {
			for (Point p : c.getCases()) {
				int val = getCellValue(p.x, p.y);

				if (val != 0 && (p.x != lig || p.y != col)) {
					remain.remove(val);
				}
			}
		}
		return remain;
	}

	private List<Contrainte> getContraintesCase(int lig, int col) {
		List<Contrainte> list = new ArrayList<Contrainte>();
		// ligne
		list.add(contraintes.get(lig));
		// colonne
		list.add(contraintes.get(9 + col));
		// bloc
		list.add(contraintes.get(18 + (lig / 3) * 3 + (col / 3)));

		return list;
	}

	@Override
	public boolean estPleine() {
		for (int c = 0; c < 9; c++) {
			for (int l = 0; l < 9; l++) {
				if (getCellValue(l, c)==0)
					return false;
			}
		}
		return true;
	}
}
