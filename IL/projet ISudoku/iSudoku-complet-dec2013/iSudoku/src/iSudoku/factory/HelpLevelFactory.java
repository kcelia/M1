package iSudoku.factory;

import iSudoku.itf.IHelpLevel;
import iSudoku.options.HelpLevel;

public class HelpLevelFactory {

	private static HelpLevel instance;

	public static IHelpLevel getHelpLevel() {
		if (instance == null) {
			instance = new HelpLevel();
		}
		return instance;
	}
}
