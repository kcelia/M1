package iSudoku.tests;

import java.io.IOException;

import iSudoku.factory.GrilleFactory;
import iSudoku.ihm.SudokuIHM;
import iSudoku.itf.IGrille;

public class TestGrille {

	public static void main(String[] args) {

		IGrille vide = GrilleFactory.createNewEmptyGrille();
		System.out.println(vide);
		try {
			IGrille g1 = GrilleFactory.createFileLoader().loadGrille("examples/grille1.sdk");
			System.out.println(g1);

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		new SudokuIHM();
	}
}
