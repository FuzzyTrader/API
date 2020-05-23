# FuzzyTrader
Ferramenta de apoio de decisão de investimento. Uma pessoa precisa não apenas acompanhar quanto custam seus investimentos (carteira) como precisa de apoio antes de fazê-lo.

Para isso, a aplicação deve permitir que o usuário tome as seguintes ações:

* Informar um valor (em dólar) que deseja aplicar;
* Com base no valor informado, apresentar um conjunto de ativos sugeridos (entre criptomoedas e ações);
* Então o usuário deve escolher qual ativo investirá o montante. Este fará parte de sua carteira;
* Deve-se então consolidar a sua carteira mostrando a quantidade atual de cada ativo e o valor atual do mesmo (e a soma da carteira).

# Endpoints
| Método | Ação | Endpoint |
|--------|------|----------|
| POST  | Cadastra um usuário no sistema. | /api/users/register |
| POST   | Autenticação no sistema.   | /api/users/login  |
| POST   | Adiciona um ativo na carteira do usuário.  | /api/stocks/add  |
| GET    | Busca os ativos da carteira do usuário.  | /api/stocks/wallet  |
