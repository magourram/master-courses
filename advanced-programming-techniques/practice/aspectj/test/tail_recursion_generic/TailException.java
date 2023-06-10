import java.util.*;

public class TailException extends Exception {

  public Object[] args;

  public TailException(Object[] args) {
    this.args = args;
  }
}									
