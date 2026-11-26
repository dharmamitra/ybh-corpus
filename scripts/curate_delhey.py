#!/usr/bin/env python3
"""Curated layer of the YBh corpus map, after Delhey 2013.

This file is the editable source of data/delhey_checklist.json (one entry
per publication, witness or reference work that Delhey mentions, with his
page and section) and data/delhey.json (sections, rows and spans in
Delhey's own coordinates). Run it, then scripts/build_data.py --merge-only.
Every span cites the page of Delhey 2013; entries without spans are drawn in
the "not localised" strip of their group.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FASC = [[1, "279a03"], [2, "284a24"], [3, "289c23"], [4, "294b08"], [5, "299a02"], [6, "303b20"], [7, "308c11"], [8, "313a14"], [9, "318a03"], [10, "323b10"], [11, "328c02"], [12, "335a13"], [13, "341a22"], [14, "348b02"], [15, "355a13"], [16, "361b13"], [17, "368c02"], [18, "374c11"], [19, "381b19"], [20, "388b05"], [21, "395c02"], [22, "401c10"], [23, "406b14"], [24, "411c02"], [25, "417a21"], [26, "424a02"], [27, "430a02"], [28, "435c21"], [29, "442a21"], [30, "448b20"], [31, "454a11"], [32, "459b20"], [33, "465a23"], [34, "470c08"], [35, "478b06"], [36, "484b02"], [37, "491b08"], [38, "498c14"], [39, "505a17"], [40, "510c02"], [41, "516a02"], [42, "521c23"], [43, "527b10"], [44, "533b02"], [45, "539a02"], [46, "544a02"], [47, "549b11"], [48, "556b22"], [49, "564c22"], [50, "571a02"], [51, "579a03"], [52, "584b23"], [53, "589b06"], [54, "594c21"], [55, "601b02"], [56, "607a18"], [57, "613a05"], [58, "620c24"], [59, "627a02"], [60, "632b13"], [61, "638a14"], [62, "644b14"], [63, "648b06"], [64, "652c15"], [65, "658c07"], [66, "663b07"], [67, "668b22"], [68, "674a02"], [69, "678c04"], [70, "684c02"], [71, "690b10"], [72, "694c20"], [73, "699c13"], [74, "704c15"], [75, "710c24"], [76, "718a02"], [77, "723b13"], [78, "729a13"], [79, "736c16"], [80, "742c12"], [81, "749c21"], [82, "755a02"], [83, "760a06"], [84, "766b14"], [85, "772b12"], [86, "778b15"], [87, "785b02"], [88, "793a04"], [89, "800c02"], [90, "807b16"], [91, "814a18"], [92, "821a11"], [93, "827b19"], [94, "834a04"], [95, "840b17"], [96, "846c08"], [97, "853c02"], [98, "861a09"], [99, "868c02"], [100, "875c02"]]

SECTIONS = [
 # parts
 ("basic", 1, "Maulī Bhūmiḥ (Basic Section)", "本地分", "279a08", "577c17", "fasc. 1–50"),
 ("vin", 1, "Viniścayasaṃgrahaṇī", "攝決擇分", "579a08", "749c26", "fasc. 51–80"),
 ("vyakh", 1, "*Vyākhyā(na)saṃgrahaṇī", "攝釋分", "749c26", "760a11", "fasc. 81–83"),
 ("pary", 1, "Paryāyasaṃgrahaṇī", "攝異門分", "760a11", "772b17", "fasc. 83–84"),
 ("vastu", 1, "Vastusaṃgrahaṇī", "攝事分", "772b17", "882a13", "fasc. 85–100"),
 # bhūmis of the Basic Section
 ("b1", 2, "1 Pañcavijñānakāyasaṃprayuktā Bhūmiḥ", "五識身相應地", "279a08", "280b04", "fasc. 1"),
 ("b2", 2, "2 Manobhūmiḥ", "意地", "280b04", "294b13", "fasc. 1–3"),
 ("b3", 2, "3–5 Savitarkā Savicārā, Avitarkā Vicāramātrā, Avitarkāvicārā Bhūmiḥ", "有尋有伺等三地", "294b13", "328c07", "fasc. 4–10"),
 ("b6", 2, "6 Samāhitā Bhūmiḥ", "三摩呬多地", "328c07", "344b20", "fasc. 11–13"),
 ("b7", 2, "7 Asamāhitā Bhūmiḥ", "非三摩呬多地", "344b20", "344c17", "fasc. 13"),
 ("b8", 2, "8–9 Sacittikā, Acittikā Bhūmiḥ", "有心無心二地", "344c17", "345a18", "fasc. 13"),
 ("b10", 2, "10 Śrutamayī Bhūmiḥ", "聞所成地", "345a18", "361b18", "fasc. 13–15"),
 ("b11", 2, "11 Cintāmayī Bhūmiḥ", "思所成地", "361b18", "388b10", "fasc. 16–19"),
 ("b12", 2, "12 Bhāvanāmayī Bhūmiḥ", "修所成地", "388b10", "395c08", "fasc. 20"),
 ("b13", 2, "13 Śrāvakabhūmiḥ", "聲聞地", "395c08", "477c03", "fasc. 21–34"),
 ("b14", 2, "14 Pratyekabuddhabhūmiḥ", "獨覺地", "477c03", "478b12", "fasc. 34"),
 ("b15", 2, "15 Bodhisattvabhūmiḥ", "菩薩地", "478b12", "576b29", "fasc. 35–50"),
 ("b16", 2, "16 Sopadhikā Bhūmiḥ", "有餘依地", "576b29", "577b01", "fasc. 50"),
 ("b17", 2, "17 Nirupadhikā Bhūmiḥ", "無餘依地", "577b01", "577c17", "fasc. 50"),
 # chapters of the Viniścayasaṃgrahaṇī
 ("v1", 2, "Viniścaya on bhūmis 1–2", "五識身相應地意地", "579a08", "620c29", "fasc. 51–58"),
 ("v3", 2, "Viniścaya on bhūmis 3–5", "有尋有伺等三地", "620c29", "644b19", "fasc. 58–62"),
 ("v6", 2, "*Samāhitabhūmiviniścaya", "三摩呬多地", "644b19", "650c27", "fasc. 62–63"),
 ("v7", 2, "*Asamāhitabhūmiviniścaya", "非三摩呬多地", "650c27", "651b06", "fasc. 63"),
 ("v8", 2, "Viniścaya on bhūmis 8–9", "有心地・無心地", "651b06", "652c20", "fasc. 63–64"),
 ("v10", 2, "Viniścaya on bhūmi 10", "聞所成慧地", "652c20", "658c12", "fasc. 64–65"),
 ("v11", 2, "Viniścaya on bhūmi 11", "思所成慧地", "658c12", "668b27", "fasc. 65–67"),
 ("v12", 2, "*Bhāvanāmayībhūmiviniścaya", "修所成慧地", "668b27", "669b08", "fasc. 67"),
 ("v13", 2, "*Śrāvakabhūmiviniścaya (incl. bhūmi 14)", "聲聞地", "669b08", "694c25", "fasc. 67–71"),
 ("v15", 2, "*Bodhisattvabhūmiviniścaya", "菩薩地", "694c25", "747b28", "fasc. 72–80"),
 ("v16", 2, "Viniścaya on bhūmis 16–17 (nirvāṇa)", "有餘依及無餘依二地", "747b28", "749c26", "fasc. 80"),
 # Vastusaṃgrahaṇī
 ("vs-sutra", 2, "Sūtra-vastu (on the *Saṃyuktāgama)", "契經事", "772b17", "868c07", "fasc. 85–99"),
 ("vs-vinaya", 2, "Vinaya-vastu (Tib. *Vinayasaṃgrahaṇī)", "調伏事", "868c07", "878a26", "fasc. 99–100"),
 ("vs-matrka", 2, "Mātṛkā-vastu", "本母事", "878a26", "882a13", "fasc. 100"),
 # subdivisions (level 3)
 ("b10-adhy", 3, "adhyātmavidyā", "內明處", "345a18", "356a08", ""),
 ("b10-cik", 3, "cikitsāvidyā", "醫方明處", "356a08", "356a12", ""),
 ("b10-hetu", 3, "hetuvidyā", "因明處", "356a12", "360c22", ""),
 ("b10-sabda", 3, "śabdavidyā", "聲明處", "360c22", "361b05", ""),
 ("b10-silpa", 3, "śilpakarmasthānavidyā", "工業明處", "361b05", "361b18", ""),
 ("b11-12", 3, "sections 1–2", "自性清淨・思擇所知", "361b18", "363a11", ""),
 ("b11-pg", 3, "Paramārthagāthā", "勝義伽他", "363a11", "365c17", ""),
 ("b11-ag", 3, "Ābhiprāyikārthagāthā", "意趣義伽他", "365c17", "370a09", ""),
 ("b11-sg", 3, "Śarīrārthagāthā", "體義伽他", "370a09", "388b10", ""),
 ("b13-ys1", 3, "ŚrBh yogasthāna 1", "初瑜伽處", "395c08", "424a07", ""),
 ("b13-ys2", 3, "ŚrBh yogasthāna 2", "第二瑜伽處", "424a07", "448b25", ""),
 ("b13-ys3", 3, "ŚrBh yogasthāna 3", "第三瑜伽處", "448b25", "465a28", ""),
 ("b13-ys4a", 3, "ŚrBh yogasthāna 4, sect. 1 (laukikamārga)", "第四瑜伽處之一", "465a28", "470c13", ""),
 ("b13-ys4b", 3, "ŚrBh yogasthāna 4, sect. 2", "第四瑜伽處之二", "470c13", "477c03", ""),
 ("bb-I.1", 3, "I.1 Gotrapaṭala", "種姓品", "478b12", "480b25", ""),
 ("bb-I.2", 3, "I.2 Cittotpādapaṭala", "發心品", "480b25", "482c03", ""),
 ("bb-I.3", 3, "I.3 Svaparārthapaṭala", "自他利品", "482c03", "486b09", ""),
 ("bb-I.4", 3, "I.4 Tattvārthapaṭala", "真實義品", "486b09", "491b14", ""),
 ("bb-I.5", 3, "I.5 Prabhāvapaṭala", "威力品", "491b14", "496b26", ""),
 ("bb-I.6", 3, "I.6 Paripākapaṭala", "成熟品", "496b26", "498c20", ""),
 ("bb-I.7", 3, "I.7 Bodhipaṭala", "菩提品", "498c20", "500b10", ""),
 ("bb-I.8", 3, "I.8 Balagotrapaṭala", "力種姓品", "500b10", "505a23", ""),
 ("bb-I.9", 3, "I.9 Dānapaṭala", "施品", "505a23", "510c08", ""),
 ("bb-I.10", 3, "I.10 Śīlapaṭala", "戒品", "510c08", "523a15", ""),
 ("bb-I.11", 3, "I.11 Kṣāntipaṭala", "忍品", "523a15", "525c03", ""),
 ("bb-I.12", 3, "I.12 Vīryapaṭala", "精進品", "525c03", "527b16", ""),
 ("bb-I.13", 3, "I.13 Dhyānapaṭala", "靜慮品", "527b16", "528b27", ""),
 ("bb-I.14", 3, "I.14 Prajñāpaṭala", "慧品", "528b27", "529c16", ""),
 ("bb-I.15", 3, "I.15 Saṃgrahavastupaṭala", "攝事品", "529c16", "533b08", ""),
 ("bb-I.16", 3, "I.16 Pūjāsevāpramāṇapaṭala", "供養親近無量品", "533b08", "537b11", ""),
 ("bb-I.17", 3, "I.17 Bodhipakṣyapaṭala", "菩提分品", "537b11", "545b24", ""),
 ("bb-I.18", 3, "I.18 Guṇapaṭala", "菩薩功德品", "545b24", "549b17", ""),
 ("bb-II.1", 3, "II.1 Liṅgapaṭala", "菩薩相品", "549b17", "550c06", ""),
 ("bb-II.2", 3, "II.2 Pakṣapaṭala", "分品", "550c06", "551c10", ""),
 ("bb-II.3", 3, "II.3 Adhyāśayapaṭala", "增上意樂品", "551c10", "552c21", ""),
 ("bb-II.4", 3, "II.4 Vihārapaṭala", "住品", "552c21", "562c22", ""),
 ("bb-III.1", 3, "III.1 Upapattipaṭala", "生品", "562c22", "563b28", ""),
 ("bb-III.2", 3, "III.2 Parigrahapaṭala", "攝受品", "563b28", "564c28", ""),
 ("bb-III.3", 3, "III.3 Bhūmipaṭala", "地品", "564c28", "565c15", ""),
 ("bb-III.4", 3, "III.4 Caryāpaṭala", "行品", "565c15", "566c07", ""),
 ("bb-III.5", 3, "III.5 Lakṣaṇānuvyañjanapaṭala", "建立品 (first part)", "566c07", "568c20", ""),
 ("bb-III.6", 3, "III.6 Pratiṣṭhāpaṭala (+ IV Anukrama)", "建立品", "568c20", "576b29", ""),
]

sections = []
for sid, lvl, name, zh, a, b, fasc in SECTIONS:
    sections.append({"id": sid, "level": lvl, "name": name, "zh": zh, "from": a, "to": b, "fasc": fasc})

# ------------------------------------------------------------------ rows
D = "Delhey 2013"

# ====================================================================== ITEMS
# One item per publication / witness that Delhey mentions. `sec` = the
# paragraph of Delhey's survey, `pages` = Delhey pages. An item with no spans
# is "not localised" (drawn in the not-localised strip of its group).

ITEMS = []
def I(id, sect, pages, group, lang, type, label, spans, sub=None, dn=None, note=None):
    d = {"id": id, "delhey_section": sect, "pages": pages, "group": group, "lang": lang, "type": type,
         "label": label, "spans": spans}
    if sub: d["sub"] = sub
    if dn: d["dn"] = dn
    if note: d["note"] = note
    ITEMS.append(d)

def S(p, own=None, note=None, extent=None, **coord):
    d = dict(coord); d["page"] = p
    if own: d["own"] = own
    if note: d["note"] = note
    if extent: d["extent"] = extent
    return d

def SEC(p, sec, own=None, note=None):      # section-level placement of a partial treatment
    return S(p, sec=sec, own=own, note=note, extent="section-only")

PARTS = ["basic", "vin", "vyakh", "pary", "vastu"]
def WHOLE(p, note="concerns the whole Yogācārabhūmi"):
    return S(p, sec=PARTS, note=note, extent="whole-work")

DNSA = lambda i: {"id": i, "lang": "sa", "url": "https://dharmamitra.org/nexus/db/sa/%s/text" % i}
DNBO = lambda i: {"id": i, "lang": "bo", "url": "https://dharmamitra.org/nexus/db/bo/%s/text" % i}
DNZH = lambda i: {"id": i, "lang": "zh", "url": "https://dharmamitra.org/nexus/db/zh/%s/text" % i}

# ---------------------------------------------------------------- §1.2 manuscripts
I("ms-srbh", "1.2 no. 1", "508, 510, 517–523", "sa-ms", "sa", "manuscript", "Śrāvakabhūmi MS (ŚrBh MS)",
  sub="palm-leaf, Lhasa (Cat. Beijing 20–22); c. 11th c.?", spans=[
   S(517, sec="b7", note="Asamāhitā Bhūmiḥ, extant in both MSS"),
   S(518, sec="b8", note="Sacittikā/Acittikā (Wayman 1960 edited them from this MS)"),
   S(518, t=["354b17", "361b18"], note="Śrutamayī Bhūmiḥ: the adhyātmavidyā section is missing except for its end; start after the T1579 references of the Study Group edition (2007, App. II: the Sanskrit resumes in §A.I-7 = T 354b11–19, Ms. 15b6 at 354b19)", extent="approx-start"),
   S(520, sec="b11", note="Cintāmayī Bhūmiḥ: 'only the last 10–20% seem to be missing'", extent="approx-end"),
   S(510, sec="b13", note="nearly the complete Śrāvakabhūmi; three small parts (c. 7–8 Peking folios) missing (n. 49)"),
   S(523, sec="b14", note="Pratyekabuddhabhūmi")])
I("ms-srbh-facs", "1.2 no. 1a–d", "508", "sa-ms", "sa", "reproduction", "ŚrBh MS: facsimile 1994; Beijing microfilm; photos by Sāṅkṛtyāyana (nos. 350–351) and Tucci",
  sub="China Library of Nationalities & Taishō Univ. 1994; Göttingen prints Xc 14/27; Rome (Sferra 2009: 46, 51)",
  spans=[S(508, sec=["b7", "b8"]), S(508, t=["354b17", "388b10"], extent="approx-start"), S(508, sec=["b13", "b14"])])
I("ms-ybh", "1.2 no. 2", "508, 510, 515–523, 532", "sa-ms", "sa", "manuscript", "Yogācārabhūmi MS (YoBh MS)",
  sub="palm-leaf, Sa skya?; c. 1000 CE; all of the Basic Section except ŚrBh and BoBh", spans=[
   S(515, sec="b1", own="YoBh MS 1b–3b2"), S(516, sec="b2", own="YoBh MS 3b2–21a3"),
   S(516, sec="b3", own="YoBh MS 21a3–63a6"), S(517, sec="b6", own="YoBh MS 63a6–82b6"),
   S(517, sec="b7", own="YoBh MS 82b6–83a5"), S(518, sec="b8", own="YoBh MS 83a5–83b5"),
   S(518, sec="b10", own="YoBh MS 83b5–102b4"), S(520, sec="b11", own="YoBh MS 102b4–139a1"),
   S(521, sec="b12", own="YoBh MS 139a1–153a3"), S(523, sec="b14", own="YoBh MS 153a4–154b2"),
   S(532, sec="b16", own="YoBh MS 154b2–156a1"), S(532, sec="b17", own="YoBh MS 156a1–156b")])
I("ms-ybh-photos", "1.2 no. 2a–b", "508–509", "sa-ms", "sa", "reproduction", "YoBh MS: photos by Sāṅkṛtyāyana (no. 199) and Tucci",
  sub="Patna negatives; Göttingen prints Xc 14/28; Rome (Sferra 2009: 41)",
  spans=[S(508, sec=["b1", "b2", "b3", "b6", "b7", "b8", "b10", "b11", "b12"]), S(508, sec="b14"), S(508, sec=["b16", "b17"])])
I("ms-ybh-transcript", "1.2 no. 2, n. 37", "509", "sa-ms", "sa", "reproduction", "Sāṅkṛtyāyana's hand-written transcript of the YoBh MS",
  sub="whereabouts unknown; used by Bhattacharya 1957", spans=[],
  note="not localised: a transcript of the whole codex; lost")
for mid, lab, sub, p, note in [
    ("ms-bobh-c", "Cambridge MS of the BoBh (C)", "palm-leaf, Cambridge Add. 1702; c. 9th c.?", "509, 526–527, 531",
     "incomplete; lacks the very beginning of I.1; the only MS with the Anukramapaṭala"),
    ("ms-bobh-p", "Patna MS of the BoBh (P, B, R)", "palm-leaf, Lhasa (Cat. Beijing 19); 12th–14th c.?; Beijing microfilm; photos Sāṅkṛtyāyana no. 352, Tucci", "509, 526–527",
     "'fairly complete'; basis of Dutt 1966; the only MS with the very beginning of I.1"),
    ("ms-bobh-n", "National Archives MS of the BoBh", "palm-leaf, Kathmandu 3/681; NGMPP A 38/3", "509, 526", "not used by Wogihara and Dutt"),
    ("ms-bobh-k", "Kyoto MS of the BoBh (K)", "paper, Kyoto Univ. (Goshima & Noguchi 1983 no. 74); 19th c.", "509, 526", "an apograph of the National Archives MS (Takahashi 2005a)"),
]:
    I(mid, "1.2", p, "sa-ms", "sa", "manuscript", lab, sub=sub, note=note, spans=[S(509, sec="b15", note="Bodhisattvabhūmi; lacunae not specified")])
I("ms-bobh-kimura", "2.1.9.1 n. 136", "525", "sa-ms", "sa", "manuscript", "'Kimura MS' (Devanāgarī transcript) / 'Calcutta MS' of the BoBh",
  sub="transcript destroyed in WW II; a Calcutta MS possibly extant (Ui 1961; Sugawara 1990)", spans=[SEC(525, "b15")])
I("ms-sht964", "1.2 no. 7; 2.1.9.4", "510, 531", "sa-ms", "sa", "manuscript", "SHT III 964 (Turfan fragment)", sub="paper; c. 7th–10th c.; identified by Aramaki",
  spans=[S(531, bobhd=["159,23", "161,1"], own="BoBhD 159,23–161,1 = BoBhW 232,2–233,16", note="n. 168; Waldschmidt et al. give BoBhD 159,24–160,15")])
I("ms-vin-leningrad", "1.2 no. 8; 2.2.1.2", "510, 533", "sa-ms", "sa", "manuscript", "Viniścaya fragment, St Petersburg (Ms. Ind. VII.23 [421])",
  sub="paper; discovered by K. Matsuda (1988); unpublished; more folios in the Potala?", spans=[S(533, t=["589b19", "600c10"], own="Q5539.zi.31a5–59b2")])
I("ms-vin-kathm", "1.2 no. 9a; 2.2.5.3", "510, 535", "sa-ms", "sa", "manuscript", "Kathmandu NA 1/1697, folio a (Viniścaya)",
  sub="palm-leaf single folio; NGMPP A 39/3", spans=[S(535, t=["728c16", "730b21"], own="Q5539.'i.87b7–92a3 = Saṃdh VIII.39–IX.6")])
I("ms-pary-kathm", "1.2 no. 9b; 2.4", "510, 539", "sa-ms", "sa", "manuscript", "Kathmandu NA 1/1697, folio b (Paryāya)",
  sub="palm-leaf single folio", spans=[S(539, t=["768c20", "769c9"], own="Q5542.47b7–49b7")])
I("cit-asbh", "2.2.1.1", "532", "sa-ms", "sa", "citation", "Citation in the Abhidharmasamuccayabhāṣya (ASBh, ed. Tatia 1976)",
  dn=[DNSA("SA_T06_abhsubhu")], spans=[S(532, t=["579a14", "579c22"], own="ASBh 11,16–13,20 = Q5539.zi.2b2–4a4")])
I("cit-vastu-bh", "2.5", "539", "sa-ms", "sa", "parallel", "Vastusaṃgrahaṇī passage incorporated in the Savitarkādibhūmi",
  sub="the only part of the Vastusaṃgrahaṇī preserved in Sanskrit (Kritzer 1999: 157)", dn=[DNSA("SA_T06_n1394u")],
  spans=[S(539, t=["827c3", "828c12"], own="Q5540.285a3–287b6 = Bh. 198,17–203,5"),
         S(539, bh=["198,17", "203,5"], own="Bh. 198,17–203,5 (its place in the Basic Section)")])
I("cit-vyakhya-t1602", "1.3 n. 51", "511", "sa-ms", "multi", "citation", "Quotation of the Xiǎnyáng lùn in the *Yogācārabhūmivyākhyā",
  sub="Schmithausen 1987b: 261 n. 99 (after K. Matsuda)", spans=[], note="not localised")
I("cit-samdh", "2.2.5.3 n. 184", "536", "sa-ms", "sa", "citation", "Sanskrit testimonia of the Saṃdhinirmocanasūtra",
  sub="SHT III 923, 981; Triṃśikābhāṣya (Lévi 1925; Buescher 2007) [Saṃdh V]; Bhāvanākrama III (Tucci 1971) [III, VII.15]; Jñānaśrīmitranibandhāvalī [VIII.7] (Schmithausen 2005)",
  spans=[SEC(536, "v15", note="testimonia of the independent sūtra, which the *Bodhisattvabhūmiviniścaya quotes")])
# place the Saṃdh testimonia on the citation, not the whole chapter
ITEMS[-1]["spans"] = [S(536, t=["713c28", "736c12"], extent="section-only", note="testimonia of the independent sūtra; shown on the span of its citation in the Viniścaya")]

# ---------------------------------------------------------------- Sanskrit editions
I("ed-bh1957", "2.1.1", "515", "sa-ed", "sa", "edition", "Bhattacharya 1957 (Bh.)", sub="bhūmis 1–5, YoBh MS (+ transcript); compared with the Tibetan",
  dn=[DNSA("SA_T06_n1394u")], spans=[S(515, sec=["b1", "b2", "b3"], own="Bh. 3–232")])
I("ed-bh1946", "2.1.1 n. 77", "515", "sa-ed", "sa", "partial-edition", "Bhattacharya 1946", sub="ātmavāda passage (first use of Sāṅkṛtyāyana's photos)",
  spans=[S(515, bh=["129,6", "137,8"], own="Bh. 129,6–137,8")])
I("ed-schmit1987b", "2.0; 2.1.1; 2.1.3; 2.1.5", "512, 515–520", "sa-ed", "sa", "partial-edition", "Schmithausen 1987b (Ālayavijñāna)",
  sub="many passages edited/translated; index of texts", spans=[
   SEC(515, "b1", own="pp. 110–117", note="discussion (higher textual criticism)"),
   S(516, bh=["24,1", "24,10"], own="pp. 127–132: Bh. 24,1–10"),
   SEC(517, "b6", own="p. 276 n. 146", note="'Initial Passage' citation"),
   S(518, sec="b8", own="pp. 220–222", note="'very reliable' edition, both MSS"),
   SEC(520, "b11-pg", own="pp. 223–241", note="Paramārthagāthā vv. 28–41 with commentary (both MSS)"),
   SEC(532, "v1", own="pp. 671f.; 300 n. 226", note="discussion of the ālayavijñāna treatise"),
   WHOLE(512, note="'an extraordinarily high amount' of passages from all over the YoBh")])
I("ed-sakuma1990", "2.0 n. 62 and passim", "516–540", "sa-ed", "sa", "partial-edition", "Sakuma 1990 (Sanskrit passages)", sub="small passages with German translation",
  spans=[S(516, bh=["27,1", "27,3"], own="pp. 145f.: Bh. 27,1–3"),
   SEC(518, "b10-adhy", own="pp. 147–148", note="short citations of the Śrutamayī Bhūmi from the MS (n. 91)"),
   S(521, sh=["192,21", "202,2"], own="Sh. 192,21–202,2"), S(521, sh=["270,15", "270,20"], own="Sh. 270,15–20"),
   S(521, sh=["271,15", "272,6"], own="Sh. 271,15–272,6"), S(521, sh=["283,2", "284,3"], own="Sh. 283,2–284,3"),
   S(521, sh=["320,3", "320,5"], own="Sh. 320,3–5"), S(522, sh=["395,2", "398,6"], own="Sh. 395,2–398,6"),
   S(522, sh=["402,7", "402,20"], own="Sh. 402,7–20"), S(522, sh=["404,4", "405,9"], own="Sh. 404,4–405,9"),
   S(522, sh=["406,13", "407,3"], own="Sh. 406,13–407,3"), S(522, sh=["432,4", "433,18"], own="Sh. 432,4–433,18"),
   S(522, sh=["449,14", "455,3"], own="Sh. 449,14–455,3"),
   SEC(531, "bb-III.3", own="pp. 149–152", note="very short passages from III.3 …"),
   SEC(531, "bb-III.6", own="pp. 149–152", note="… and III.6"),
   SEC(532, ["b16", "b17"], own="pp. 153–154", note="a very small section (n. 172)")])
I("ed-ahn2003", "2.1.1", "517", "sa-ed", "sa", "partial-edition", "Ahn 2003: 56–87", sub="kleśasaṃkleśa, YoBh MS; German transl. pp. 158–214",
  dn=[DNSA("SA_T06_-ybh-klesa")], spans=[S(517, bh=["160,10", "170,10"], own="Bh. 160,10–170,10")])
I("ed-aymore1995", "2.1.1", "517", "sa-ed", "sa", "partial-edition", "Aymoré 1995 (unpublished M.A.)", sub="first half of karmasaṃkleśa; German transl.",
  spans=[S(517, bh=["170,11", "182,22"], own="Bh. 170,11–182,22")])
I("ed-wezler1985", "2.1.1", "516", "sa-ed", "sa", "partial-edition", "Wezler 1985", sub="Sāṃkhya sections partly emended on the MS; translated",
  spans=[S(516, bh=["118,14", "122,6"], own="Bh. 118,14–122,6")])
I("ed-kritzer1999", "2.1.1; 2.2.1.2; 2.5", "517, 533, 539", "sa-ed", "sa", "partial-edition", "Kritzer 1999", sub="Vasubandhu and the YBh; Skt/Tib/Chin passages with emendations (no MS)",
  spans=[S(517, bh=["200,6", "201,13"], own="pp. 83–86: Bh. 200,6–201,13"),
         S(533, t=["585c9", "588c9"], own="pp. 225–281: Q5539.zi.21b1–29b1"), S(533, t=["607a23", "608a6"], own="Q5539.zi.76a5–78a3"),
         S(539, t=["827c3", "828c12"], own="p. 157 (Vastu passage)")])
I("ed-harada2004", "2.1.1", "517", "sa-ed", "sa", "partial-edition", "Harada 2004", sub="pratītyasamutpāda; revised Skt text (no MS); Japanese transl.",
  spans=[S(517, bh=["198,13", "203,20"], own="Bh. 198,13–203,20"), S(517, bh=["214,6", "214,14"], own="Bh. 214,6–14")])
I("ed-kajiyama2000", "2.1.1", "516", "sa-ed", "sa", "partial-edition", "Kajiyama 2000", sub="cosmology; English transl. with corrections to Bh.",
  spans=[S(516, bh=["30,21", "44,14"], own="Bh. 30,21–44,14")])
I("ed-delhey2009", "2.1.1", "517", "sa-ed", "sa", "edition", "Delhey 2009", sub="Samāhitā Bhūmiḥ, critical edition; errata online", dn=[DNSA("SA_T06_sambhu")],
  spans=[S(517, sec="b6", own="YoBh MS 63a6–82b6")])
I("ed-delhey2007", "2.1.1 n. 83", "517", "sa-ed", "sa", "study", "Delhey 2007", sub="the avidyā and vicikitsā definitions garbled in Bh.",
  spans=[SEC(517, "b3", note="within Bh. 160–170 (kleśa section)")])
ITEMS[-1]["spans"] = [S(517, bh=["160,10", "170,10"], extent="section-only", note="definitions within the kleśa section (Bh. 160–170)")]
I("ed-delhey2006", "2.1.2; 2.2.3", "517, 534", "sa-ed", "sa", "edition", "Delhey 2006", sub="Asamāhitā Bhūmiḥ (both MSS) pp. 134–136; *Asamāhitabhūmiviniścaya pp. 136–140",
  spans=[S(517, sec="b7", own="pp. 134–136"), S(534, sec="v7", own="pp. 136–140 (Tib./Chin.)")])
I("ed-sg1992a", "2.1.2 n. 87; 2.1.4.1 n. 92", "517–518", "sa-ed", "sa", "partial-edition", "Śrāvakabhūmi Study Group 1992a",
  sub="first editions of the Asamāhitā and of the end of the adhyātmavidyā", spans=[S(517, sec="b7"), S(518, t=["354a23", "356a08"], extent="approx-start")])
I("ed-sg1993", "2.1.4.1 nn. 92–93; 2.1.4.3; 2.1.5", "518, 520", "sa-ed", "sa", "partial-edition", "Śrāvakabhūmi Study Group 1993",
  sub="earlier versions of the Śrutamayī and Cintāmayī editions", spans=[S(518, t=["354a23", "356a12"], extent="approx-start"), S(520, sec=["b10-sabda", "b10-silpa"]), S(520, sec="b11-12")])
I("ed-sg2007-app", "2.1.2–2.1.5", "517–520", "sa-ed", "sa", "edition", "Śrāvakabhūmi Study Group 2007 (appendices)", sub="Asamāhitā, Śrutamayī, Cintāmayī; ŚrBh MS only; Japanese transl.",
  dn=[DNSA("SA_T06_srabhu_u")], spans=[
   S(517, sec="b7", own="pp. 275–280"), S(518, t=["354a06", "356a08"], own="pp. 284–305", note="end of the adhyātmavidyā; 354a6–b17 supplied from the Tibetan by the editors, the Sanskrit MS resumes in §A.I-7"),
   S(518, sec="b10-cik", own="pp. 304–305"), S(520, sec=["b10-sabda", "b10-silpa"], own="pp. 306–313"),
   S(520, sec="b11-12", own="pp. 315–336"), S(520, sec="b11-ag", own="pp. 337–370 (rev. of Maeda 1991)")])
I("ed-sg-srbh", "2.1.7", "521", "sa-ed", "sa", "edition", "Śrāvakabhūmi Study Group 1998, 2007", sub="yogasthānas 1–2, ŚrBh MS; Japanese transl.",
  dn=[DNSA("SA_T06_srabhu_u")], spans=[S(521, sec="b13-ys1", own="1998 = Sh. 1–166"), S(521, sec="b13-ys2", own="2007 = Sh. 167–348")])
I("ed-sg-articles", "2.1.7 n. 113", "521", "sa-ed", "sa", "partial-edition", "Śrāvakabhūmi Study Group 1981–1991, 1994–2006 (articles)",
  sub="earlier editions superseded by the books", spans=[S(521, sec=["b13-ys1", "b13-ys2"], extent="section-only")])
I("ed-sg-ys3", "2.1.7", "522", "sa-ed", "sa", "partial-edition", "Śrāvakabhūmi Study Group 2008, 2009", sub="re-edition of yogasthāna 3 begun",
  spans=[SEC(522, "b13-ys3")])
I("ed-amichay", "2.1.7 n. 116", "522", "sa-ed", "sa", "partial-edition", "Amichay (in preparation, 2007)", sub="critical edition of yogasthāna 3 planned for a Ph.D. thesis",
  spans=[SEC(522, "b13-ys3")])
I("ed-wayman1960", "2.1.3; 2.1.8", "518, 523", "sa-ed", "sa", "edition", "Wayman 1960", sub="ŚrBh MS (superseded)",
  dn=[DNSA("SA_T06_ybh-sacittika")], note="the DharmaNexus e-text SA_T06_ybh-sacittika contains only the Sacittikā/Acittikā part",
  spans=[S(518, sec="b8", own="pp. 378–376"), S(523, sec="b14", own="pp. 376–375")])
I("ed-wayman1984", "2.1.3; 2.1.5", "518, 520", "sa-ed", "sa", "edition", "Wayman 1984", sub="reprints and new editions; English translations",
  spans=[S(518, sec="b8", own="pp. 327–330"), S(520, sec="b11-pg", own="pp. 333–352"), S(520, sec="b11-ag", own="pp. 354–366")])
I("ed-schmit2000", "2.1.1; 2.1.4.1; 2.1.5", "516, 518, 520", "sa-ed", "sa", "partial-edition", "Schmithausen 2000",
  sub="Śrutamayī passage (pp. 246–254), nāstikavāda (pp. 254–259), beginning of the Cintāmayī (pp. 259–263)",
  spans=[S(518, t=["345b4", "345c16"], own="Q5536.184a6–185b6"), S(516, bh=["151,19", "155,5"], own="Bh. 151,19–155,5"),
         SEC(520, "b11-12", own="pp. 259–263", note="beginning of the chapter, both MSS")])
I("ed-wayman1958", "2.1.4.2", "519", "sa-ed", "sa", "study", "Wayman 1958", sub="first citations of the hetuvidyā from a Sanskrit MS", spans=[SEC(519, "b10-hetu")])
for rid, lab, sub, p in [
    ("ed-pandey1986", "Pandey 1986: 334–348", "hetuvidyā on the YoBh MS; Hindi translation", "518, 520"),
    ("ed-yaita1992", "Yaita 1992: 511–546 (Japanese transl. 547–576)", "hetuvidyā, ŚrBh MS (+ Pandey's readings); 'the best'", "518–520"),
    ("ed-yaita2005", "Yaita 2005: 95–124 (transl. 22–41)", "revised hetuvidyā edition", "519–520"),
    ("ed-yaita-takano1995", "Yaita & Takano 1995", "corrections and trilingual index of the hetuvidyā", "518, 520"),
    ("ed-wayman1999", "Wayman 1999: 3–41", "hetuvidyā, ŚrBh MS; English translation", "518–520"),
    ("ed-oberhammer", "Oberhammer 1991–2006", "long hetuvidyā citations with text-critical notes by Schmithausen", "519–520"),
]:
    I(rid, "2.1.4.2", p, "sa-ed", "sa", "partial-edition", lab, sub=sub, spans=[S(518, sec="b10-hetu")],
      dn=[DNSA("SA_T06_ybh-hetuvidya")] if rid == "ed-yaita2005" else None)
I("ed-shukla1991", "2.1.4.2; 2.1.5", "518, 520–521", "sa-ed", "sa", "partial-edition", "Shukla 1991 (appendices)", sub="hetuvidyā; Cintāmayī verses",
  spans=[S(518, sec="b10-hetu", own="App. III, pp. 14–25"), S(520, sec="b11-pg", own="pp. 26–29 (verses only)"),
         SEC(520, "b11-ag", own="pp. 29–31 (partial)"), SEC(521, "b11-sg", own="p. 31 (one verse)")])
I("ed-wayman1961", "2.1.5; 2.1.7", "520–521", "sa-ed", "sa", "partial-edition", "Wayman 1961", sub="Analysis of the ŚrBh MS; passages edited and translated",
  spans=[S(520, sec="b11-pg", own="pp. 163–185"), S(521, sec="b13", extent="selections", note="numerous passages from the whole ŚrBh")])
I("ed-wayman-other", "2.1.7 n. 110", "521", "sa-ed", "sa", "partial-edition", "Wayman 1978: 31–42; 1997: 335–368", sub="further ŚrBh passages; reprint of the āhāra chapter",
  spans=[SEC(521, "b13")])
I("ed-maeda1991", "2.1.5 n. 106", "520", "sa-ed", "sa", "partial-edition", "Maeda 1991", sub="Ābhiprāyikārthagāthā (revised in SG 2007)", spans=[S(520, sec="b11-ag")])
I("ed-enomoto1989", "2.1.5", "520–521", "sa-ed", "sa", "edition", "Enomoto 1989", sub="Śarīrārthagāthā verses, both MSS (commentary unedited)",
  dn=[DNSA("SA_T06_asycsaru")], spans=[S(521, sec="b11-sg")])
I("ed-schmit1970-87a", "2.1.5 n. 107", "521", "sa-ed", "sa", "partial-edition", "Schmithausen 1970: 50–54, 114f.; 1987a: 382–387", sub="some Śarīrārthagāthā verses",
  spans=[SEC(521, "b11-sg")])
I("ed-sugawara1998", "2.1.6", "521", "sa-ed", "sa", "partial-edition", "Sugawara 1998", sub="Sanskrit titles of the main sections of the Bhāvanāmayī (edition in progress)",
  spans=[SEC(521, "b12")])
I("ed-shukla1973", "2.1.7", "521–522", "sa-ed", "sa", "edition", "Shukla 1973 (Sh.)", sub="the only complete ŚrBh edition; omits a folio after Sh. 432,3",
  dn=[DNSA("SA_T06_srabhusu")], spans=[S(521, sec="b13", own="Sh. 1–511")])
I("ed-choi2001", "2.1.7; 1.3", "511, 521–522", "sa-ed", "sa", "partial-edition", "Choi 2001", sub="ŚrBh passages and their Xiǎnyáng lùn parallels; German transl.",
  spans=[S(521, sh=a, own="Sh. %s–%s" % tuple(a)) for a in
         [["14,1", "15,8"], ["37,7", "51,9"], ["58,5", "60,11"], ["190,8", "190,21"], ["263,13", "264,4"], ["265,2", "265,8"],
          ["270,15", "272,23"], ["275,23", "277,23"], ["439,4", "445,12"], ["447,1", "448,1"], ["449,7", "449,10"]]] +
        [SEC(518, "b10-adhy", own="pp. 40–41", note="short citations of the Śrutamayī MS (n. 91)")])
I("ed-maithri1999", "2.1.7; 2.1.9.4", "521–522, 531", "sa-ed", "sa", "partial-edition", "Maithrimurthi 1999", sub="ŚrBh and BoBh passages; German transl.",
  spans=[S(521, sh=["207,7", "210,2"], own="Sh. 207,7–210,2"), S(522, sh=["377,10", "380,15"], own="Sh. 377,10–380,15"),
         S(522, sh=["426,20", "429,9"], own="Sh. 426,20–429,9"),
         S(531, bobhd=["166,1", "170,17"], own="pp. 305–316: BoBhD 166,1–170,17 = BoBhW 241,15–249,6")])
I("ed-jost1990", "2.1.7", "522", "sa-ed", "sa", "partial-edition", "Jost 1990 (unpublished)", spans=[S(522, sh=["291,5", "307,5"], own="Sh. 291,5–307,5")])
I("ed-schmit1982b", "2.1.7 nn. 116, 119", "522", "sa-ed", "sa", "study", "Schmithausen 1982b", sub="text-critical notes on yogasthānas 3 and 4",
  spans=[SEC(522, "b13-ys3"), SEC(522, ["b13-ys4a", "b13-ys4b"])])
I("ed-kimura1992", "2.1.7", "522", "sa-ed", "sa", "partial-edition", "Kimura 1992", sub="editio princeps of the folio omitted by Shukla",
  spans=[S(522, sh=["432,3", "432,4"], own="after Sh. 432,3", extent="point")])
I("ed-deleanu2006", "2.1.7", "522", "sa-ed", "sa", "edition", "Deleanu 2006", sub="laukikamārga: diplomatic and critical Skt, Tib., Chin.; English transl.",
  dn=[DNSA("SA_T06_ybh-laukikamarga")], spans=[S(522, sh=["437,1", "470,6"], own="Sh. 437–470,6")])
I("ed-schmit1982a", "2.1.7", "522", "sa-ed", "sa", "partial-edition", "Schmithausen 1982a", sub="last pages of the ŚrBh", spans=[S(522, sh=["506,10", "511,6"], own="Sh. 506,10–511,6")])
I("ed-vonrospatt1995", "2.1.7 n. 119; 2.2.1.2 n. 177", "522, 533", "sa-ed", "sa", "partial-edition", "von Rospatt 1995: 219–248", sub="cites and emends ŚrBh passages; cites the Viniścaya fragment",
  spans=[S(522, sh=["475,1", "489,24"], own="Sh. 475–489"), SEC(533, "v1", note="passages of the St Petersburg fragment (see his index)")])
I("ed-yonezawa1998", "2.1.8", "523", "sa-ed", "sa", "edition", "Yonezawa 1998", sub="Pratyekabuddhabhūmi, ŚrBh MS; English transl. pp. 19–25", dn=[DNSA("SA_T06_ybh-pratyekabuddha")], spans=[S(523, sec="b14")])
I("ed-pandey1987", "2.1.8", "523", "sa-ed", "sa", "edition", "Pandey 1987", sub="Pratyekabuddhabhūmi, YoBh MS (or transcript?)", spans=[S(523, sec="b14")])
I("ed-pandey2009", "2.1.8 n. 124", "523", "sa-ed", "sa", "partial-edition", "Pandey 2009 (not seen by Delhey)", sub="possibly a new edition/translation of the Pratyekabuddhabhūmi",
  spans=[SEC(523, "b14")])
I("ed-wayman1997", "2.1.8", "523", "sa-ed", "sa", "edition", "Wayman 1997: 191–196", sub="Pratyekabuddhabhūmi (= 1960) with English transl.", spans=[S(523, sec="b14")])
I("ed-wogihara", "2.1.9.1", "525–526", "sa-ed", "sa", "edition", "Wogihara 1930–1936 (BoBhW)", sub="Cambridge + Kyoto MSS; editio princeps; lacks the beginning of I.1",
  dn=[DNSA("SA_T06_Asaṅga_Bodhisattvabhūmi"), DNSA("SA_T06_Asaṅga_Bodhisattvabhūmi-wogiwara")], spans=[S(525, sec="b15")])
I("ed-dutt1966", "2.1.9.1", "525–526", "sa-ed", "sa", "edition", "Dutt 1966 (BoBhD)", sub="mainly the Patna MS; 'rather mediocre'", dn=[DNSA("SA_T06_bsa034")],
  spans=[S(525, sec="b15")])
I("ed-hadano1975", "2.1.9.1 n. 161", "525, 530", "sa-ed", "sa", "edition", "Hadano 1975 (unofficial)", sub="preliminary synoptic edition of the whole BoBh",
  spans=[S(525, sec="b15")])
I("ed-rahder1926", "2.1.9.1 n. 137", "525", "sa-ed", "sa", "partial-edition", "Rahder 1926a, 1926b", sub="Vihāra- and Bhūmipaṭala from Wogihara's transcript",
  spans=[S(525, sec="bb-II.4"), S(525, sec="bb-III.3")])
I("ed-roth", "2.1.9.2", "527", "sa-ed", "sa", "partial-edition", "Roth 1975–1976", sub="beginning of I.1 (Patna MS); English transl.",
  spans=[S(527, bobhd=["1,1", "2,3"], own="BoBhD 1,1–2,3")])
for rid, lab, sub, sec, p in [
    ("ed-wangchuk2007-bobh", "Wangchuk 2007 (BoBh)", "Cittotpādapaṭala: Skt and Tib. critical editions", "bb-I.2", "527"),
    ("ed-takahashi2005", "Takahashi 2005a: 83–117", "Tattvārthapaṭala on all four MSS; Japanese transl.", "bb-I.4", "526–527"),
    ("ed-yaita2010", "Yaita 2010", "Prabhāvapaṭala: new critical edition and translation", "bb-I.5", "527"),
    ("ed-nakamura2004", "Nakamura 2004 (unpublished M.A.)", "Bodhipaṭala; German transl.", "bb-I.7", "527"),
    ("ed-leumann1931", "Leumann 1931", "Balagotrapaṭala (= BoBhW 95,1–110,13, re-presented)", "bb-I.8", "527–528"),
    ("ed-yaita2008", "Yaita 2008", "Dānapaṭala: critical edition and Japanese transl.", "bb-I.9", "528"),
    ("ed-hadano1993", "Hadano et al. 1993", "Śīlapaṭala, synoptic (Skt, Tib., 3 Chinese, *Sāgaramegha)", "bb-I.10", "530"),
    ("ed-markert2005", "Markert-Braham 2005 (M.A.)", "Kṣāntipaṭala: edition and translation", "bb-I.11", "531"),
    ("ed-furusaka2007", "Furusaka 2007", "synoptic edition of I.18", "bb-I.18", "531"),
]:
    I(rid, "2.1.9.2–4", p, "sa-ed", "sa", "partial-edition", lab, sub=sub, spans=[S(int(p.split("–")[0].split(",")[0]), sec=sec)])
I("ed-isoda1995", "2.1.9.4", "531", "sa-ed", "sa", "partial-edition", "Isoda & Furusaka 1995", sub="synoptic edition of yogasthānas II–IV",
  spans=[S(531, t=["549b17", "576b29"], own="BoBh II–IV")])
I("ed-lvp1928", "2.1.9.1 n. 137", "525", "sa-ed", "sa", "partial-edition", "de La Vallée Poussin 1928", sub="quotes Tattvārtha passages from Wogihara's transcript",
  spans=[SEC(525, "bb-I.4", own="BoBhW 45,22–48,13; 48,23–50,7")])
I("ed-dutt1931", "2.1.9.3", "528–529", "sa-ed", "sa", "parallel", "Dutt 1931 (Bodhisattvaprātimokṣasūtra)", sub="first part agrees almost literally with the Śīlapaṭala",
  dn=[DNSA("SA_K01_bsu011_u")], spans=[S(529, bobhd=["105,1", "106,30"], own="BoBhW 152–155 = BoBhD 105–106; Dutt 1931: 269–277")])
I("ed-schmit1991", "2.1.10", "532", "sa-ed", "sa", "edition", "Schmithausen 1991", sub="Sopadhikā and Nirupadhikā Bhūmiḥ (YoBh MS)", dn=[DNSA("SA_T06_ybh-sopadhika")], spans=[S(532, sec=["b16", "b17"])])
I("ed-schmit1969b-ms", "2.1.10 n. 172", "532", "sa-ed", "sa", "study", "Schmithausen 1969b (MS citations)", sub="passages of the Sopadhikā/Nirupadhikā cited from the MS",
  spans=[SEC(532, ["b16", "b17"])])
I("ed-matsuda1994", "2.4", "539", "sa-ed", "sa", "edition", "Matsuda 1994", sub="Paryāya folio: diplomatic and critical edition", dn=[DNSA("SA_T06_ybh-paryaya")], spans=[S(539, t=["768c20", "769c9"])])
I("ed-matsuda1995", "2.2.5.3", "535", "sa-ed", "sa", "edition", "Matsuda 1995", sub="Viniścaya folio: facsimile; Saṃdh IX part edited, Japanese transl.",
  spans=[S(535, t=["728c16", "730b21"], note="only the part belonging to Saṃdh IX is edited (sub-range not given)")])
I("ed-matsuda1988", "1.2 n. 44; 2.2.1.2", "510, 533", "sa-ed", "sa", "study", "Matsuda 1988", sub="report on the St Petersburg Viniścaya fragment; passages cited",
  spans=[S(533, t=["589b19", "600c10"], extent="selections")])
I("ed-kritzer2005", "2.0 n. 63; 2.2.1.2; 2.5", "512, 533, 540", "sa-ed", "sa", "study", "Kritzer 2005", sub="passages from all over the YoBh (Tib., Chin., Skt where extant)",
  spans=[WHOLE(512, note="numerous passages from all over the YoBh"), SEC(533, "v1", own="pp. 5, 187, 189", note="cites the St Petersburg fragment"),
         S(540, sec="vs-vinaya", own="pp. XVIf.", extent="section-only", note="Vinaya verses / end of the prose")])
I("ed-sakuma1996", "2.2.1.1 n. 175", "532", "sa-ed", "sa", "study", "Sakuma 1996: 7–8", sub="corrections to the Sanskrit of the ASBh citation",
  spans=[S(532, t=["579a14", "579c22"])])

# ---------------------------------------------------------------- Tibetan translation & witnesses
I("bo-d4035", "2.1.1", "503, 515", "bo", "bo", "translation", "D4035 / Q5536 Sa'i dngos gzhi", sub="Basic Section without ŚrBh and BoBh",
  dn=[DNBO("BO_T06_D4035")], spans=[S(515, t=["279a08", "395c08"]), S(515, sec="b14"), S(515, sec=["b16", "b17"])])
I("bo-d4036", "2.1.7", "521", "bo", "bo", "translation", "D4036 / Q5537 Nyan thos kyi sa", sub="Śrāvakabhūmi", dn=[DNBO("BO_T06_D4036")], spans=[S(521, sec="b13")])
I("bo-d4037", "2.1.9.1", "524, 531", "bo", "bo", "translation", "D4037 / Q5538 Byang chub sems dpa'i sa", sub="Bodhisattvabhūmi (Anukramapaṭala after a colophon)",
  dn=[DNBO("BO_T06_D4037")], spans=[S(524, sec="b15")])
I("bo-d4038", "2.2.0", "532", "bo", "bo", "translation", "D4038 / Q5539 Rnam par gtan la dbab pa bsdu ba", sub="Viniścayasaṃgrahaṇī",
  dn=[DNBO("BO_T06_D4038"), DNBO("BO_T06_D4038-2")], spans=[S(532, sec="vin")])
I("bo-d4039", "2.5", "539", "bo", "bo", "translation", "D4039 / Q5540 Gzhi bsdu ba", sub="Vastusaṃgrahaṇī, sūtra part", dn=[DNBO("BO_T06_D4039")],
  spans=[S(539, t=["772b", "868b"], own="Q5540 = D4039 = T1579.772b–868b")])
I("bo-d4040", "2.5", "540", "bo", "bo", "translation", "D4040 / Q5541 *Vinayasaṃgrahaṇī", sub="opening verses (Q5541.1a1–5a8) without Chinese counterpart",
  dn=[DNBO("BO_T06_D4040")], spans=[S(540, t=["868b", "877c1"], note="T1579.877c2–17 only a short remark; 877c18–878a24 missing")])
I("bo-d4041", "2.4", "539", "bo", "bo", "translation", "D4041 / Q5542 Rnam grangs bsdu ba", sub="Paryāyasaṃgrahaṇī", dn=[DNBO("BO_T06_D4041")], spans=[S(539, sec="pary")])
I("bo-d4042", "2.3", "539", "bo", "bo", "translation", "D4042 / Q5543 Rnam par bshad pa bsdu ba", sub="*Vyākhyāsaṃgrahaṇī", dn=[DNBO("BO_T06_D4042")], spans=[S(539, sec="vyakh")])
I("bo-witnesses", "1.1 n. 30", "507", "bo", "bo", "witnesses", "Tibetan witnesses: Peking Q5536–5543, Narthang, Ganden G3535–3542 | Derge, Cone",
  sub="two groups of bstan 'gyur witnesses (Deleanu 2006: 78ff.; Kramer 2005: 67; Wangchuk 2007: 381)", spans=[WHOLE(507)])
I("bo-zt", "2.0", "512–513", "bo", "bo", "edition", "Zhōnghuá bstan 'gyur (ZT)", sub="collated Tibetan text; 'by no means a critical one'", spans=[WHOLE(512)])
I("bo-beijing-bobh", "2.1.9.1 n. 129", "524", "bo", "bo", "edition", "Beijing separate edition of the Tibetan BoBh", sub="'no historical and philological value' (Wangchuk 2007: 380 n. 12)",
  spans=[S(524, sec="b15")])
I("bo-dunhuang", "1.1 n. 30", "507", "bo", "bo", "manuscript", "Tibetan Dūnhuáng fragments: Fujita 1979; Hakamaya 1985: 220–224; Ishikawa 1992, 1993, 1994",
  sub="locations not given by Delhey", spans=[], note="not localised")
I("bo-dunhuang-srbh", "1.1 n. 30", "507", "bo", "bo", "manuscript", "Dūnhuáng fragments of the Tibetan Śrāvakabhūmi (Deleanu 2006: 77f.)", spans=[SEC(507, "b13")])
I("bo-mongolian", "1.1 n. 31; 2.2.6", "507, 538", "bo", "multi", "translation", "Mongolian translation (from the Tibetan)", sub="collated by Schmithausen 1969b for the nirvāṇa chapter",
  spans=[WHOLE(507), S(538, sec="v16", note="used in Schmithausen 1969b")])

# ---------------------------------------------------------------- editions & studies of the Tibetan / Chinese text
TE = "te"
I("te-hakamaya1978", "2.2.1.1", "532", TE, "bo", "edition", "Hakamaya 1978", sub="ASBh citation edited with Tib. and Chin.; Japanese transl.",
  spans=[S(532, t=["579a14", "579c22"], own="Q5539.zi.2b2–4a4")])
I("te-hakamaya1979", "2.2.1.1", "532", TE, "bo", "edition", "Hakamaya 1979", sub="synoptic critical Tib./Chin. of the rest of the ālayavijñāna treatise; Japanese transl.",
  spans=[S(532, t=["579c23", "582a12"], own="Q5539.zi.4a5–10b6")])
I("te-ui1930", "2.2.1.1", "532", TE, "zh", "edition", "Ui 1930: 543–707", sub="synoptic edition of T1579 and Paramārtha's T1584",
  spans=[S(532, t=["579a", "601a"], own="Q5539.zi.1a1–60b7")])
I("te-sakuma1990", "2.2.1–2.5", "532–540", TE, "bo", "edition", "Sakuma 1990 (Tibetan/Chinese passages)", sub="tiny passages, edited and translated into German",
  spans=[S(532, t=["581b22", "581b29"], own="pp. 155–161: Q5539.zi.9a3f.", note="end not given"),
   S(532, t=["581c3", "581c22"], own="Q5539.zi.9a8–10a3"), S(533, t=["589a9", "589b2"], own="pp. 161–165: Q5539.zi.30a5–30b7"),
   S(533, t=["621a26", "630a5"], own="pp. 165–171", extent="section-only", note="two small portions of the kleśa sections"),
   S(533, t=["635c6", "635c11"], own="pp. 171–173: Q5539.zi.152a4–6"),
   S(534, t=["669a8", "669a21"], own="pp. 173–182: Q5539.zi.236b1–237a1"), S(534, t=["669a29", "669b3"], own="Q5539.zi.237a4–5"),
   S(534, t=["671b14", "671b21"], own="Q5539.zi.242b8–243a5"), S(534, t=["676b9", "676b16"], own="Q5539.zi.255a7–255b2"),
   S(535, t=["695c26", "703a25"], own="pp. 183–190", extent="section-only", note="a small section of the vastu part (n. 180)"),
   S(535, t=["707a5", "707b23"], own="pp. 190–201: Q5539.'i.30a6–31b5"), S(535, t=["733c19", "733c24"], own="pp. 201–203: Q5539.'i.100b8–101a4"),
   S(538, t=["746c14", "746c18"], own="pp. 203–204: Q5539.'i.134b8–135a1"),
   S(540, t=["802a5", "802a12"], own="pp. 204–208: Q5540.221a2–5"), S(540, t=["839a25", "839b4"], own="Q5540.312b2–5")])
I("te-ahn2003", "2.2.1.2; 2.2.2", "533", TE, "bo", "edition", "Ahn 2003 (Tibetan)", sub="kleśa sections of the Viniścaya; German transl.",
  spans=[S(533, t=["602a9", "604b9"], own="pp. 88–95: Q5539.zi.65a3–68b7"), S(533, t=["621a26", "630a5"], own="pp. 96–155: Q5539.zi.112b2–137b1")])
I("te-jan1984", "2.2.2", "533–534", TE, "zh", "study", "Jan 1984", sub="summary and partial translation of the royal-code section (Chinese)",
  spans=[S(533, t=["638a19", "644a6"], extent="selections")])
I("te-zimmermann2006", "2.2.2", "533", TE, "zh", "study", "Zimmermann 2006: 230 n. 52", sub="T1579 vs T1615: minor variants", spans=[S(533, t=["638a19", "644a6"], extent="section-only")])
I("te-maeda2007", "2.2.2", "534", TE, "bo", "edition", "Maeda 2007", sub="partial critical Tib. edition of the royal-code section; Japanese transl.; T1615 and T524",
  spans=[S(534, t=["638a19", "644a6"], extent="section-only")])
I("te-maeda2005", "2.2.2 n. 179", "534", TE, "zh", "study", "Maeda 2005 (not seen by Delhey)", sub="on the same section", spans=[S(534, t=["638a19", "644a6"], extent="section-only")])
I("te-delhey2006", "2.2.3", "534", TE, "bo", "edition", "Delhey 2006: 136–140", sub="*Asamāhitabhūmiviniścaya, synoptic; German transl. pp. 144–150", spans=[S(534, sec="v7")])
I("te-wangchuk2007", "2.2.5.0; 2.2.5.4", "534, 538", TE, "bo", "edition", "Wangchuk 2007 (Viniścaya)", sub="two passages of the *Bodhisattvabhūmiviniścaya",
  spans=[S(534, q={"text": "Q5539", "from": "zi300a7", "to": "zi300b8"}, own="pp. 263–266: Q5539.zi.300a7–300b8", note="interpolated between Delhey's Q–T anchors"),
         S(538, q={"text": "Q5539", "from": "'i127b3", "to": "'i129b2"}, own="pp. 140–142: Q5539.'i.127b3–129b2", note="interpolated between Delhey's Q–T anchors")])
I("te-kramer2005", "2.2.5.1", "535", TE, "bo", "edition", "Kramer 2005", sub="five vastus: Tibetan on all five witnesses; German transl.",
  spans=[S(535, t=["695c26", "703a25"], own="Q5539.zi.302b1–'i.19b6")])
I("te-willis1976", "2.2.5.1", "535", TE, "bo", "edition", "Willis 1976: 186–257", sub="selected passages of part 2 of the *Tattvārthapaṭalaviniścaya",
  spans=[S(535, t=["703a25", "707a5"], extent="approx-end", note="end of part 2 not given")])
I("te-takahashi2005", "2.2.5.1", "535", TE, "bo", "edition", "Takahashi 2005a: 119–149 (transl. 181–212)", sub="selected passages of both parts",
  spans=[S(535, t=["695c26", "707a5"], extent="selections")])
I("te-tatz-tsongkhapa", "2.2.5.2", "535", TE, "bo", "study", "Tatz 1986: 132–136 (Tsong kha pa's citation)", sub="relatively long section cited by Tsong kha pa; translation",
  spans=[S(535, t=["710c29", "712a17"], own="Q5539.'i.40a1–43a5")])
I("te-saṃdh-yoshimura", "2.2.5.3", "536", TE, "bo", "edition", "Saṃdh editions: Lamotte 1935; Nozawa 1957 (ch. VIII); Yoshimura 1959 (VIII, Tib./Chin.); Powers 1995; Hakamaya 1984–1987, 2008 (Dūnhuáng Tib.)",
  sub="editions of the independent sūtra, relevant to its citation", spans=[S(536, t=["713c28", "736c12"], extent="section-only")])
I("te-saṃdh-recensions", "2.2.5.3", "536–537", TE, "bo", "study", "Powers 1993b; Kato 2006; Schmithausen 1984", sub="recensions of the Tibetan Saṃdh; text-critical problems",
  spans=[S(536, t=["713c28", "736c12"], extent="section-only")])
I("te-schmit1969b", "2.2.6", "538", TE, "bo", "edition", "Schmithausen 1969b", sub="nirvāṇa chapter: Tibetan (4 witnesses + Mongolian); German transl.; uses T1828",
  spans=[S(538, sec="v16")])
I("te-silk2009", "2.2.5.4 n. 198", "538", TE, "bo", "study", "Silk 2009; Potter 2003: 526–532", sub="Kāśyapaparivarta-related section; correspondence tables",
  spans=[S(538, t=["738c28", "747b25"])])
I("te-schmit1969a", "2.2.0 n. 173; 0.4", "502, 532", TE, "multi", "study", "Schmithausen 1969a: 812–823; 1969b: 17–37", sub="structure and literary history of the Viniścaya",
  spans=[SEC(532, "vin")])
I("te-mukai1985", "2.5", "539–540", TE, "bo", "study", "Mukai 1985", sub="concordance of Peking, Derge, Taishō and the Saṃyuktāgama (pp. 27–41); the mātṛkā problem (pp. 4–8)",
  spans=[S(539, sec="vs-sutra", own="pp. 27–41"), S(540, sec="vs-matrka", own="pp. 4–8")])
I("te-mukai1996", "2.3; 2.4", "539", TE, "bo", "study", "Mukai 1996", sub="synopses of the *Vyākhyā- (pp. 575–573) and Paryāyasaṃgrahaṇī (pp. 572–569)",
  spans=[S(539, sec="vyakh"), S(539, sec="pary")])
I("te-horiuchi2008", "2.3", "539", TE, "bo", "study", "Horiuchi 2008: 1130 n. 3", sub="desideratum: comparison with the Vyākhyāyukti", spans=[SEC(539, "vyakh")])
I("te-kwon2003", "2.1.6 n. 109", "521", TE, "bo", "edition", "Kwon 2003 (Ph.D.)", sub="critical/collated Tib. and Chin. of the Bhāvanāmayī; Japanese transl.",
  spans=[S(521, sec="b12")])
I("te-sugawara2013", "2.1.6", "521", TE, "sa", "study", "Sugawara 2013; von Rospatt 2013 (same volume)", sub="on the Bhāvanāmayī Bhūmi", spans=[S(521, sec="b12")])
I("te-deleanu-zh", "1.1 n. 29", "507", TE, "zh", "study", "Deleanu 2006: 106–146", sub="production and textual witnesses of the Chinese translation; editions other than Taishō",
  spans=[WHOLE(507)])
I("te-taisho", "2.0", "512", TE, "zh", "edition", "Taishō edition of T1579", sub="variant readings, not of the highest text-critical standard (Yuyama 1994)", spans=[WHOLE(512)])
I("te-sueki1980", "2.1.9.1 n. 133", "525", TE, "zh", "study", "Sueki 1980", sub="peculiarities of Guṇavarman's BoBh translation", spans=[SEC(525, "b15")])
I("te-chen2004", "2.1.9.1 n. 130", "524", TE, "zh", "study", "Chen 2004", sub="date of Dharmakṣema's translations (422–431)", spans=[SEC(524, "b15")])
I("te-demieville1957", "2.1.9.1; 2.1.9.4", "524–525, 531", TE, "zh", "study", "Demiéville 1957", sub="on the three Chinese BoBh translations; French transl. of the Dhyānapaṭala",
  spans=[SEC(524, "b15"), S(531, sec="bb-I.13")])
I("te-lunglien", "2.1.9.3 n. 150", "528", TE, "zh", "study", "Lung-Lien 1972; Hôbôgirin fasc. 2: 142–146", sub="the Chinese Śīlapaṭala texts", spans=[S(528, sec="bb-I.10")])
I("te-kritzer-vinaya", "2.5", "540", TE, "bo", "study", "Kritzer 2005: XVIf.; Deleanu 2006: 46f.", sub="Tibetan vs Chinese Vinaya part",
  spans=[S(540, sec="vs-vinaya")])

# ---------------------------------------------------------------- Chinese
I("zh-t1579", "1.1", "507", "zh", "zh", "translation", "T1579 Yúqié shīdì lùn 瑜伽師地論", sub="Xuánzàng's bureau, complete (the axis of this map)",
  dn=[DNZH("ZH_T30_1579")], spans=[S(507, t=["279a08", "882a12"])])
I("zh-t1581", "2.1.9.1", "524", "zh", "zh", "translation", "T1581 Púsà dìchí jīng 菩薩地持經", sub="Dharmakṣema; whole BoBh, without the Anukramapaṭala",
  dn=[DNZH("ZH_T30_1581")], spans=[S(524, sec="b15")])
I("zh-t1582", "2.1.9.1", "524", "zh", "zh", "translation", "T1582 Púsà shànjiè jīng 菩薩善戒經", sub="Guṇavarman, 431; sūtra format; without the Anukramapaṭala",
  dn=[DNZH("ZH_T30_1582")], spans=[S(524, sec="b15", note="the part from BoBhD 105,4 onwards is transmitted separately as T1583")])
I("zh-t1583", "2.1.9.1 n. 131; 2.1.9.3", "524, 528", "zh", "zh", "translation", "T1583 Púsà shànjiè jīng 菩薩善戒經 (Śīla part)", sub="extracted from T1582",
  dn=[DNZH("ZH_T30_1583")], spans=[S(524, bobhd=["105,4", "106,30"], own="from BoBhD 105,4 = BoBhW 152,18", extent="approx-end", note="Delhey gives only the starting point")])
I("zh-python1973", "2.1.9.1 n. 133", "525", "zh", "zh", "study", "Python 1973: 141–153", sub="French transl. of the sūtra-style introduction of T1582", spans=[SEC(525, "bb-I.1")])
I("zh-t1499", "2.1.9.3", "528", "zh", "zh", "extract", "T1499 Púsà jiè jiémó wén 菩薩戒羯磨文", dn=[DNZH("ZH_T24_1499")], spans=[S(528, t=["514b14", "515c28"])])
I("zh-t1501", "2.1.9.3", "528", "zh", "zh", "extract", "T1501 Púsà jièběn 菩薩戒本 (Xuánzàng)", dn=[DNZH("ZH_T24_1501")],
  spans=[S(528, t=["515a17", "515a22"]), S(528, t=["515b21", "521a16"])])
I("zh-t1500", "2.1.9.3", "528", "zh", "zh", "extract", "T1500 Púsà jièběn 菩薩戒本 (Dharmakṣema)", sub="= T1581.913b–917a", dn=[DNZH("ZH_T24_1500")],
  spans=[SEC(528, "bb-I.10", own="T1581.913b–917a")])
I("zh-t1503", "2.1.9.3", "528", "zh", "zh", "extract", "T1503 Yōupósè wǔjiè wēiyí jīng 優婆塞五戒威儀經", sub="ascribed to Guṇavarman (contested)", dn=[DNZH("ZH_T24_1503")],
  spans=[S(528, t=["515b", "521a"], own="T1503.1116c–1119b")])
I("zh-t1584", "2.2.1.1", "532", "zh", "zh", "translation", "T1584 Juédìngzàng lùn 決定藏論", sub="Paramārtha, 6th c.", dn=[DNZH("ZH_T30_1584")],
  spans=[S(532, t=["579a", "601a"], own="Q5539.zi.1a1–60b7")])
I("zh-t1615", "2.2.2", "533", "zh", "zh", "extract", "T1615 Wángfǎ zhènglǐ lùn 王法正理論", sub="attributed to Xuánzàng (649?)", dn=[DNZH("ZH_T31_1615")],
  spans=[S(533, t=["638a19", "642a5"]), S(533, t=["642b20", "644a6"])], note="omits T1579.642a6–b19")
I("zh-t524", "2.2.2", "534", "zh", "zh", "extract", "T524 Fó wéi Yōutián wáng shuō wáng fǎzhèng lùn jīng 佛為優填王說王法政論經", sub="attributed to Amoghavajra; Tantric additions",
  dn=[DNZH("ZH_T14_0524")], spans=[S(534, t=["638a19", "642a5"])])
I("zh-saptadasa", "1.1 n. 29", "507", "zh", "zh", "translation", "Paramārtha's *Saptadaśabhūmiśāstra (lost)", sub="Deleanu 2006: 196–201", spans=[],
  note="not localised: lost translation")
I("zh-kundoku", "1.1 n. 31; 2.0", "507, 513, 515", "zh", "ja", "translation", "Japanese kundoku of T1579 (Katō Seishin 1930–1935)", sub="with tables of contents",
  spans=[WHOLE(507)])
I("zh-uighur", "1.1 n. 31", "507", "zh", "multi", "translation", "Uighur translation (von Gabain 1961, 1963)", sub="probably secondary, from the Chinese; whereabouts unknown",
  spans=[], note="not localised")

# ---------------------------------------------------------------- commentaries & related
I("rel-d4043", "1.4; 2.3", "511, 539", "rel", "bo", "commentary", "*Yogācārabhūmivyākhyā (D4043 / Q5544)", sub="Indian commentary (torso)",
  dn=[DNBO("BO_T06_D4043")], note="Delhey cites it as 'Q5543, D4042' (the numbers of the *Vyākhyāsaṃgrahaṇī).",
  spans=[S(511, bh=["3,1", "137,22"], own="up to Bh. 137 (n. 58)", note="stops in the commentary on the Savitarkādibhūmi")])
I("rel-t1580", "1.4", "511", "rel", "zh", "commentary", "T1580 Yúqiéshīdìlùn shì 瑜伽師地論釋", sub="corresponds to the introductory section of the *Vyākhyā",
  dn=[DNZH("ZH_T30_1580")], spans=[S(511, t=["279a08", "279a08"], extent="point")])
I("rel-mukai1979", "1.4 n. 59", "511", "rel", "zh", "study", "Mukai 1979: 42; Silk 1997: 240 n. 44", sub="T1580 and the *Vyākhyā compared", spans=[S(511, t=["279a08", "279a08"], extent="point")])
I("rel-lost-comm", "1.4", "512", "rel", "multi", "commentary", "Lost Indian commentaries (Yūki 1962: 61–77; Deleanu 2006: 249f., 263f.)", spans=[],
  note="not localised")
I("rel-t1602", "1.3; 2.1.4.2; 2.1.7", "511, 518, 522", "rel", "zh", "related", "T1602 Xiǎnyáng shèngjiào lùn 顯揚聖教論", sub="largely quotations from the YoBh",
  dn=[DNZH("ZH_T31_1602")], spans=[S(522, sh=["475,1", "489,24"], own="T1602.548c18–549b21 ≈ Sh. 475–489"),
                                   SEC(518, "b10-hetu", note="cites the hetuvidyā"), SEC(521, "b13", note="parallels of ŚrBh sections (Choi 2001, 2002)")])
I("rel-hayashima-mori", "1.3 n. 52", "511", "rel", "zh", "index", "Hayashima & Mōri 1990: 54–68; Hayashima 1997; Choi 2001", sub="concordance and bibliography of the YoBh–Xiǎnyáng lùn parallels",
  spans=[WHOLE(511)])
I("rel-samdh", "2.2.5.3", "535–537", "rel", "multi", "related", "Saṃdhinirmocanasūtra (independent: D106/Q774; T675–679)", sub="the Viniścaya quotes nearly all of it",
  dn=[DNBO("BO_K10_D0106"), DNZH("ZH_T16_0676"), DNZH("ZH_T16_0675"), DNZH("ZH_T16_0677"), DNZH("ZH_T16_0678"), DNZH("ZH_T16_0679")],
  spans=[S(535, t=["713c28", "736c12"], own="Q5539.'i.47b7–108b8")])
I("rel-samdh-comm", "2.2.5.3", "537–538", "rel", "bo", "commentary", "Saṃdh commentaries: D3981 (Asaṅga?); D4033 Jñānagarbha (VIII); D4016 Woncheuk; D4358",
  sub="eds./transls. Lamotte 1935, Powers 1992a, 1998, Nozawa 1957; Steinkellner 1989", dn=[DNBO("BO_T05_D3981"), DNBO("BO_T06_D4033"), DNBO("BO_T05_D4016")],
  spans=[S(537, t=["713c28", "736c12"], extent="section-only")])
I("rel-kp", "2.2.5.4", "538", "rel", "multi", "related", "Kāśyapaparivarta commentary ascribed to Sthiramati (D4009, T1523)", dn=[DNBO("BO_T05_D4009"), DNZH("ZH_T26_1523")],
  spans=[S(538, t=["738c28", "747b25"], own="Q5539.'i.115a1–136b7")])
I("rel-t1828", "2.2.6", "538", "rel", "zh", "commentary", "T1828 Yújiālùn jì 瑜伽論記 (East Asian commentary)", sub="used by Schmithausen 1969b for the nirvāṇa chapter",
  dn=[DNZH("ZH_T42_1828")], spans=[SEC(538, "v16", note="Delhey mentions it only for this chapter")])
I("rel-d4044", "2.1.9.1", "525, 529", "rel", "bo", "commentary", "D4044 / Q5545 Guṇaprabha, BoBh commentary", sub="Gotra- to Dānapaṭala", dn=[DNBO("BO_T06_D4044")],
  spans=[S(529, t=["478b12", "510c08"], own="I.1–I.9")])
I("rel-d4047", "2.1.9.1", "525, 529–531", "rel", "bo", "commentary", "D4047 / Q5548 *Sāgaramegha, BoBh commentary", sub="complete; cites the Anukramapaṭala without comment",
  dn=[DNBO("BO_T06_D4047")], spans=[S(525, sec="b15")])
I("rel-d4045", "2.1.9.3", "529", "rel", "bo", "commentary", "D4045 / Q5546 Guṇaprabha, Śīlapaṭala commentary", dn=[DNBO("BO_T06_D4045")], spans=[S(529, sec="bb-I.10")])
I("rel-d4046", "2.1.9.3", "529", "rel", "bo", "commentary", "D4046 / Q5547 Jinaputra, Śīlapaṭala commentary", sub="= the section in *Sāgaramegha", dn=[DNBO("BO_T06_D4046")],
  spans=[S(529, sec="bb-I.10")])
I("rel-candragomin", "2.1.9.3", "529", "rel", "bo", "related", "Candragomin, Bodhisattvasaṃvaraviṃśikā (D4081)", sub="eds. Tatz 1978, Fujita 2002; transl. Tatz 1978, 1983, 1985; Skt verses (Kanō 2009a/b)",
  dn=[DNBO("BO_T06_D4081"), DNSA("SA_T01_Candragomin_Bodhisattvasaṃvaraviṃśikā-Skt-verses-available-in-testimonia-thus-far_Li_2015")],
  spans=[SEC(529, "bb-I.10")])
I("rel-santaraksita", "2.1.9.3", "529", "rel", "bo", "commentary", "Śāntarakṣita on the Saṃvaraviṃśikā (D4082)", sub="Skt folio (Kanō 2009); eds. Tatz 1978, Fujita 2002",
  dn=[DNBO("BO_T06_D4082")], spans=[SEC(529, "bb-I.10")])
I("rel-bodhibhadra", "2.1.9.3", "529", "rel", "bo", "commentary", "Bodhibhadra on the Saṃvaraviṃśikā (D4083)", sub="ed. Fujita 2002", dn=[DNBO("BO_T06_D4083")],
  spans=[SEC(529, "bb-I.10")])
I("rel-zambasta", "2.1.9.3", "529", "rel", "kho", "related", "Book of Zambasta (Khotanese) – Śīlapaṭala paraphrase", sub="Leumann 1933–1936: 144–164; Emmerick 1968: 164–185; 1990; 1992",
  spans=[SEC(529, "bb-I.10")])
I("rel-vyakhyayukti", "2.3", "539", "rel", "bo", "related", "Vasubandhu, Vyākhyāyukti (D4061; ed. Lee 2001)", sub="later counterpart of the *Vyākhyāsaṃgrahaṇī",
  dn=[DNBO("BO_T06_D4061")], spans=[SEC(539, "vyakh")])

# ---------------------------------------------------------------- reference works
RF = "ref"
for rid, lab, sub, p in [
  ("ref-yuki1962", "Yūki 1962", "catalogue of Yogācāra literature (extant and lost); partial Chinese translations (p. 61)", "498, 507"),
  ("ref-hakamaya-notes", "Hakamaya, notes (Tokyo sDe dge sems tsam ed.)", "bibliographical notes up to c. 1980", "499"),
  ("ref-sugawara1990", "Sugawara 1990: 318–329", "survey of sources and editions", "499"),
  ("ref-silk2001", "Silk 2001: 150–168", "list of Sanskrit editions; reference works", "499, 513"),
  ("ref-nakamura1980", "Nakamura 1980: 256–258", "bibliographical survey (use with caution)", "499"),
  ("ref-powers1991", "Powers 1991", "Yogācāra bibliography (many errors)", "499"),
  ("ref-pfandt1986", "Pfandt 1986", "translations into Western languages", "499"),
  ("ref-potter", "Potter, EIP bibliography; Potter 1999: 398–433", "bibliography and summary", "499, 515"),
  ("ref-hakamaya1982", "Hakamaya 1982; 2001", "article on Yogācāra texts with addendum", "499"),
  ("ref-yokoyama", "Yokoyama & Hirosawa 1996, 1997", "trilingual index of the YoBh (criticised by Silk 2001); online version", "513"),
  ("ref-huang2001", "Huang et al. 2001", "Chinese–Tibetan index ('of no practical value')", "514"),
  ("ref-cbeta-sat", "CBETA; SAT Daizōkyō Text Database", "electronic Chinese canon", "514"),
  ("ref-ybh-db", "Yogācārabhūmi Database (DDBC; Bhikkhu et al. 2002)", "parallel Chinese, Sanskrit, Tibetan texts", "514"),
  ("ref-acip", "ACIP Release VI", "electronic Tibetan text (Derge)", "514–515"),
  ("ref-shi1986", "Shi 1986: 137–199", "synoptic presentation of the contents (Sino-Japanese analysis)", "515"),
  ("ref-swtf", "SWTF", "Sanskrit-Wörterbuch der Turfan-Funde", "514"),
  ("ref-catalogues", "Lhan kar ma (Herrmann-Pfandt 2008); 'Phang thang ma", "early Tibetan catalogues listing the YoBh", "507"),
]:
    I(rid, "0.2; 2.0", p, RF, "multi", "reference", lab, sub=sub, spans=[WHOLE(int(p.split(",")[0].split("–")[0]))])
I("ref-choi2002", "2.0", "513–514", RF, "multi", "index", "Choi 2002 (cf. Choi 2001: 213–360)", sub="index of ŚrBh sections and Xiǎnyáng lùn parallels", spans=[SEC(513, "b13")])
I("ref-inaba1952", "2.0 n. 68", "513", RF, "multi", "index", "Inaba 1952 (not seen by Delhey)", sub="older YoBh index with Skt equivalents from the BoBh",
  spans=[WHOLE(513)])
I("ref-ui1961-index", "2.0; 2.1.9.1", "514, 526", RF, "multi", "index", "Ui 1961: 313–591", sub="Sanskrit–Chinese index of the BoBh", spans=[S(514, sec="b15")])
I("ref-edgerton", "2.0", "514", RF, "multi", "dictionary", "Edgerton 1953 (BHSD); Wogihara 1904, 1908; de Jong 1987: 166–171", sub="lexicography of the BoBh",
  spans=[S(514, sec="b15")])
I("ref-ms-catalogues", "1.2", "508–510", RF, "multi", "catalogue", "MS catalogues and reports: Sāṅkṛtyāyana 1937, 1938; Bandurski 1994; Sferra 2000, 2009; Hu-von Hinüber 2006; Bendall 1883; Goshima & Noguchi 1983; Waldschmidt et al. (SHT); Matsuda 1990, Matsuda & Steinkellner 1991, Matsuda 2002",
  sub="where the manuscripts and photographs are", spans=[S(508, sec=["b1", "b2", "b3", "b6", "b7", "b8", "b10", "b11", "b12", "b13", "b14", "b15", "b16", "b17"]),
  S(510, t=["589b19", "600c10"]), S(510, t=["728c16", "730b21"]), S(510, t=["768c20", "769c9"])])
I("ref-suzuki1995", "1.2 n. 34", "508", RF, "multi", "reference", "Suzuki 1995; ŚrBh Study Group 1994: 7–22", sub="script table and collation table (Skt–Tib.–Chin.) of the ŚrBh MS",
  spans=[S(508, sec=["b7", "b8"]), S(508, t=["354b17", "388b10"], extent="approx-start"), S(508, sec=["b13", "b14"])])
I("ref-bdk", "2.0", "513", RF, "en", "reference", "BDK English translation of T1579 (announced)", sub="not yet published (2010)", spans=[WHOLE(513)])

# ---------------------------------------------------------------- modern translations and reviews
def T(id, sect, pages, label, lang, spans, sub=None):
    I(id, sect, pages, "mod", lang, "modern-translation", label, spans, sub=sub)

T("tr-shimizu1985", "2.1.1 n. 79", "516", "Shimizu 1983–1985", "ja", [SEC(516, ["b1", "b2"], note="bhūmi 1 and (parts of?) the Manobhūmi; not seen by Delhey")])
T("tr-hakamaya1999", "2.1.1", "516", "Hakamaya 1999", "ja", [S(516, bh=["48,7", "49,3"], own="Bh. 48,7–49,3")])
T("tr-chan2007", "2.1.1", "516", "Chan 2007: 146–184", "en", [S(516, bh=["105,1", "112,22"], own="Bh. 105–112")])
T("tr-furusaka2001", "2.1.1", "516", "Furusaka 2001", "ja", [S(516, bh=["118,14", "120,11"], own="Bh. 118,14–120,11")])
T("tr-mikogami1969", "2.1.1", "516", "Mikogami 1969", "ja", [S(516, bh=["120,22", "122,6"], own="Bh. 120,22–122,6")])
T("tr-mikogami1967", "2.1.1", "516", "Mikogami 1967", "ja", [S(516, bh=["137,1", "142,22"], own="Bh. 137–142")])
T("tr-hayashima1991", "2.1.1", "516", "Hayashima 1991a, 1991b", "ja", [S(516, bh=["132,13", "134,2"], own="1991a: Bh. 132,13–134,2")])
T("tr-shukla1969", "2.1.1 n. 81", "516", "Shukla 1969 (paraphrase)", "en", [S(516, bh=["129,6", "137,8"], extent="section-only", note="ātmavāda section, rather a paraphrase")])
T("tr-chemparathy", "2.1.1", "516", "Chemparathy 1968–1969: 94–96", "en", [S(516, bh=["144,7", "145,18"], own="Bh. 144,7–145,18")])
T("tr-ahn2003", "2.1.1; 2.2.1–2", "517, 533", "Ahn 2003 (German transl.)", "de", [S(517, bh=["160,10", "170,10"]), S(533, t=["602a9", "604b9"]), S(533, t=["621a26", "630a5"])])
T("tr-delhey2009", "2.1.1", "517", "Delhey 2009 (German transl.)", "de", [S(517, sec="b6", extent="selections")])
T("tr-delhey2006", "2.1.2; 2.2.3", "518, 534", "Delhey 2006: 140–150", "de", [S(518, sec="b7"), S(534, sec="v7")])
T("tr-sg", "2.1.2–2.1.7", "518–521", "Śrāvakabhūmi Study Group 1998, 2007 (Japanese)", "ja",
  [S(518, sec="b7"), S(518, t=["354a06", "356a12"]), S(520, sec=["b10-sabda", "b10-silpa"]), S(520, sec="b11-12"),
   S(520, sec="b11-ag"), S(521, sec=["b13-ys1", "b13-ys2"])])
T("tr-wayman1984", "2.1.3; 2.1.5", "518, 520", "Wayman 1984 (English)", "en", [S(518, sec="b8"), S(520, sec="b11-pg"), S(520, sec="b11-ag")])
T("tr-pandey1986", "2.1.4.2", "520", "Pandey 1986 (Hindi)", "hi", [S(520, sec="b10-hetu")])
T("tr-yaita", "2.1.4.2", "520", "Yaita 1992: 547–576; 2005: 22–41", "ja", [S(520, sec="b10-hetu")])
T("tr-wayman1999", "2.1.4.2", "520", "Wayman 1999 (English)", "en", [S(520, sec="b10-hetu")])
T("tr-kloppenborg", "2.1.8", "523", "Kloppenborg 1974: 126–129", "en", [S(523, sec="b14")])
T("tr-wayman1997", "2.1.8", "523", "Wayman 1997: 193–196", "en", [S(523, sec="b14")])
T("tr-yonezawa", "2.1.8", "523", "Yonezawa 1998: 19–25", "en", [S(523, sec="b14")])
T("tr-mori1986", "2.1.7", "522", "Mōri 1986", "ja", [SEC(522, "b13-ys3", note="beginning of yogasthāna 3")])
T("tr-deleanu2006", "2.1.7", "522", "Deleanu 2006 (English)", "en", [S(522, sh=["437,1", "470,6"])])
T("tr-choi2001", "2.1.7", "521–522", "Choi 2001 (German, from the Xiǎnyáng lùn)", "de", [SEC(521, "b13", note="see Choi 2001 for the spans")])
T("tr-sakuma1990", "passim", "516–540", "Sakuma 1990 (German)", "de", [WHOLE(516, note="German translations of all passages he edits")])
T("tr-maithri1999", "2.1.7; 2.1.9.4", "522, 531", "Maithrimurthi 1999 (German)", "de", [SEC(522, "b13"), S(531, bobhd=["166,1", "170,17"])])
T("tr-ui1961", "2.1.9.1", "526", "Ui 1961: 1–312", "ja", [S(526, sec="b15", extent="selections")])
T("tr-bendall", "2.1.9.1", "527", "Bendall & de La Vallée Poussin 1905, 1906, 1911", "en", [S(527, t=["478b12", "505a23"], own="I.1–8 (annotated summary)")])
T("tr-thurman", "2.1.9.1 n. 142", "526", "Thurman et al. (BoBh translation in preparation)", "en", [S(526, sec="b15", extent="section-only")])
T("tr-mullens", "2.1.9.1 n. 142", "526", "Mullens 1994 (Ph.D.)", "en", [S(526, sec="b15", extent="selections")])
T("tr-roth", "2.1.9.2", "527", "Roth 1975–1976 (English)", "en", [S(527, bobhd=["1,1", "2,3"])])
T("tr-wangchuk2002", "2.1.9.2 n. 145", "527", "Wangchuk 2002: 27–70; 2007", "en", [S(527, sec="bb-I.2")])
T("tr-soma1986b", "2.1.9.2", "527", "Sōma 1986b; 1987", "ja", [S(527, t=["478b12", "486b09"], own="I.1–3")])
T("tr-soma1986a", "2.1.9.2", "527", "Sōma 1986a", "ja", [S(527, sec="bb-I.4")])
T("tr-takahashi2005", "2.1.9.2", "527", "Takahashi 2005a: 151–179", "ja", [S(527, sec="bb-I.4")])
T("tr-frauwallner", "2.1.9.2; 2.2.5.3", "527, 537", "Frauwallner 1969", "de", [SEC(527, "bb-I.4", own="pp. 264–279"), S(537, t=["713c28", "736c12"], own="pp. 279–295: Saṃdh VI, parts of VII", extent="section-only")])
T("tr-willis1979", "2.1.9.2", "527", "Willis 1979: 67–175 (repr. Koller 1991)", "en", [S(527, sec="bb-I.4")])
T("tr-yaita2010", "2.1.9.2", "527", "Yaita 2010 (Japanese)", "ja", [S(527, sec="bb-I.5")])
T("tr-yaita2008", "2.1.9.2", "528", "Yaita 2008 (Japanese)", "ja", [S(528, sec="bb-I.9")])
T("tr-tatz1986", "2.1.9.3", "530", "Tatz 1986: 47–89", "en", [S(530, sec="bb-I.10")])
T("tr-fujita", "2.1.9.3", "530", "Fujita 1989, 1990, 1991; Fujita 2001 (Ph.D.)", "ja", [S(530, sec="bb-I.10")])
T("tr-leumann1933", "2.1.9.3", "530", "Leumann 1933–1936: 368–384", "de", [SEC(530, "bb-I.10", note="analysis and abbreviated translation")])
T("tr-sparham2009", "2.1.9.3 n. 167", "530", "Sparham 2009", "en", [SEC(530, "bb-I.10", note="small parts; seriously flawed")])
T("tr-markert", "2.1.9.4", "531", "Markert-Braham 2005 (transl.)", "en", [S(531, sec="bb-I.11")])
T("tr-lamotte1976", "2.1.9.4", "531", "Lamotte 1976: 1857–1859", "fr", [S(531, bobhd=["185,5", "186,10"], own="BoBhD 185,5–186,10 = BoBhW 272,12–274,7")])
T("tr-harada2010", "2.1.9.4", "531", "Harada 2010", "ja", [SEC(531, "bb-II.4", note="begun")])
T("tr-furusaka1985", "2.1.9.4", "531", "Furusaka 1985: 93–99", "ja", [S(531, sec=["bb-III.1", "bb-III.2"])])
T("tr-nasu2010", "2.1.9.4", "531", "Nasu 2010", "ja", [SEC(531, "bb-III.6", note="ten powers (begun)")])
T("tr-furusaka1996", "2.1.9.4", "531", "Furusaka 1996: 118–123", "ja", [S(531, t=["576b20", "576b29"], extent="approx-start", note="Anukramapaṭala; its place in T1579 not given")])
T("tr-griffiths1986", "2.2.1.1", "532", "Griffiths 1986: 129–138", "en", [S(532, t=["579a14", "579c22"])])
T("tr-waldron2003", "2.2.1.1", "532", "Waldron 2003: 178–189", "en", [S(532, t=["579c23", "582a12"])])
T("tr-kramer2005", "2.2.5.1", "535", "Kramer 2005 (German)", "de", [S(535, t=["695c26", "703a25"])])
T("tr-samdh", "2.2.5.3", "537", "Saṃdh: Lamotte 1935; Powers 1995; Keenan 2000; Cleary 1995; Cornu 2005; Hakamaya 1994; Nozawa 1957", "multi",
  [S(537, t=["713c28", "736c12"], extent="section-only")])
T("tr-schmit1969b", "2.2.6", "538", "Schmithausen 1969b (German)", "de", [S(538, sec="v16")])

# reviews with text-critical remarks
for rid, lab, sub, spans in [
  ("rv-demieville1958", "Demiéville 1958 (review of Bh.)", "the Chinese should have been used", [S(515, sec=["b1", "b2", "b3"])]),
  ("rv-conze1963", "Conze 1963 (review of Bh., Wayman 1961)", "overview of the contents of ch. 3", [S(516, sec="b3")]),
  ("rv-dejong1976a", "de Jong 1976a; Schmithausen 1982a: 457", "on Shukla's and Wayman's ŚrBh", [S(521, sec="b13")]),
  ("rv-dejong1976b", "de Jong 1976b", "on Kloppenborg's Pratyekabuddhabhūmi", [S(523, sec="b14")]),
  ("rv-dejong1985-87", "de Jong 1985; 1987: 164–171; 1989", "on Willis, the BoBh MSS and editions, Tatz", [S(526, sec="b15")]),
  ("rv-tillemans1997", "Tillemans 1997; Wedemeyer 2003", "reviews of Powers' Saṃdh books", [S(537, t=["713c28", "736c12"], extent="section-only")]),
]:
    I(rid, "passim", "515–538", "mod", "multi", "review", lab, sub=sub, spans=spans)

# drop the placeholder (None) entries
ITEMS = [x for x in ITEMS if x]

# ---------------------------------------------------------------- Saṃdhinirmocanasūtra group
# Chapter boundaries inside the Viniścaya citation were located by matching the
# chapter openings of Xuánzàng's independent translation (T676) in T1579
# (see SAMDH_SECTIONS). Chapter numbers follow Lamotte 1935 / the Tibetan.
for old in ["rel-samdh", "rel-samdh-comm", "te-saṃdh-yoshimura", "te-saṃdh-recensions", "cit-samdh", "tr-samdh", "rv-tillemans1997"]:
    ITEMS = [x for x in ITEMS if x and x["id"] != old]
SD = "samdh"
I("sd-cit", "2.2.5.3", "503, 535", SD, "zh", "citation", "Saṃdhinirmocanasūtra quoted in the *Bodhisattvabhūmiviniścaya",
  sub="nearly the whole sūtra (without the introduction and the concluding sentence, n. 181), each chapter introduced by one sentence",
  dn=[DNZH("ZH_T30_1579"), DNBO("BO_T06_D4038-2")],
  spans=[S(535, t=["713c28", "718a09"], own="Saṃdh I–IV (T676 ch. 2)"), S(535, t=["718a09", "718c05"], own="Saṃdh V"),
         S(535, t=["718c05", "719b15"], own="Saṃdh VI"), S(535, t=["719b15", "723b20"], own="Saṃdh VII"),
         S(535, t=["723b20", "729a19"], own="Saṃdh VIII"), S(535, t=["729a19", "733c17"], own="Saṃdh IX"),
         S(535, t=["733c17", "736c12"], own="Saṃdh X; whole citation = Q5539.'i.47b7–108b8")],
  note="Chapter boundaries located by matching the opening lines of the chapters of T676 in T1579 (data-derived).")
I("sd-t676", "2.2.5.3", "536", SD, "zh", "translation", "T676 Jiě shēnmì jīng 解深密經 (Xuánzàng)", sub="complete independent translation",
  dn=[DNZH("ZH_T16_0676")], spans=[S(536, t=["713c28", "736c12"], own="T676.688b–711b")])
I("sd-t675", "2.2.5.3", "536", SD, "zh", "translation", "T675 Shēnmì jiětuō jīng 深密解脫經 (*Bodhiruci)", sub="complete (Matsuda 2013: 942 n. 8)",
  dn=[DNZH("ZH_T16_0675")], spans=[S(536, t=["713c28", "736c12"])])
I("sd-t677", "2.2.5.3", "536", SD, "zh", "translation", "T677 Fóshuō jiějié jīng 佛說解節經 (Paramārtha)", sub="chapters I–IV only (Matsuda 2013: 943 n. 12)",
  dn=[DNZH("ZH_T16_0677")], spans=[S(536, t=["713c28", "718a09"], own="Saṃdh I–IV; T677.711–714")])
I("sd-t678", "2.2.5.3", "536", SD, "zh", "translation", "T678 Xiāngxù jiětuō dì bōluómì liǎoyì jīng 相續解脫地波羅蜜了義經 (Guṇabhadra)", sub="chapter IX as an independent sūtra (Matsuda 2013: 943 n. 11)",
  dn=[DNZH("ZH_T16_0678")], spans=[S(536, t=["729a19", "733c17"], own="Saṃdh IX; T678.714–718")])
I("sd-t679", "2.2.5.3", "536", SD, "zh", "translation", "T679 Xiāngxù jiětuō rúlái suǒzuò suíshùn chù liǎoyì jīng 相續解脫如來所作隨順處了義經 (Guṇabhadra)", sub="chapter X as an independent sūtra (Matsuda 2013: 943 n. 11)",
  dn=[DNZH("ZH_T16_0679")], spans=[S(536, t=["733c17", "736c12"], own="Saṃdh X; T679.718–720")])
I("sd-d106", "2.2.5.3", "536", SD, "bo", "translation", "D106 / Q774 'Phags pa dgongs pa nges par 'grel pa (bKa' 'gyur)", sub="two recensions (Powers 1993b; Kato 2006)",
  dn=[DNBO("BO_K10_D0106")], spans=[S(536, t=["713c28", "736c12"], own="Q774")])
I("sd-dunhuang", "2.2.5.3", "536", SD, "bo", "translation", "Earlier Tibetan translation from Dūnhuáng (Hakamaya 1984, 1986, 1987a, 1987b, 2008)", sub="large fragments, edited synoptically with D106",
  spans=[S(536, t=["713c28", "736c12"], extent="section-only", note="extent of the fragments not given by Delhey")])
I("sd-skt-kathm", "1.2 no. 9a; 2.2.5.3", "510, 535", SD, "sa", "manuscript", "Sanskrit: Kathmandu folio (Matsuda 1995; 2013)", sub="end of ch. VIII and beginning of ch. IX",
  spans=[S(535, t=["728c16", "730b21"], own="Saṃdh VIII.39–IX.6")])
I("sd-skt-sht923", "2.2.5.3 n. 184", "536", SD, "sa", "manuscript", "Sanskrit: SHT III 923 (and SHT III 981)", sub="923: end of ch. II and beginning of ch. III (Matsuda 2013: 941); 981 not specified",
  spans=[S(536, t=["713c28", "718a09"], extent="section-only", note="within Saṃdh I–IV")])
I("sd-skt-testimonia", "2.2.5.3 n. 184", "536", SD, "sa", "citation", "Sanskrit testimonia: Triṃśikābhāṣya (Lévi 1925; Buescher 2007); Bhāvanākrama III (Tucci 1971); Jñānaśrīmitra (Schmithausen 2005)",
  spans=[S(536, t=["713c28", "718a09"], own="Saṃdh III verse (Bhāvanākrama III)", extent="section-only"),
         S(536, t=["718a09", "718c05"], own="Saṃdh V (Triṃśikābhāṣya)", extent="section-only"),
         S(536, t=["719b15", "723b20"], own="Saṃdh VII.15 (Bhāvanākrama III)", extent="section-only"),
         S(536, t=["723b20", "729a19"], own="Saṃdh VIII.7 (Jñānaśrīmitra)", extent="section-only")])
I("sd-editions", "2.2.5.3", "536", SD, "bo", "edition", "Editions: Lamotte 1935 (Tib., Narthang); Nozawa 1957 (ch. VIII); Yoshimura 1959 (VIII, Tib./Chin.); Powers 1995 (Derge)",
  sub="new critical edition in progress in Japan (Kato 2006)", spans=[S(536, t=["713c28", "736c12"], extent="section-only"),
                                                                 S(536, t=["723b20", "729a19"], own="Nozawa; Yoshimura: ch. VIII")])
I("sd-studies", "2.2.5.3", "536–537", SD, "bo", "study", "Powers 1993b; Kato 2006; Schmithausen 1984; Yamada 1959; Sueki 2008; Matsuda 2013", sub="recensions, text-critical problems, bibliography",
  spans=[S(536, t=["713c28", "736c12"], extent="section-only")])
I("sd-transl", "2.2.5.3", "537", SD, "multi", "modern-translation", "Translations: Lamotte 1935 (fr); Powers 1995, Keenan 2000, Cleary 1995 (en); Cornu 2005 (fr); Frauwallner 1969 (de, VI–VII); Hakamaya 1994 (ja, VI–VII); Nozawa 1957 (ja, VIII)",
  spans=[S(537, t=["713c28", "736c12"], extent="section-only"), S(537, t=["718c05", "723b20"], own="Frauwallner; Hakamaya: VI–VII"),
         S(537, t=["723b20", "729a19"], own="Nozawa: VIII")])
I("sd-reviews", "2.2.5.3 nn. 192, 196", "537–538", SD, "multi", "review", "Tillemans 1997; Wedemeyer 2003", sub="reviews of Powers' Saṃdh books", spans=[S(537, t=["713c28", "736c12"], extent="section-only")])
I("sd-comm", "2.2.5.3", "537–538", SD, "bo", "commentary", "Commentaries: D3981 (Asaṅga?; Lamotte 1935, Powers 1992a); D4016 Woncheuk (Tib. by Chos grub); D4358 (Tibetan)",
  dn=[DNBO("BO_T05_D3981"), DNBO("BO_T05_D4016")], spans=[S(537, t=["713c28", "736c12"], extent="section-only")])
I("sd-d4033", "2.2.5.3", "537–538", SD, "bo", "commentary", "D4033 / Q5535 Jñānagarbha on ch. VIII (Nozawa 1957; Powers 1992a, 1998; Steinkellner 1989)",
  dn=[DNBO("BO_T06_D4033")], spans=[S(537, t=["723b20", "729a19"], own="Saṃdh VIII (Maitreyaparivarta)")])
SAMDH_SECTIONS = [
 ("sd-1", 3, "Saṃdh I–IV", "解深密經 勝義諦相品", "713c28", "718a09", ""),
 ("sd-5", 3, "Saṃdh V Viśālamati", "心意識相品", "718a09", "718c05", ""),
 ("sd-6", 3, "Saṃdh VI Guṇākara", "一切法相品", "718c05", "719b15", ""),
 ("sd-7", 3, "Saṃdh VII Paramārthasamudgata", "無自性相品", "719b15", "723b20", ""),
 ("sd-8", 3, "Saṃdh VIII Maitreya", "分別瑜伽品", "723b20", "729a19", ""),
 ("sd-9", 3, "Saṃdh IX Avalokiteśvara", "地波羅蜜多品", "729a19", "733c17", ""),
 ("sd-10", 3, "Saṃdh X Mañjuśrī", "如來成所作事品", "733c17", "736c12", ""),
]

for s in SAMDH_SECTIONS:
    SECTIONS.append(s)
    sections.append({"id": s[0], "level": s[1], "name": s[2], "zh": s[3], "from": s[4], "to": s[5], "fasc": s[6]})

DERIVED = []
def DR(etext, lang, label, sub=None, contained=None):
    url = {"sa": "https://dharmamitra.org/nexus/db/sa/%s/text", "bo": "https://dharmamitra.org/nexus/db/bo/%s/text",
           "zh": "https://dharmamitra.org/nexus/db/zh/%s/text"}[lang] % etext
    d = {"id": "dn-" + etext, "etext": etext, "group": "dn", "lang": lang, "type": "etext", "label": label,
         "dn": [{"id": etext, "lang": lang, "url": url}]}
    if sub: d["sub"] = sub
    if contained: d["contained"] = contained
    DERIVED.append(d)

# Parts of an e-text that are too short or too fragmentary to be aligned: drawn
# in the e-text's row (basis "contained") where no aligned span covers them.
# T1579 locations from the "Ch." references printed in the edition.
def C(a, b, own, note=None):
    d = {"t": [a, b], "own": own}
    if note: d["note"] = note
    return d

DR("SA_T06_n1394u", "sa", "SA_T06_n1394u – Bhattacharya 1957 (emended)")
DR("SA_T06_-ybh-klesa", "sa", "SA_T06_-ybh-klesa – Ahn 2003")
DR("SA_T06_sambhu", "sa", "SA_T06_sambhu – Delhey 2009")
DR("SA_T06_srabhu_u", "sa", "SA_T06_srabhu_u – Śrāvakabhūmi Study Group", contained=[
   C("344b19", "344c15", "App. I Asamāhitā Bhūmiḥ, Śbh II 276–281", "Ch. 344b19–c15 (segments 6764–6787)"),
   C("354a06", "354b16", "App. II §A.I-1–7, Śbh II 284–290", "end of the adhyātmavidyā; lost in the Sanskrit MS, supplied from the Tibetan by the editors (Ch. 354a6–b19)"),
   C("354b17", "356a07", "App. II §A.I-8–IV-2, Śbh II 290–305", "end of the adhyātmavidyā, Sanskrit (Ch. 354b19–356a8)"),
   C("356a08", "356a11", "App. II §B, Śbh II 305", "cikitsāvidyā (Ch. 356a8; T1579 356a8–a11); the hetuvidyā (§C) is not edited here, see SA_T06_ybh-hetuvidya"),
   C("360c21", "361b17", "App. II §D–E, Śbh II 306–315", "śabdavidyā and śilpakarmasthānavidyā (Ch. 360c21–361b4ff.)"),
   C("361b18", "363a11", "App. III Cintāmayī Bhūmiḥ 1–2, Śbh II 318–337", "Ch. 361b18–363a8ff."),
   C("367a06", "370a08", "App. IV Ābhiprāyikārthagāthānirdeśa, Śbh II 340–370", "Ch. 367a6–369c22ff., to the end of the section (370a8)"),
  ])
DR("SA_T06_srabhusu", "sa", "SA_T06_srabhusu – Shukla 1973")
DR("SA_T06_ybh-laukikamarga", "sa", "SA_T06_ybh-laukikamarga – Deleanu 2006")
DR("SA_T06_bsa034", "sa", "SA_T06_bsa034 – Dutt 1966")
DR("SA_T06_Asaṅga_Bodhisattvabhūmi", "sa", "SA_T06_Asaṅga_Bodhisattvabhūmi – BoBh (Wogihara pagination)", sub="not aligned itself: placed by text matching to SA_T06_bsa034")
DR("SA_T06_Asaṅga_Bodhisattvabhūmi-wogiwara", "sa", "SA_T06_Asaṅga_Bodhisattvabhūmi-wogiwara – Wogihara (partial e-text)", sub="not aligned itself: placed by text matching to SA_T06_bsa034")
DR("SA_T06_abhsubhu", "sa", "SA_T06_abhsubhu – Abhidharmasamuccayabhāṣya")
DR("SA_T06_ybh-sacittika", "sa", "SA_T06_ybh-sacittika – Wayman 1960", sub="Sacittikā/Acittikā Bhūmiḥ only; not aligned to the Chinese itself: placed via its alignment to the Tibetan (BO_T06_D4035)")
DR("SA_T06_ybh-hetuvidya", "sa", "SA_T06_ybh-hetuvidya – Yaita 2005", sub="hetuvidyā of the Śrutamayī Bhūmiḥ")
DR("SA_T06_ybh-pratyekabuddha", "sa", "SA_T06_ybh-pratyekabuddha – Yonezawa 1998")
DR("SA_T06_ybh-sopadhika", "sa", "SA_T06_ybh-sopadhika – Schmithausen 1991")
DR("SA_T06_ybh-paryaya", "sa", "SA_T06_ybh-paryaya – Matsuda 1994", sub="Paryāyasaṃgrahaṇī folio, critical text")
for d in ["D4035", "D4036", "D4037", "D4038", "D4038-2", "D4039", "D4039-2", "D4040", "D4041", "D4042", "D4043", "D4044", "D4046", "D4047"]:
    DR("BO_T06_" + d, "bo", "BO_T06_" + d, sub={"D4038-2": "second part of D4038 (vol. 'i)",
        "D4039-2": "file labelled D4039 but aligned to the ranges of D4041 (Paryāya) and D4040 (Vinaya) – numbering to be checked",
        "D4043": "*Yogācārabhūmivyākhyā – a commentary, aligns only sporadically"}.get(d))
DR("ZH_T30_1581", "zh", "ZH_T30_1581 – Dharmakṣema", sub="placed via its alignment to the Sanskrit BoBh (SA_T06_bsa034)")
DR("ZH_T30_1582", "zh", "ZH_T30_1582 – Guṇavarman", sub="placed via its alignment to the Sanskrit BoBh (SA_T06_bsa034)")
DR("ZH_T24_1500", "zh", "ZH_T24_1500 – Púsà jièběn (Dharmakṣema)", sub="placed via the Sanskrit BoBh")
DR("ZH_T24_1501", "zh", "ZH_T24_1501 – Púsà jièběn (Xuánzàng)", sub="placed via the Sanskrit BoBh")
DR("ZH_T31_1602", "zh", "ZH_T31_1602 – Xiǎnyáng shèngjiào lùn", sub="placed via its alignments with the Sanskrit YBh e-texts (only stretches with a Sanskrit e-text can show)")

# ------------------------------------------------------------------ Q anchors
Q_ANCHORS = {"Q5539": [
  ["zi2b2", "579a14"], ["zi4a4", "579c22"], ["zi4a5", "579c23"], ["zi9a8", "581c3"], ["zi10a3", "581c22"], ["zi10b6", "582a12"],
  ["zi21b1", "585c9"], ["zi29b1", "588c9"], ["zi30a5", "589a9"], ["zi30b7", "589b2"], ["zi31a5", "589b19"], ["zi59b2", "600c10"],
  ["zi65a3", "602a9"], ["zi68b7", "604b9"], ["zi76a5", "607a23"], ["zi78a3", "608a6"], ["zi112b2", "621a26"], ["zi137b1", "630a5"],
  ["zi152a4", "635c6"], ["zi158a4", "638a19"], ["zi168a1", "642a5"], ["zi169a5", "642b20"], ["zi173a5", "644a6"],
  ["zi236b1", "669a8"], ["zi237a5", "669b3"], ["zi242b8", "671b14"], ["zi255a7", "676b9"], ["zi255b2", "676b16"], ["zi302b1", "695c26"],
  ["'i19b6", "703a25"], ["'i30a6", "707a5"], ["'i31b5", "707b23"], ["'i40a1", "710c29"], ["'i43a5", "712a17"], ["'i47b7", "713c28"],
  ["'i87b7", "728c16"], ["'i92a3", "730b21"], ["'i100b8", "733c19"], ["'i108b8", "736c12"], ["'i115a1", "738c28"],
  ["'i134b8", "746c14"], ["'i136b7", "747b25"]]}

GROUPS = [
  {"id": "sa-ms", "label": "Sanskrit manuscripts & testimonia", "lang": "sa"},
  {"id": "sa-ed", "label": "Sanskrit editions (complete and partial)", "lang": "sa"},
  {"id": "bo", "label": "Tibetan translation (bstan 'gyur)", "lang": "bo"},
  {"id": "te", "label": "Editions & studies of the Tibetan / Chinese text", "lang": "bo"},
  {"id": "zh", "label": "Chinese translations and extracts", "lang": "zh"},
  {"id": "samdh", "label": "Saṃdhinirmocanasūtra – quoted in the Viniścaya, and its versions", "lang": "multi"},
  {"id": "rel", "label": "Commentaries and related texts", "lang": "multi"},
  {"id": "ref", "label": "Reference works: indices, catalogues, bibliographies, databases", "lang": "multi"},
  {"id": "mod", "label": "Modern translations and reviews", "lang": "modern", "collapsed": True},
  {"id": "dn", "label": "DharmaNexus e-texts – aligned to T1579 (data-derived)", "lang": "dn"},
]

SOURCES = {
 "delhey2013": "Martin Delhey, “The Yogācārabhūmi Corpus: Sources, Editions, Translations, and Reference Works”, in Ulrich Timme Kragh (ed.), The Foundation for Yoga Practitioners: The Buddhist Yogācārabhūmi Treatise and Its Adaptation in India, East Asia, and Tibet, Harvard Oriental Series 75, Cambridge, MA: Harvard University Press, 2013, pp. 498–561.",
 "t1579": "Taishō Shinshū Daizōkyō vol. 30, no. 1579, pp. 279a–882a (CBETA line numbers as in DharmaNexus ZH_T30_1579).",
 "dharmanexus": "DharmaNexus (https://dharmamitra.org/nexus) e-texts and the Dharmamitra multilingual sentence alignments.",
}

checklist = [{k: it[k] for k in ("id", "delhey_section", "pages", "group", "lang", "type", "label", "sub", "note") if k in it}
             | {"localisation": ("not localised" if not it["spans"] else
                                 "located" if any(s.get("extent") is None for s in it["spans"]) else
                                 sorted({s["extent"] for s in it["spans"]})[0]),
                "n_spans": len(it["spans"]), "dharmanexus": [d["id"] for d in it.get("dn", [])]}
             for it in ITEMS]
with open(os.path.join(ROOT, "data", "delhey_checklist.json"), "w", encoding="utf-8") as fh:
    json.dump({"source": SOURCES["delhey2013"], "note": "One entry per edition, partial edition, translation, study with text-critical content, reference work and manuscript mentioned by Delhey (plus the Saṃdhinirmocanasūtra versions after Matsuda 2013). 'pages' = Delhey pages.",
               "items": checklist}, fh, ensure_ascii=False, indent=1)
out = {"title": "Yogācārabhūmi corpus map", "axis": {"text": "T1579", "from": "279a08", "to": "882a12", "fascicles": FASC},
       "groups": GROUPS, "sections": sections, "rows": ITEMS, "derived_rows": DERIVED,
       "q_anchors": Q_ANCHORS, "concordance_anchors": {"Bh.": [[3, "279a08"]], "BoBhD": [[1, "478b12"]]}, "sources": SOURCES}
with open(os.path.join(ROOT, "data", "delhey.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print(len(ITEMS), "items;", sum(1 for i in ITEMS if not i["spans"]), "not localised;", sum(len(i["spans"]) for i in ITEMS), "spans")
