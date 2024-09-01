import javax.swing.*;
import java.awt.event.*;

public class TextAreaExample implements ActionListener {
    JLabel l1, l2;
    JButton b;
    JTextArea area;

    TextAreaExample() {
        JFrame f = new JFrame();
        l1 = new JLabel();
        l1.setBounds(50, 25, 100, 30);
        l2 = new JLabel();
        l2.setBounds(160, 25, 100, 30);
        area = new JTextArea();
        area.setBounds(20, 75, 250, 200);
        b = new JButton("Count");
        b.setBounds(100, 300, 120, 30);
        b.addActionListener(this);
        f.add(l1);
        f.add(l2);
        f.add(b);
        f.add(area);
        f.setSize(400, 600);
        f.setLayout(null);
        f.setVisible(true);

    }

    public void actionPerformed(ActionEvent e) {
        String s = area.getText();
        String words[] = s.split("\\s+");
        l1.setText("Word: " + words.length);
        l2.setText("CHerweter : " + s.length());
    }

    public static void main(String[] args) {
        new TextAreaExample();
    }
}