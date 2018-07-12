package iSudoku.options;

import iSudoku.itf.IHelpLevel;

public class HelpLevel implements IHelpLevel {

	private boolean showInvalid = true;
	private boolean showInvalidCells = true;
	private boolean showSingle = true;
	private boolean showSuggs = true;

	@Override
	public boolean shouldShowInvalid() {
		return showInvalid;
	}

	@Override
	public void doShowInvalid(boolean set) {
		showInvalid = set;
	}

	@Override
	public boolean shouldShowInvalidCells() {
		return showInvalidCells;
	}

	@Override
	public void doShowInvalidCells(boolean set) {
		showInvalidCells = set;
	}

	@Override
	public void doShowSingleSolution(boolean b) {
		showSingle = b;
	}

	@Override
	public void doShowSuggestions(boolean b) {
		showSuggs = b;
	}

	@Override
	public boolean shouldShowSuggestions() {
		return showSuggs;
	}

	@Override
	public boolean shouldShowSingleSolution() {
		return showSingle;
	}

}
