# Now we are talking redis

I have had my mishap. I have turned right and left, not know what is wrong. Typescript saved the day and now I have to learn some specifics of Typescript.

I started with `redis-om` version `0.2.0`. Then upgraded to version `0.3.6` which is the current version.

## Create a connection

```ts
// client.ts
import { Client } from "redis-om";

const REDIS_URI = proceess.env.REDIS_URI;

const client: Client = new Client();

const redisConnect = async () => {
  if (!client.isOpen()) {
    await client.open(REDIS_URI);
  }

  console.log(await client.execute(["PING", "Redis server running"]));
};

redisConnect();

export default client;
```

## Create Schema

The only thing here is is different from the others so far is that, this is `ts` and according to the [docs](https://www.npmjs.com/package/redis-om#a-note-for-typescript-users), we have to create an interface with the same name as the entity.

```ts
// schema.ts
import { Entity, Schema, SchemaDefinition } from "redis-om";

// This is necessary in ts
interface UserEntity {
  username: string;
  password: string;
  email: string;
}

class UserEntity extends Entity {}

const UserSchemaStructure: SchemaDefinition = {
  username: {
    type: "string"
  },
  password: {
    type: "string"
  },
  email: {
    type: "string"
  }
};

export default new Schema(UserEntity, UserSchemaStructure, {
  dataStructure: "JSON"
});
```

## Create repository

From what I have done so far, we can create a repository using `new Repository(schema, client)` or `client.fetchRepository(schema)`. The later worked. The form gave an error that `Repository` is an _abstract_ class. So we have to extend it and implement its _abstract_ methods, `writeEntity` and `readEntity`. I went with the former since it make my work faster.

```ts
// repository.ts
import { Entity, Repository } from "redis-om";
import client from "./client";
import schema from "./schema";

const repository: Repository<Entity> = client.fetchRepository(schema);

export default respository;
```

I look like a `ts` noob.

## Create a row

We will use the repository to create a new user. From what I have done so far, we can do:

```ts
// index.ts
import repository from "./repository";

const user = await repository.AndSave({
  username: "johndoe",
  email: "johndoe@gmail.com",
  password: "PASSjohndoe"
});

console.log(user);

// Output from the console log
/* 
{
  entityId: "01GB1W8GFDDX6FQN9H7F4T1808",
  username: "johndoe",
  password: "PASSjohndoe"
  email: "johndoe@gmail.com"
}
*/
```

or

```ts
// index.ts
import repository from "./repository";

const user = repository.createEntity({
  username: "johndoe",
  email: "johndoe@gmail.com",
  password: "PASSjohndoe"
});

const id = await repository.save(user);

// Output from the console log
// 01GB1W8GFDDX6FQN9H7F4T1808 // ID of the row created
```

## Conclusion

There is not much to say here than, keep trying and sleep when you have to. Even though I ws doing the right thing all the time and not getting the output I am expecting, I kept looking for others ways and posting the issue I was facing onto other platforms , hoping another person had faced the same issue. Typescript worked for me even though I never thought of using Typescript in the first place. Now another path to learn has opened.
