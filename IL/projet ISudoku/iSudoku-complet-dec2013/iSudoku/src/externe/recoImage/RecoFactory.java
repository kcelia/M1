package externe.recoImage;

public class RecoFactory {

	public static IReconnaissanceImage createRecoImage() {
		return new RecoImageBouchon();
	}
}
