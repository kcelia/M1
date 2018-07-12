package iSudoku.ihm.grille;

import java.util.concurrent.TimeUnit;

/** Classe piquée sur stackoverflow :
 * 
 *http://stackoverflow.com/questions/1770010/how-do-i-measure-time-elapsed-in-java
 *
 */
public class TimeWatch {

	long starts;

	public static TimeWatch start() {
		return new TimeWatch();
	}

	private TimeWatch() {
		reset();
	}

	public TimeWatch reset() {
		starts = System.currentTimeMillis();
		return this;
	}

	public long time() {
		long ends = System.currentTimeMillis();
		return ends - starts;
	}

	public long time(TimeUnit unit) {
		return unit.convert(time(), TimeUnit.MILLISECONDS);
	}
	
	public long timeSecs () {
		return time(TimeUnit.SECONDS);
	}

}