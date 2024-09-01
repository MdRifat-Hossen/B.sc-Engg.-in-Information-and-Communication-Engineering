import javax.swing.*;
import java.awt.event.*;

public class TextFieldExample implements ActionListener {
    JTextField t1, t2, t3;
    JButton b1, b2, b3, b4;

    TextFieldExample() {
        JFrame f = new JFrame();
        t1 = new JTextField();
        t1.setBounds(50, 50, 150, 20);
        t2 = new JTextField();
        t2.setBounds(50, 100, 150, 20);
        t3 = new JTextField();
        t3.setBounds(50, 150, 150, 20);
        t3.setEditable(false);
        b1 = new JButton("+");
        b1.setBounds(50, 200, 50, 50);
        b2 = new JButton("-");
        b2.setBounds(120, 200, 50, 50);
        b3 = new JButton("/");
        b3.setBounds(190, 200, 50, 50);
        b4 = new JButton("*");
        b4.setBounds(270, 200, 50, 50);
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        f.add(t1);
        f.add(t2);
        f.add(t3);
        f.add(b1);
        f.add(b2);
        f.add(b3);
        f.add(b4);
        f.setSize(400, 600);
        f.setLayout(null);
        f.setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        String s = t1.getText();
        String s1 = t2.getText();
        int a = Integer.parseInt(s);
        int b = Integer.parseInt(s1);
        int c = 0;
        if (e.getSource() == b1) {
            c = a + b;
        } else if (e.getSource() == b2) {
            c = a - b;
        } else if (e.getSource() == b3) {
            if (a > 0) {
                c = a / b;
            } else {
                System.out.println("Cant Dividec");
            }
        } else {
            c = a * b;
        }
        String resutl = String.valueOf(c);
        t3.setText(resutl);
    }

    public static void main(String[] args) {
        new TextFieldExample();
    }
}
