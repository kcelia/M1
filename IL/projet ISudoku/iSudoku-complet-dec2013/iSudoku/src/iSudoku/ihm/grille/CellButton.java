package iSudoku.ihm.grille;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import iSudoku.factory.HelpLevelFactory;
import iSudoku.itf.IHelpLevel;

import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.border.LineBorder;

public class CellButton extends JButton {

	private final GrillePanel parent;
	private final int ligne;
	private final int col;

	public CellButton(GrillePanel grillePanel, int ligne, int col) {
		super();
		this.parent = grillePanel;
		this.ligne = ligne;
		this.col = col;
		refreshVisuals();

		addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				onClick();
			}
		});
	}

	protected void onClick() {
		// Do we provide suggestions ?
		String suggs = "";
		if (getHelpLevel().shouldShowSuggestions()) {
			suggs = "(hint :"
					+ parent.getGrille()
					.getSuggestions(ligne,col).toString()
					+ ")";
		}

		String valStr = JOptionPane
				.showInputDialog("Please enter a new cell value"
						+ suggs);

		// parse user input
		try {
			int value ;
			if (valStr==null || valStr.equals("")) {
				value = 0;
			} else {
				value = Integer.parseInt(valStr);
			}
			if (value >= 0 && value < 10) {
				parent.getGrille().setCellValue(ligne, col, value);
				parent.testFinPartie();
			}
		} catch (NumberFormatException e) {
			System.err.println("not a number, you fool !");
		}

	}

	@Override
	public void paint(Graphics arg0) {
		refreshVisuals();
		super.paint(arg0);
	}

	private void refreshVisuals() {
		int val = parent.getGrille().getCellValue(ligne, col);

		// update display value
		if (val != 0) {
			setText(Integer.toString(val));
		} else {
			setText("");
		}

		// default outline
		setBorder(new LineBorder(Color.BLACK, 1));
		
		// test if enabled
		if (parent.getGrille().isFixed(ligne, col)) {
			setEnabled(false);			
			return;
		} else {
			setEnabled(true);
		}

		if (getHelpLevel().shouldShowInvalidCells()
				&& !parent.getGrille().isCaseValid(ligne, col)) {
		
			// red outline for invalid cell			
			setBorder(new LineBorder(Color.RED, 1));
		
		} else if (getHelpLevel().shouldShowSingleSolution() && val == 0
				&& parent.getGrille().getSuggestions(ligne, col).size() == 1) {
			
			// outline cells with single solution ?
			setBorder(new LineBorder(Color.GREEN, 1));
			
		}

	}

	private IHelpLevel getHelpLevel() {
		return HelpLevelFactory.getHelpLevel();
	}

}
