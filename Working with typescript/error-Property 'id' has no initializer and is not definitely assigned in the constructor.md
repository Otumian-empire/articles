- Property 'id' has no initializer and is not definitely assigned in the constructor.ts(2564) (property) User.id: number

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

In tsconfig.json, set, `"strictPropertyInitialization": false` 







