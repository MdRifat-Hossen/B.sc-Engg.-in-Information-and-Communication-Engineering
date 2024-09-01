import java.util.Scanner;

class addstring {
    public String name1;
    public String name2;

    public addstring(String name1, String name2) {
        this.name1 = name1;
        this.name2 = name2;
    }

    public void add() {
        String name3;
        name3 = name1 + name2;
        System.out.println(name3);
    }
}

public class lab6_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        String a1 = scanner.nextLine();

        addstring obj = new addstring(s, a1);
        obj.add();
    }
}