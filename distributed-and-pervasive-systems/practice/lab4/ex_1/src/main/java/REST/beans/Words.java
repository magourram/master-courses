package REST.beans;

import java.util.ArrayList;
import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
@XmlAccessorType (XmlAccessType.FIELD)
public class Words {

    @XmlElement(name="my_word")
    private List<Word> wordslist;

    private static Words instance;

    private Words() {
        wordslist = new ArrayList<Word>();
    }

    //singleton
    public synchronized static Words getInstance(){
        if(instance==null)
            instance = new Words();
        return instance;
    }

    public synchronized List<Word> getWordslist() {

        return new ArrayList<>(wordslist);

    }

    public synchronized void setWordslist(List<Word> wordslist) {
        this.wordslist = wordslist;
    }

    public synchronized void add(Word u){
        wordslist.add(u);
    }


    public Word getByWord(String name){
        List<Word> usersCopy = getWordslist();
        for(Word u: usersCopy)
            if(u.getWord().toLowerCase().equals(name.toLowerCase()))
                return u;
        return null;
    }

    public boolean delete(Word word) {
        for(Word u: wordslist) 
            if(u.getWord().toLowerCase().equals(word.getWord().toLowerCase())) {
                wordslist.remove(u); 
                return true;
            }
        return false;
    } 
}
 
