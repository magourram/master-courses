package REST.services;

import javax.ws.rs.*;
import javax.ws.rs.core.Response;
import REST.beans.Words;
import REST.beans.Word;

@Path("words")
public class WordsService {

    @GET
    @Produces({"application/json", "application/xml"})
    public Response getWordsList(){
        return Response.ok(Words.getInstance()).build();
    }

    //permette di inserire un utente (nome e cognome)
    @Path("add")
    @POST
    @Consumes({"application/json", "application/xml"})
    public Response addWord(Word u){
        Words.getInstance().add(u);
        return Response.ok().build();
    }

    //permette di prelevare un utente con un determinato nome
    @Path("get/{word}")
    @GET
    @Produces({"application/json", "application/xml"})
    public Response getByWord(@PathParam("word") String word){
        Word u = Words.getInstance().getByWord(word);
        if(u!=null)
            return Response.ok(u).build();
        else
            return Response.status(Response.Status.NOT_FOUND).build();
    }


    @Path("put")
    @PUT
    @Consumes({"application/json", "application/xml"})
    public Response putDefinition(Word word){
        Word u = Words.getInstance().getByWord(word.getWord());
        if(u!=null) {
            u.setDefinition(word.getDefinition());
            return Response.ok(u).build();
        } else {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
    }


    @Path("del")
    @DELETE
    @Consumes({"application/json", "application/xml"})
    public Response delWord(Word word){
        if(Words.getInstance().delete(word)) {
            return Response.ok().build();
        } else {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
    }
    

}
