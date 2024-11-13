import javax.swing.*;
import java.awt.event.*;

public class summary implements ActionListener {
    JLabel l1, l2;
    JTextArea t1;
    JButton b;

    summary() {
        JFrame f = new JFrame("Counting string");
        l1 = new JLabel("Word COunt");
        l1.setBounds(50, 25, 100, 30);
        l2 = new JLabel("String count");
        l1.setBounds(160, 25, 100, 30);
        t1 = new JTextArea();
        t1.setBounds(20, 75, 250, 200);
        b = new JButton();
        b.setBounds(100, 300, 120, 30);
        b.addActionListener(this);
        f.add(l1);
        f.add(l2);
        f.add(t1);
        f.add(b);
        f.setSize(400, 500);
        f.setLayout(null);
        f.setVisible(true);
    }

    public void ActionListener(ActionEvent e) {
        String text = t1.getText();
        String words[] = text.split("\\");
        l1.setText("Words: " + words.length);
        l1.setText("charetcere: " + text.length());
    }

    public static void main(String[] args) {
        new summary();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'actionPerformed'");
    }

}
