package iSudoku.load.image;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import externe.recoImage.IReconnaissanceImage;

import iSudoku.factory.GrilleFactory;
import iSudoku.itf.IGrille;
import iSudoku.itf.IGrilleLoader;

public class ImageLoader implements IGrilleLoader {

	IReconnaissanceImage reco ;
	
	public ImageLoader(IReconnaissanceImage reco) {
		this.reco = reco;
	}


	@Override
	public IGrille loadGrille(String url) throws IOException {
		BufferedImage img = null;
		img = ImageIO.read(new File(url));
		
		int [] [] mat =  reco.readImage(img);
		
		IGrille grille = GrilleFactory.createNewEmptyGrille();
		for (int l = 0 ; l < 9 ; l++) {
			for (int c=0; c < 9 ; c++) {
				grille.setCellValue(l, c, mat[l][c]);
				if (mat[l][c]!=0) 
					grille.setFixed(l, c, true);
			}
		}
		return grille;
	}

}
