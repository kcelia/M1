package iSudoku.ihm;

import iSudoku.factory.GrilleFactory;
import iSudoku.itf.IGrilleLoader;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

import javax.swing.JFileChooser;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;

public class FileMenu extends JMenu {

	private final SudokuIHM parent;
	
	public FileMenu(SudokuIHM parent) {
		super("Load");

		this.parent=parent;
		JMenuItem loadFile = new JMenuItem("Load file");

		loadFile.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				loadFromFile();
			}
		});

		add(loadFile);
		
		JMenuItem loadImage = new JMenuItem("Load Image");

		loadImage.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				loadFromImage();
			}
		});
		
		add(loadImage);
	}

	protected void loadFromImage() {
		// / Code pris directement dans la doc de JFileChooser.
		// L'argument "./" permet de démarrer directement dans le
		// repertoire
		// courant
		// La version par défaut JFilechooser() démarre dans le $home.
		JFileChooser chooser = new JFileChooser(new File("./examples"));
		FileNameExtensionFilter filter = new FileNameExtensionFilter(
				"Image files", "png");
		chooser.setFileFilter(filter);
		chooser.setDialogTitle("Sélectionnez une photo d'un sudoku ");
		int returnVal = chooser.showOpenDialog(parent);
		String fileName;
		if (returnVal == JFileChooser.APPROVE_OPTION) {
			fileName = chooser.getSelectedFile().getPath();
		} else {
			// Un cancel, click sur la croix...
			return;
		}

		try {
			IGrilleLoader gl = getGrilleImageLoader();
			parent.setGrille(gl.loadGrille(fileName));
		} catch (IOException e) {
			JOptionPane.showInternalMessageDialog(
					parent.getContentPane(), e.getMessage(),
					"Error during import ", JOptionPane.ERROR_MESSAGE);
			e.printStackTrace();
		}
	}

	protected void loadFromFile() {
		// / Code pris directement dans la doc de JFileChooser.
		// L'argument "./" permet de démarrer directement dans le
		// repertoire
		// courant
		// La version par défaut JFilechooser() démarre dans le $home.
		JFileChooser chooser = new JFileChooser(new File("./examples"));
		FileNameExtensionFilter filter = new FileNameExtensionFilter(
				"Sudoku files", "sdk");
		chooser.setFileFilter(filter);
		chooser.setDialogTitle("Entrez un nom de fichier .sdk ");
		int returnVal = chooser.showOpenDialog(parent);
		String fileName;
		if (returnVal == JFileChooser.APPROVE_OPTION) {
			fileName = chooser.getSelectedFile().getPath();
		} else {
			// Un cancel, click sur la croix...
			return;
		}

		try {
			IGrilleLoader gl = getGrilleFileLoader();
			parent.setGrille(gl.loadGrille(fileName));
		} catch (IOException e) {
			JOptionPane.showInternalMessageDialog(
					parent.getContentPane(), e.getMessage(),
					"Error during import ", JOptionPane.ERROR_MESSAGE);
			e.printStackTrace();
		}
	}

	private IGrilleLoader getGrilleFileLoader() {
		return GrilleFactory.createFileLoader();
	}

	private IGrilleLoader getGrilleImageLoader() {
		return GrilleFactory.createImageLoader();
	}

}
