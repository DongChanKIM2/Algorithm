class Solution {
    public String solution(String new_id) {

        String answer = "";
        // System.out.println("new_id " + new_id);

        // 1. 소문자 처리
        new_id = new_id.toLowerCase();
        // System.out.println("소문자 처리 " + new_id);

        // 2. 필요없는 문자열 제거
        String tmp_b = new String("");
        for (int i=0; i < new_id.length(); i++) {
            // String 객체인 new_id 이므로 idx가 아님
            // 원하는 순서를 char로 변환시켜줌
            char ch = new_id.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                // String.valueof 안해도 되지만 String 형태 null값 포함
                tmp_b += String.valueOf(ch);
            } else if (ch >= '0' && ch <= '9') {
                tmp_b += String.valueOf(ch);
            } else if ( ch == '-' || ch == '_' || ch =='.') {
                tmp_b += String.valueOf(ch);
            }
        }

        // System.out.println(tmp_b);
        // System.out.println(tmp_b.length());
        int last = tmp_b.length() - 1;

        String tmp_c = new String("");
        // 3. 마침표가 2개 이상 연속이면 하나만 추가해주기
        // System.out.println(tmp_b); 
        for (int i=0; i < tmp_b.length() - 1; i++) {
            if (tmp_b.charAt(i) == '.' && tmp_b.charAt(i+1) == '.') {
                continue;
            } else {
                tmp_c += String.valueOf(tmp_b.charAt(i));
            }
        }
        tmp_c += String.valueOf(tmp_b.charAt(last));

        // System.out.println("마침표제거 " + tmp_c);
        // 4단계. 마침표 처음과 끝 제거
        // String tmp_d = new String("");
        if (tmp_c.length() > 0) {
            if (tmp_c.startsWith(".")) {
                tmp_c = tmp_c.substring(1, tmp_c.length());
            }
        }
        if (tmp_c.length() > 0) {
            if (tmp_c.endsWith(".")) {
                tmp_c = tmp_c.substring(0, tmp_c.length()-1);
            }
        }

        // System.out.println("마침표 처끝 제거 " + tmp_c);

        // 5단계. 빈문자열이면 a 대입        
        if (tmp_c.length() == 0) {
            tmp_c += "a";
        }

        // System.out.println("문자열 a 추가 " + tmp_c);

        // 6단계. 16자 이상이면 15자 이하로 + 마지막. 제거
        if (tmp_c.length() >= 16) {
            tmp_c = tmp_c.substring(0, 15);
            if (tmp_c.endsWith(".")) {
                tmp_c = tmp_c.substring(0, 14);
            }
        }
        // System.out.println("길이제한 " + tmp_c);

        // 7단계. 길이가 2자 이하면 마지막문자를 길이 3 추가
        if (tmp_c.length() <= 2) {
            char end = tmp_c.charAt(tmp_c.length()-1);

            while (tmp_c.length() < 3) {
                tmp_c += end;
            }
        }

        answer = tmp_c;

        return answer;
    }
}