# Greenfield

## Technologies

- gRPC

- Protocol Buffer

- gson

- Jersey 1.19

- AspectJ

## Requirements

- Java 1.8 

- Gradle >= 7.4.2 

## Compile and run

> You can use `gradle` or `./gradlew`  

**First of all run `gradle` or `./gradlew` to check that everything is OK.**

#### Compile java with aspectj:


```
gradle :compileJava
```

or

```
./gradlew :compileJava
```

Note that `.aj` files must be on `src/main/aspectj` folder.

If you want to put `.aj` file on the same directory of `.java` files, 
you should replace on `build.gradle` file `compileJava.ajc.options.compilerArgs = ["-sourceroots", "../../../src/main/aspectj"]` 
with `compileJava.ajc.options.compilerArgs=["-sourceroots", sourceSets.main.java.sourceDirectories.getAsPath()]`

#### Build project: 

```
gradle build
```

or

```
./gradlew build
```



