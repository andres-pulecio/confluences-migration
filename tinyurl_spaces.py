import requests
import csv

espacios = ['~athayyil', '~avkumar', '~ayaseer', '~ayu', '~bburdan', '~bdiallo', '~bhoudek', '~bibanez', '~bkrishnamoorthy', '~blane', '~bmarlok', '~bmuthukrishnan', '~brtaylor', '~btang', '~bthirupathi', '~bwilliams', '~bzylbersztajn', '~cachgill', '~cbhagat', '~ccloutier', '~ccovert', '~cdixon', '~ceickemeyer', '~cflorez', '~cgraham', '~cgutt', '~chjones', '~ckumar', '~cmeneses', '~cospina', '~cpadilla', '~cromero-principe', '~crpinzon', '~csotozuluaga', '~csuarez', '~cwilbur', '~dbarrero', '~dcano', '~dcardona', '~dcepeda', '~dchmurciak', '~dcholakova', '~devans', '~dgaray', '~dgore', '~dguzman', '~dhavard', '~djoshila', '~dlazarova', '~dmanev', '~dnayak', '~driano', '~drodriguezvenegas', '~dsady', '~dsivaprakasam', '~dsoto', '~dstepanavicius', '~dstoyanova', '~dtorohoyos', '~ea', '~ebyl', '~edavidson', '~edsandoval', '~ejackson', '~enasevska', '~enemcova', '~eperez', '~esilva', '~fkhan', '~fclausen', '~fegonzalez', '~fklemming', '~frichtarik', '~gbalakrishnan', '~gharper', '~gpalacios', '~gpalanisamy', '~graja', '~gsabesan', '~gvargas', '~gyoung', '~hahmad', '~har', '~hhimmelberger', '~hmohanakrishnan', '~hrajaraman', '~hroumani', '~hvenkataramanan', '~iandrea', '~iiniguez', '~ikedron', '~iklandev', '~iluska', '~imitkov', '~itrakimas', '~jalbert', '~jarias', '~javargas', '~jboulier', '~JBrant', '~jchalex', '~jchou', '~jcohecha', '~jcopete', '~jdiamant', '~jeng', '~jespinosa', '~jfraser', '~jhale', '~jhalvarez', '~jhorsley', '~jhuang', '~jkelley', '~jkirby', '~jkostrhun', '~jkratochvil', '~jkrstevski', '~jlindsey', '~jm', '~jmacdonald', '~jmartinez', '~jmauro', '~jmccormick', '~jmeticota', '~johernandez', '~jrector', '~jricaurte', '~jrios', '~jrubio', '~jruiz', '~jschweitzer', '~jspencer', '~jspurny', '~jstepan', '~jstormo', '~jstruhar', '~jsuarezmartinez', '~jsvargas', '~jsvoboda', '~jtriana', '~juribe', '~jvaca', '~jvargas', '~jwalthall', '~jwebb', '~kapalanisamy', '~kberanek', '~kbharathi', '~kchilders', '~kkrishnan', '~kkumar', '~kkuppula', '~kmaity', '~knorman', '~kruppa', '~ksubbiah', '~ktomeska', '~laclark', '~lbrock', '~lciomei', '~lcorredor', '~lcortes', '~ldiaz', '~lkoukal', '~lmetzger', '~lmoss', '~lmyftaraj', '~lneumann', '~lperez', '~lplachkycc', '~lprice', '~lramirez', '~lroy', '~lsalomone', '~lsindelka', '~lsolarte', '~ltanaskovikj', '~lthota', '~lusanchez', '~lzapata', '~makens', '~mbeyazit', '~mcackova', '~mcai', '~mcifuentes', '~mcobb', '~mcuello', '~mdurai', '~mescobar', '~mfajt', '~mferraroni', '~mhamdy', '~mjaifank', '~mkafka', '~mkauffman', '~mklouda', '~mkv', '~mlesniak', '~mmaric', '~mmedina', '~mmelocik', '~mnadeau', '~mnielsen', '~moneil', '~mor', '~mosmani', '~mpitonak', '~msananes', '~mstusek', '~mtrajkov', '~mvazan', '~naugustus', '~ngopal', '~nguy', '~nhavlova', '~nikumar', '~nkamper', '~nmanivannan', '~nmarin', '~ntalevski', '~nwall', '~ocasallas', '~ocuhel', '~ofajardo', '~omiltonpackiaraj', '~parodriguez', '~pdans', '~pgupta', '~pjovic', '~pkacer', '~pkodytek', '~pmj', '~pmoll', '~pomohan', '~pparthiban', '~ppavelka', '~ppayares', '~ppearcy', '~ppineda', '~ppinzon', '~ppolasek', '~pvediyappan', '~rariza', '~rcostello', '~rdesiano', '~rdickinson', '~rdolezal', '~rfoster', '~rjzhang', '~rk', '~rkalaiselvan', '~rmedlin', '~rmischler', '~rpaveska', '~rpeterson', '~rrakshithr', '~rrodriguezville', '~rrogers', '~rsalcedo', '~rstaudinger', '~rsterrett', '~rsubramanian', '~rtasevska', '~saravichandran', '~sasudhakar', '~sbiruduraju', '~sbp', '~sbroughton', '~sbyrne', '~sc', '~scrown', '~sdelcampo', '~sekumaran', '~seswarlal', '~sfarias', '~sg', '~sgaeremynck', '~sgonzalez', '~sgorsuch', '~shameed', '~sharris', '~shessenthaler', '~shoffman', '~sjayaraj', '~skamalanathan', '~sksrinivasan', '~skumbeswaran', '~slaforge', '~smahato', '~smanimaran', '~smartinezlizarazo', '~smoorthyk', '~smuruganandham', '~spandian', '~spaskova', '~srajan', '~sristovska', '~srojasherrera', '~ssankaran', '~ssathyakumar', '~sselvapriya', '~ssharmishtha', '~ssilva', '~stamilmani', '~sthoomati', '~sumkumar', '~svaikaikani', '~svaratharaj', '~tbednarek', '~tcrody', '~tgrady', '~thochstetler', '~thunter', '~tkack', '~triley', '~trollinger', '~truzicka', '~tsyed', '~ttelecky', '~varju', '~vflorez', '~vgadepalli', '~vhernandez-shep', '~viriarte', '~vkuttan', '~vmedarski', '~vrg', '~vsekharpasupule', '~vselvaraju', '~vtorres', '~vvelan', '~wmulvihill', '~wrojas', '~wstawicki', '~yespinosagonzalez', '~ykanak', '~zb', '~zhasekcc']
results = []
def main():
    for espacio in espacios:
        url = f"https://confluence.bbpd.io/rest/api/content?spaceKey={espacio}"
        fetch_data(url)
        with open(f"{espacio}.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["pageid", "title", "tinyui", "searchurl"])
            writer.writerows(results)
            print(espacio)

def fetch_data(url):
    headers = {'Authorization': 'Bearer <TOKEN>'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        handle_page_of_results(data)
        if "next" in data["_links"]:
            next_url = "https://confluence.bbpd.io" + data["_links"]["next"]
            fetch_data(next_url)


def handle_page_of_results(data):
    for result in data["results"]:
        pageid = result["id"]
        title = result["title"]
        tinyui = "https://confluence.bbpd.io" + result["_links"]["tinyui"]
        searchurl = "https://www.microsoft365.com/search?auth=2&home=1&q=" + title.replace(" ", "+")
        results.append([pageid, title, tinyui, searchurl])

main()
print("Archivo CSV creado correctamente.")
