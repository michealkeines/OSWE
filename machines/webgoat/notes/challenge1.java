import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

//boolean passwordCorrect = "admin".equals(username) && PASSWORD.replace("1234", String.format("%04d",ImageServlet.PINCODE)).equals(password);
//we need to find the correct password
//String PASSWORD = "!!webgoat_admin_1234!!";
//1234 will be replaced by a random intergers that will be updated in the logo file

class Main {
  public static void main(String[] args) {

     try {
	     String filePath = "logo.png";

            // file to bytes[]
	     byte[] in = Files.readAllBytes(Paths.get(filePath));
     	     System.out.println(in[81216]);
	     System.out.println(in[81217]);
	     System.out.println(in[81218]);
	     System.out.println(in[81219]);
 	     System.out.println("Done");

        } catch (IOException e) {
            e.printStackTrace();
        }
  }
}
