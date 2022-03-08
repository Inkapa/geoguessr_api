import httpx

r = httpx.get("https://www.geoguessr.com/api/maps?createdBy=612a0b6ba6278c0001bec01e&page=0&count=9", cookies={'_ncfa': "ealcexPaxj8OBiVv9/8W0qRD0D6KA85IQDjMYeuwvTc=aV1Bzd8nZcGEReDiQvcjGOLwugAopUu9z1zvmvKAoDf8/WYZkbDIo84/UM2L/EGu"})
if r.json():
    print("a")
