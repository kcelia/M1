package iSudoku.ihm.stats;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JDialog;
import javax.swing.JMenu;
import javax.swing.JMenuItem;

public class StatsMenu extends JMenu {

	
	private JDialog dialog;
	private StatPanel stats;

	public StatsMenu() {
		super("Stats");
		
		JMenuItem show = new JMenuItem("Show stats");
		
		show.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				showStats();
			}
		});
		
		add(show);
		
		dialog = new JDialog();
		dialog.setSize(400,400);
		stats = new StatPanel();
		dialog.setContentPane(stats);
	}

	protected void showStats() {
		stats.refreshVisuals();
		dialog.setVisible(true);
	}
}
