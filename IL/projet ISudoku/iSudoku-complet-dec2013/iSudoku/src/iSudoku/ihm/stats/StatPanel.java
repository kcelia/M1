package iSudoku.ihm.stats;

import iSudoku.factory.StatFactory;
import iSudoku.itf.IStats;

import javax.swing.Box;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class StatPanel extends JPanel {

	private JTextField winTF;
	private JTextField qiTF;
	private JTextField timeTF;

	public StatPanel() {
		Box b1 = Box.createHorizontalBox();
		b1.add(new JLabel("Wins :"));
		winTF=new JTextField(5);
		winTF.setEditable(false);
		b1.add(winTF);		
		add(b1);
		
		Box b2 = Box.createHorizontalBox();
		b2.add(new JLabel("QI :"));
		qiTF=new JTextField(5);
		qiTF.setEditable(false);
		b2.add(qiTF);		
		add(b2);
		
		Box b3 = Box.createHorizontalBox();
		b3.add(new JLabel("Temps total :"));
		timeTF=new JTextField(5);
		timeTF.setEditable(false);
		b3.add(timeTF);		
		add(b3);
		
		refreshVisuals();
	}

	void refreshVisuals() {
		winTF.setText(getStats().getWins()+"");
		qiTF.setText(""+ getStats().getQI());
		timeTF.setText(""+getStats().getTotalTimePlayed());
	}

	private IStats getStats() {
		return StatFactory.getStats();
	}
}
