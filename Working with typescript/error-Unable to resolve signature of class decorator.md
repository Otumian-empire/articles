- Unable to resolve signature of class decorator when called as an expression.
  The runtime will invoke the decorator with 2 arguments, but the decorator expects 1

We have a very simple entity

```ts
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    firstName: string;

    @Column()
    lastName: string;

    @Column()
    isActive: boolean;
}
```

Go into the tsconfig.json file and set, `"experimentalDecorators": true` 

