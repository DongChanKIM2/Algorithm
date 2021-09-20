package lab.ssafy.corona.virus;

public class Virus {
    protected String name = "바이러스";
    protected int level;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

//    public Virus() {}

    public Virus(String name, int level) {
        this.name = name;
        this.level = level;
    }

    public String toString() {
        return this.getName() + " " + this.getLevel();
    }
}
