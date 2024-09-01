import java.util.Scanner;

class student {
    public String name;
    public int age, roll;

    public student(String name, int age, int roll) {
        this.name = name;
        this.age = age;
        this.roll = roll;
    }

    void diplya() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(roll);

    }
}

public class lab7_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();
        int age = scanner.nextInt();
        int roll = scanner.nextInt();
        student obj = new student(name, age, roll);
        obj.diplya();
    }
}