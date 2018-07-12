package iSudoku.ihm.grille;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.util.List;

import iSudoku.factory.GrilleFactory;
import iSudoku.factory.HelpLevelFactory;
import iSudoku.factory.StatFactory;
import iSudoku.itf.IGrille;
import iSudoku.itf.IGrilleContrainte;
import iSudoku.itf.IHelpLevel;

import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.LineBorder;

public class GrillePanel extends JPanel {

	private IGrilleContrainte grille;
	private List<CellButton> boutons = new ArrayList<CellButton>();
	private TimeWatch timer;

	public GrillePanel() {
		super(new GridLayout(3, 3));
		setGrille(GrilleFactory.createNewEmptyGrille());

		
		for (int sl = 0; sl < 3; sl++) {
			for (int sc = 0; sc < 3; sc++) {
				JPanel sub = new JPanel(new GridLayout(3,3));
				sub.setBorder(new LineBorder(Color.BLACK,4));
				for (int dl = 0; dl < 3; dl++) {
					for (int dc = 0; dc < 3; dc++) {
						CellButton bouton = new CellButton(this, sl*3+dl,  sc*3+dc);
						boutons.add(bouton);
						
						sub.add(bouton);
					} // dc
				} // dl
				this.add(sub);
			} // sc
		} // sl
		

		repaint();
	}

	public IGrilleContrainte getGrille() {
		return grille;
	}
	
	public void testFinPartie() {
		if (grille.estPleine() && grille.computeGrilleIsValid()) {
			StatFactory.getStats().registerGameEnd((int) timer.timeSecs());
			JOptionPane.showMessageDialog(null, "Partie gagnée en " + timer.timeSecs() + " secondes !");
			timer.reset();
		}
	}

	public void setGrille(IGrille grille) {
		this.grille = GrilleFactory.getContraintes(grille);
		timer = TimeWatch.start();
		repaint();
	}

	@Override
	public void paint(Graphics arg0) {
		if (getHelpLevel().shouldShowInvalid()) {
			if (grille.computeGrilleIsValid()) {
				setBorder(new LineBorder(Color.GREEN, 2));
			} else {
				setBorder(new LineBorder(Color.RED, 5));
			}
		} else {
			setBorder(new LineBorder(Color.BLACK, 2));
		}
		super.paint(arg0);
	}

	private IHelpLevel getHelpLevel() {
		return HelpLevelFactory.getHelpLevel();
	}
}
