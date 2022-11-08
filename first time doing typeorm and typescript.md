# First time using Typeorm and typsecript?

These are some error you have to watch out for

```
Type 'string' is not assignable to type '"mysql" | "mariadb" | "postgres" | "cockroachdb" | "sqlite" | "mssql" | "sap" | "oracle" | "cordova" | "nativescript" | "react-native" | "sqljs" | "mongodb" | "aurora-mysql" | ... 4 more ... | "spanner"'.ts(2322)
MysqlConnectionOptions.d.ts(12, 14): The expected type comes from property 'type' which is declared here on type 'DataSourceOptions'
```

This error occurred when I was setting up my database configurations for typeorm using the datasource. The `type` field has the above error. The `type` field expects a string literal but a string was passed to it. I passed all the `env` variables into a `.env` file and I read them into the datasource file. So what I did was to replace the `type` field with a string literal of the value passed. So just used "postgres" if the `TYPEORM_CONNECTION` is "postgres". This error is more of a typescript error. Another is that you pass the variable as `any`.

`{..., type: TYPEORM_CONNECTION as any, ... }`

https://stackoverflow.com/questions/58181006/pass-string-variable-to-type-in-typeormmoduleoptions
https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html


```
TypeError: Class constructor BaseEntity cannot be invoked without 'new'
```

This error occurred after a created my first entity. This was a typescript configuration error. In the `tsconfig.json` file, I changed 

```
{
  "compilerOptions": {
    ...,
    "target": "es5",
    ...
}
```

to 

```
{
  "compilerOptions": {
    ...,
    "target": "es6",
    ...
}

https://github.com/typeorm/typeorm/issues/9154#issuecomment-1182058874
https://stackoverflow.com/questions/50203369/class-constructor-cannot-be-invoked-without-new-typescript-with-commonjs
