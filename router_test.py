from router import Router


router = Router()

router.add("hello", lambda: "Hello Yhomi")

print(router.run("hello"))