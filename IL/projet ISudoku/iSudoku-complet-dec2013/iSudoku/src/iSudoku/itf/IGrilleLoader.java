package iSudoku.itf;

import java.io.IOException;

public interface IGrilleLoader {

	/**
	 * Load a Grille from a given source.
	 * 
	 * @param url
	 *            a description of the source, of the form "protocol://path".
	 * @return a newly loaded IGrille
	 * @throws IOException
	 *             if url is invalid
	 */
	public IGrille loadGrille(String url) throws IOException;
}
