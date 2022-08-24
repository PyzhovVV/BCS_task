1. Фронтовая часть задания простая: кнопка «Отправить транзакцию» и список отправленных транзакций с вашего бэкенда.
2. Бэкенд: по нажатию на кнопку «Отправить транзакцию» у вас должны выполняться следующие действия:
◦ запросить по rpc у нашей ноды новый адрес (доступы rpc ниже в ресурсах) — rpc-команда getnewaddress — возврщается json вида
 {"result":"BEusyCzC9PaFqL4RGyxPAwJYiLhmEcCVSB","error":null,"id":"curltext"}
◦ Сформировать транзакцию с отправкой 1 коина (1е8 сатоши) с вашего адреса на полученный адрес на предыдущем шаге,
 подписать эту транзакцию и получить ее hex-представление. Можно использовать любые готовые решения (например, pycoin),
 но обратите внимание, что в выбранном пакете необходима реализация, где можно указать сеть (network), отличную от Биткоина.
 Параметры сети BCS Chain представлены ниже в ресурсах. ◦ Отправить полученную транзакцию в блокчейн. Это можно сделать одним из двух способов (выбор остается на ваше усмотрение):
 ▪ Вызвать rpc-команду sendrawtransaction и ее параметром передать полученное hex-представление транзакции
 ▪ Вызвать POST-метод API /tx/send с параметром rawtx={hex-представление транзакции} ◦ В ответе вам вернется json c ID транзакции, который необходимо записать в вашу БД и выводить ее в списке транзакций на фронте.
3. Сделать админ-панель приложения, из которой можно добавлять к каждой транзакции свое описание (его нужно будет отображать не на индексной странице, а генерировать страницу с адресом /tx/txid )