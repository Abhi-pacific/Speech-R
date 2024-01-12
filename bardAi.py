from bardapi import BardCookies
cookies_dict = {
    '__Secure-1PSID':'cwjgBYauMld4sWoec4FqnPg9yEnwJBOgHiVbITBFzfsAsgIG0EtL2WJyH3WXl7yr9q0PVw.',
    '__Secure-1PSIDTS':'sidts-CjIBPVxjStpMLmCPIH3zjE-Rf_N56ITsaGlN7NRgbfaPug-d80PX1fRbP_dqTzRhd4Bw5BAA',
    '__Secure-1PSIDCC':'ACA-OxNptKuS0Lp1lJ20pHNXuqGQ6WE2tffEPY0NsCRogltKhF73j8pHtWghcKZi1D--iBcILA'
}
bard = BardCookies(cookie_dict=cookies_dict)

def reply(query):
    responce  = bard.get_answer(query)['content']
    return responce
if __name__ == '__main__':
    while True:
        query = input('Input Your Query :')
        responce = reply(query)
        print(responce)