package iSudoku.factory;

import iSudoku.itf.IStats;
import iSudoku.stats.Statistics;

public class StatFactory {

	// il faudrait assurer la persistence
	// private static final String prefs = "./player.profile";
	private static IStats instance;

	public static IStats getStats() {
		if (instance == null) {
			instance = new Statistics();
		}
		return instance;
	}

}
