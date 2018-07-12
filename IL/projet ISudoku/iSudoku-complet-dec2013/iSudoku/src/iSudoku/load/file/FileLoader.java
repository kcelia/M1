package iSudoku.load.file;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import iSudoku.factory.GrilleFactory;
import iSudoku.itf.IGrille;
import iSudoku.itf.IGrilleLoader;

public class FileLoader implements IGrilleLoader {

	@Override
	public IGrille loadGrille(String path) throws IOException {
		IGrille grille = GrilleFactory.createNewEmptyGrille();

		InputStream in = new BufferedInputStream(new FileInputStream(path));

		for (int y = 0; y < 9; y++) {
			for (int x = 0; x < 9; x++) {
				int read = in.read();
				if (Character.isWhitespace(read)) {
					x--;
					continue;
				}
				int val = read - '0';
				grille.setCellValue(y, x, val);
				if (val != 0)
					grille.setFixed(y, x, true);
			}
		}
		in.close();
		return grille;
	}

}
