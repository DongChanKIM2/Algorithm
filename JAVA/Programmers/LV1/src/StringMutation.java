import java.util.Locale;

public class StringMutation {
    public static void main(String[] args) {
        String phrase = "change is evitable";
        String mutation1, mutation2, mutation3, mutation4;

        System.out.println(phrase);

        mutation1 = phrase.concat(", excepti");
        mutation2 = mutation1.toUpperCase();
        mutation3 = mutation2.replace('C', 'P');
        mutation4 = mutation3.substring(0, 27);

        System.out.println(mutation1);
        System.out.println(mutation2);
        System.out.println(mutation3);
        System.out.println(mutation4);

    }
}
