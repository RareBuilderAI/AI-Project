from tool_router import ToolRouter


router = ToolRouter()


print("\nBRAND:")
print(router.run("brand"))


print("\nTOOLS:")
print(router.run("tools"))


print("\nWEATHER:")
print(router.run("weather"))


print("\nCALCULATOR:")
print(router.run("calculator"))


print("\nTODO:")
print(router.run("todo"))


print("\nCRYPTO:")
print(router.run("crypto"))


print("\nNEWS:")
print(router.run("news"))


print("\nEXPENSE:")
print(router.run("expense"))


print("\nMEMORY:")
print(router.run("memory"))
