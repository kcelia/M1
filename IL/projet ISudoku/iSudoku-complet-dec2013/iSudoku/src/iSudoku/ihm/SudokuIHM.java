package iSudoku.ihm;

import iSudoku.ihm.grille.GrillePanel;
import iSudoku.ihm.options.OptionsMenu;
import iSudoku.ihm.stats.StatsMenu;
import iSudoku.itf.IGrille;

import javax.swing.JFrame;
import javax.swing.JMenuBar;

public class SudokuIHM extends JFrame {

	private GrillePanel centerPanel;
	private FileMenu file;
	private OptionsMenu options;
	private StatsMenu stats;

	public SudokuIHM() {
		setTitle("iSudoku");
		setSize(800, 600);
		centerPanel = new GrillePanel();
		setContentPane(centerPanel);

		addMenuBars();

		setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		setVisible(true);
	}

	private void addMenuBars() {
		JMenuBar menu = new JMenuBar();

		file = new FileMenu(this);
		menu.add(file);

		options = new OptionsMenu();
		menu.add(options);

		stats = new StatsMenu();
		menu.add(stats);
		
		setJMenuBar(menu);
	}

	public void setGrille(IGrille grille) {
		centerPanel.setGrille(grille);
	}

}
