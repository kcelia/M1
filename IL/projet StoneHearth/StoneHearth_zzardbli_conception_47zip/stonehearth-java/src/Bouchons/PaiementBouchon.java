package Bouchons;

import Interface.IPaiement;

public class PaiementBouchon implements IPaiement {
	public Boolean payer(String cb, Float montant) {
		return true;
	}
}
