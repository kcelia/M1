package iSudoku.ihm.options;

import iSudoku.factory.HelpLevelFactory;
import iSudoku.itf.IHelpLevel;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JMenu;
import javax.swing.JMenuItem;

public class OptionsMenu extends JMenu {

	public OptionsMenu() {
		super("Options");
		JMenuItem noob = new JMenuItem("noob");
		JMenuItem ez = new JMenuItem("easy");
		JMenuItem med = new JMenuItem("medium");
		JMenuItem hard = new JMenuItem("hard");

		hard.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				setHard();
			}
		});

		med.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				setMedium();
			}
		});

		ez.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				setEasy();
			}
		});

		noob.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				setNoob();
			}
		});

		add(hard);
		add(med);
		add(ez);
		add(noob);
	}

	private IHelpLevel getHelpLevel() {
		return HelpLevelFactory.getHelpLevel();
	}

	protected void setNoob() {
		getHelpLevel().doShowInvalid(true);
		getHelpLevel().doShowInvalidCells(true);
		getHelpLevel().doShowSingleSolution(true);
		getHelpLevel().doShowSuggestions(true);
	}

	protected void setEasy() {
		getHelpLevel().doShowInvalid(true);
		getHelpLevel().doShowInvalidCells(true);
		getHelpLevel().doShowSingleSolution(false);
		getHelpLevel().doShowSuggestions(false);
	}

	protected void setMedium() {
		getHelpLevel().doShowInvalid(true);
		getHelpLevel().doShowInvalidCells(false);
		getHelpLevel().doShowSingleSolution(false);
		getHelpLevel().doShowSuggestions(false);
	}

	protected void setHard() {
		getHelpLevel().doShowInvalid(false);
		getHelpLevel().doShowInvalidCells(false);
		getHelpLevel().doShowSingleSolution(false);
		getHelpLevel().doShowSuggestions(false);
	}
}
