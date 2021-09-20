package lab.ssafy.corona.app;

import lab.ssafy.corona.virus.Corona;
import lab.ssafy.corona.virus.Virus;

public class CoronaTest {
    public static void main(String[] args) {

        Virus virus = new Corona("COVID19", 5 , 20);
        System.out.println(virus);


        Corona corona = new Corona("COVID19", 5 , 20);
        System.out.println(corona);

//        Virus virus = new Virus("UNKNOWN", 5);
//
//        System.out.println(virus);
//        Virus virus = new Virus();
//        virus.setName("MERS");
//        virus.setLevel(5);

//        Corona corona = new Corona("Corona", 8, 200);
//        corona.setName("corona");
//        corona.setSpreadSpeed(200);
//        corona.setName("Corona");
//        corona.setLevel(8);
//        corona.setSpreadSpeed(200);

//        corona.showInfo();

    }
}
