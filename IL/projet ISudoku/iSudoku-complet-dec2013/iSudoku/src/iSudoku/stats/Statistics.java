package iSudoku.stats;

import iSudoku.itf.IStats;

public class Statistics implements IStats {

	private int wins = 0;
	private int totalTime = 0;
	private int QI = 80;

	@Override
	public int getWins() {
		return wins;
	}

	@Override
	public int getTotalTimePlayed() {
		return totalTime;
	}

	@Override
	public int getQI() {
		return QI;
	}

	@Override
	public void registerGameEnd(int duration) {
		wins++;
		totalTime += duration;

		// un QI qui augmente...
		QI++;
		if (wins % 10 == 0)
			QI += 5;
		if (wins % 3 == 0)
			QI += 2;
	}

}
