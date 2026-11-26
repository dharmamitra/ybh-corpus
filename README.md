# Yogācārabhūmi corpus map

An interactive, dependency-free map of the whole *Yogācārabhūmi* (YBh) corpus: which parts of the work are attested in which witness, edition, translation or related text, and where.

**Live:** https://dharmamitra.github.io/ybh-corpus/ · **Offline:** open `index.html` in a browser (no server, no build step; the data are loaded from `data/corpus.js`).

## What is shown

* **Axis.** Xuánzàng's complete Chinese translation, T1579 *Yúqié shīdì lùn* 瑜伽師地論 (Taishō vol. 30, 279a–882a, 100 fascicles), which keeps the whole work in order. Positions are Taishō page + register + line (e.g. `328c7`), as numbered in CBETA and in DharmaNexus `ZH_T30_1579`. Three bands show the five parts (Basic Section, Viniścaya-, *Vyākhyā-, Paryāya-, Vastusaṃgrahaṇī), the seventeen bhūmis and the chapters of the saṃgrahaṇīs, and sub-sections (vidyāsthānas, the verse sets of the Cintāmayī Bhūmi, the Śrāvakabhūmi yogasthānas, the Bodhisattvabhūmi paṭalas). Section boundaries are the headings in T1579. Names are given in IAST and Chinese.
* **Rows**, in groups that can be collapsed and filtered by language:
  * Sanskrit manuscripts and testimonia (ŚrBh MS, YoBh MS with its folio ranges, the four BoBh MSS, SHT III 964, the Viniścaya and Paryāya fragments, the ASBh citation);
  * Sanskrit editions, complete and partial (Bhattacharya 1957, Delhey 2009, Ahn 2003, Shukla 1973, the Śrāvakabhūmi Study Group, Deleanu 2006, Wogihara, Dutt, the hetuvidyā and Pratyekabuddhabhūmi editions, the paṭala editions of the BoBh, …);
  * the Tibetan translation D4035–4042 / Q5536–5543 and its correspondence to the Chinese parts;
  * editions and studies of the Tibetan / Chinese text where no Sanskrit survives (Hakamaya, Kramer, Ahn, Schmithausen 1969b, Sakuma 1990, …);
  * Chinese translations and extracts (T1581, T1582/1583, T1584, T1499–T1503, T1615, T524), the lost *Saptadaśabhūmiśāstra, the kundoku and Uighur versions;
  * the Saṃdhinirmocanasūtra, quoted almost entirely in the *Bodhisattvabhūmiviniścaya (T1579 fasc. 75–78, 713c28–736c12), with its chapters located inside the citation, its independent versions (T676 Xuánzàng, T675 *Bodhiruci, T677 Paramārtha ch. I–IV, T678 ch. IX, T679 ch. X, D106/Q774, the Dūnhuáng Tibetan translation), the Sanskrit fragments and testimonia (Kathmandu folio, SHT III 923, citations), editions, translations and commentaries (chapter correspondences of T677–679 and SHT III 923 after Matsuda 2013, HOS 75: 938–944);
  * commentaries and related texts (*Yogācārabhūmivyākhyā D4043, T1580, T1602 *Xiǎnyáng shèngjiào lùn*, the Saṃdhinirmocanasūtra, BoBh and Śīlapaṭala commentaries, …);
  * reference works: indices, catalogues, bibliographies, databases, dictionaries;
  * modern translations and reviews with text-critical remarks (collapsed by default);
  * DharmaNexus e-texts aligned to T1579 (data-derived, see below).
* **Interaction.** Drag to pan; Ctrl/⌘ + wheel, double-click or the +/− buttons to zoom; click a section band to zoom to it; hover a bar for the witness, its span in T1579 (with fascicle) and in its own pagination, the Delhey page and how it was placed; click a bar to open the e-text in DharmaNexus (shift-click pins the details instead). The current view is kept in the URL (`#view=478b12-576b29`) so views can be shared. A table view of all spans is at the bottom of the page.

## Sources

1. Martin Delhey, “The Yogācārabhūmi Corpus: Sources, Editions, Translations, and Reference Works”, in U. T. Kragh (ed.), *The Foundation for Yoga Practitioners*, Harvard Oriental Series 75, 2013, pp. 498–561. Every bibliographic span (solid bars) cites the page of Delhey on which the claim is made. Nothing is drawn that Delhey does not locate.
2. T1579 in CBETA / DharmaNexus (section headings, fascicle starts).
3. DharmaNexus e-texts (Sanskrit, Tibetan, Chinese) and the Dharmamitra multilingual sentence alignments (Sanskrit↔Chinese, Tibetan↔Chinese), for the data-derived layer and for the page concordances.

## How spans were placed

Delhey mostly locates passages in the pagination of the edition he discusses. The `basis` of each span says how it was put on the T1579 axis:

| basis | meaning |
|---|---|
| `delhey-T` | Delhey gives the T1579 location (e.g. *T1579.589b19–600c10*). |
| `section` | Delhey names a bhūmi, paṭala or section; its T1579 heading boundaries are used. |
| `concordance` | Delhey gives pages of Bhattacharya 1957 (Bh.), Shukla 1973 (Sh.) or Dutt 1966 (BoBhD); converted with a page→Taishō concordance computed from the alignments of the DharmaNexus e-texts of these editions. Accuracy is roughly ±10 Taishō lines. |
| `q-interpolated` | Only Peking folios are given (two passages in Wangchuk 2007); interpolated linearly between Delhey's own Q = T equations. |
| `aligned` | Data-derived layer (hatched): contiguous runs of sentence alignments between a DharmaNexus e-text and T1579. |

Every checklist entry is drawn. Entries for which Delhey names only a bhūmi, chapter or section are drawn over that section with a dashed outline (`section-only`); entries concerning the whole work (reference works, kundoku, the Tibetan witnesses …) as a thin line over the whole axis (`whole-work`); entries with no location at all (6: the lost transcript of the YoBh MS, Paramārtha's lost *Saptadaśabhūmiśāstra, the Uighur translation, the Tibetan Dūnhuáng fragments, lost Indian commentaries, a Xiǎnyáng lùn quotation in the *Vyākhyā) appear as a pill in the "not localised" strip between the labels and the plot, with tooltip and Delhey page.

A dashed outline (`extent` in the data) marks spans whose start or end is uncertain, or which Delhey only locates at section level although they cover just a part of it.

## Files

* `index.html` – the map (vanilla JavaScript + SVG, no dependencies).
* `data/delhey_checklist.json` – the completeness checklist: one entry per edition, partial edition, translation, study with text-critical content, reference work and manuscript that Delhey mentions (265 entries), with his section and pages, the group it is drawn in and how it is localised (`located`, `section-only`, `whole-work`, `selections`, `not localised`, …).
* `scripts/curate_delhey.py` – the editable source of the checklist and of `data/delhey.json`.
* `data/delhey.json` – curated layer: sections, rows and spans in Delhey's own coordinates, with page citations.
* `data/derived.json` – data-derived layer: aligned spans of the DharmaNexus e-texts and the Bh./Sh./BoBhD/BoBhW page concordances.
* `data/corpus.json` – merged result (also as `data/corpus.js` for use from `file://`).
* `scripts/build_data.py` – regenerates `derived.json` from the DharmaNexus segment files and alignment releases and merges everything into `corpus.json`/`corpus.js`:

```sh
# full rebuild (needs local copies of the DharmaNexus data and alignment releases)
python3 scripts/build_data.py \
    --sanskrit PATH/dharmanexus-sanskrit/segments \
    --sanskrit-old-n1394u PATH/SA_T06_n1394u.old.json \
    --matches PATH/mitra-parallel-v3 --matches PATH/newer-release ...

# re-merge only, after editing data/delhey.json
python3 scripts/curate_delhey.py && python3 scripts/build_data.py --merge-only
```

The committed data use the releases `mitra-parallel-v3`, `-sa2611`, `-akbh2611`, `-ybh2611`, `-ybh2611b` (later ones override earlier ones per pair of texts). Chinese texts other than T1579 (T1581, T1582, T1500, T1501, T1602) are placed on the axis through Sanskrit e-texts aligned to both.

`--sanskrit-old-n1394u` is the earlier (DSBC) segmentation of `SA_T06_n1394u` to which the current alignments refer; the script maps it onto the new e-text, whose `folio` is the page of Bhattacharya 1957. Later `--matches` directories override earlier ones file by file.

The site is published by GitHub Pages from `main` via `.github/workflows/pages.yml`.

## Limits

* Delhey's survey covers publications up to c. 2010. Later editions and translations (e.g. further volumes of the Śrāvakabhūmi Study Group, newer BoBh paṭala editions, the BDK translation) are not included.
* Only what Delhey locates is drawn; items without location (most Xiǎnyáng lùn parallels, the Tibetan Dūnhuáng fragments, Mongolian/Uighur versions) are mentioned in notes at most.
* Concordance placements are approximate. Spans given by Delhey at section level for partial treatments (e.g. “three very short passages from III.3 and III.6”) are drawn over the section with a dashed outline.
* The data-derived layer is automatic and not checked by hand: gaps may be missing text or simply unaligned passages; commentaries align only sporadically. The Chinese BoBh translations are placed via their alignment to the Sanskrit BoBh, the Wogihara e-texts via text matching to the Dutt e-text.
* Delhey (pp. 511, 539) gives “Q5543, D4042” for both the *Vyākhyāsaṃgrahaṇī and the *Yogācārabhūmivyākhyā; the commentary is D4043 / Q5544 in the standard catalogues and is listed so here.
* The DharmaNexus file `BO_T06_D4039-2` aligns to the T1579 ranges of the Paryāya- and *Vinayasaṃgrahaṇī (D4041/D4040), not to the Vastusaṃgrahaṇī; its numbering should be checked.
