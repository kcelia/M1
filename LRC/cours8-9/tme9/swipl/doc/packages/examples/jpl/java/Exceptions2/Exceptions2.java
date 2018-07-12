import org.jpl7.PrologException;
import org.jpl7.Query;

public class Exceptions2 {
	public static void main(String argv[]) {
		// Prolog.set_default_init_args(new String[] { "libpl.dll", "-f", "none", "-g", "set_prolog_flag(debug_on_error,false)", "-q" });
		System.out.print("Calling\n\n");
		System.out.print("?- X is Y.\n\n");
		System.out.print("in Prolog to force an 'instantiation_error' exception,\n");
		System.out.print("whose getMessage() will be println-ed to System.out.\n\n");
		try {
			Query.hasSolution("X is Y");
		} catch (PrologException e) {
			System.out.println(e.getMessage());
		}
	}
}
