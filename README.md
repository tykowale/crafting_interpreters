# Crafting Interpreters

Here is going to be the source for the java version

https://craftinginterpreters.com/

## Running 
Right now I use gradle - let's see if I continue that.

```bash
./gradlew run [--args="foo --bar"]
```

## Building the jar and running it
```bash
./gradlew build

java -jar build/libs/lox-1.0-SNAPSHOT.jar 
```