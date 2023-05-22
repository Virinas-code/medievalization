# Medievalization

## Modding system (`modules.modloader`)

### Ways of modding

#### 1. Adding new routes

##### 1.1. Controllers

A mod can define custom controllers and blueprints that will be added to the server.
They can be used for new routes.

###### Example: The about page mod

For example, the ***`about`*** mod adds a blueprint, **`pages`**. This blueprints has a *`about`* controller associated to 