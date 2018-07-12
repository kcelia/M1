package iSudoku.contraintes;

import iSudoku.itf.IGrille;

import java.awt.Point;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Contrainte {

	private List<Point> cases;

	public Contrainte(List<Point> cells) {
		this.cases = cells;
	}

	boolean isValid(IGrille g) {
		Set<Integer> seen = new TreeSet<Integer>();
		for (Point p : cases) {
			int val = g.getCellValue(p.x, p.y);
			if (val != 0) {
				if (!seen.add(val)) {
					return false;
				}
			}
		}
		return true;
	}

	public List<Point> getCases() {
		return cases;
	}
}
