package iSudoku.itf;

public interface IStats {

	int getWins();

	int getTotalTimePlayed();

	int getQI();

	void registerGameEnd(int duration);
}
