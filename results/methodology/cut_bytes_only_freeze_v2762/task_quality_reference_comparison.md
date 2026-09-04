# Task Quality Reference Comparison

| model | task | backend | variant | case_id | status | delta_vs_full_onnx_AP50 | delta_vs_full_onnx_AP75 | delta_vs_full_onnx_COCO_AP_50_95 | delta_vs_full_onnx_Top1 | delta_vs_full_onnx_Top5 |
|---|---|---|---|---|---|---|---|---|---|---|
| resnet50 | classification | deepx | vendor_full | full | ok |  |  |  | -0.01 | -0.004 |
| resnet50 | classification | deepx | split | b001 | ok |  |  |  | -0.046 | -0.016 |
| resnet50 | classification | deepx | split | b003 | ok |  |  |  | -0.048 | -0.026 |
| resnet50 | classification | deepx | split | b008 | ok |  |  |  | -0.044 | -0.022 |
| resnet50 | classification | deepx | split | b009 | ok |  |  |  | -0.052 | -0.022 |
| resnet50 | classification | deepx | split | b020 | ok |  |  |  | -0.048 | -0.02 |
| resnet50 | classification | deepx | split | b022 | ok |  |  |  | -0.048 | -0.022 |
| resnet50 | classification | deepx | split | b027 | ok |  |  |  | -0.044 | -0.024 |
| resnet50 | classification | deepx | split | b042 | ok |  |  |  | -0.042 | -0.024 |
| resnet50 | classification | deepx | split | b052 | ok |  |  |  | -0.044 | -0.022 |
| resnet50 | classification | deepx | split | b054 | ok |  |  |  | -0.046 | -0.022 |
| resnet50 | classification | deepx | split | b056 | ok |  |  |  | -0.044 | -0.024 |
| resnet50 | classification | deepx | split | b068 | ok |  |  |  | -0.044 | -0.024 |
| resnet50 | classification | deepx | split | b074 | ok |  |  |  | -0.044 | -0.022 |
| resnet50 | classification | deepx | split | b078 | ok |  |  |  | -0.044 | -0.022 |
| resnet50 | classification | deepx | split | b091 | ok |  |  |  | -0.046 | -0.022 |
| resnet50 | classification | deepx | split | b095 | ok |  |  |  | -0.048 | -0.022 |
| resnet50 | classification | deepx | split | b107 | ok |  |  |  | -0.048 | -0.02 |
| resnet50 | classification | deepx | split | b112 | ok |  |  |  | -0.052 | -0.02 |
| resnet50 | classification | deepx | split | b118 | ok |  |  |  | -0.05 | -0.02 |
| resnet50 | classification | deepx | split | b119 | ok |  |  |  | -0.052 | -0.024 |
| resnet50 | classification | hailo10h | vendor_full | b119 | ok |  |  |  | 0.0 | -0.004 |
| resnet50 | classification | hailo10h | split | b001 | ok |  |  |  | -0.012 | -0.004 |
| resnet50 | classification | hailo10h | split | b003 | ok |  |  |  | -0.012 | 0.0 |
| resnet50 | classification | hailo10h | split | b008 | ok |  |  |  | 0.002 | -0.006 |
| resnet50 | classification | hailo10h | split | b009 | ok |  |  |  | 0.0 | -0.004 |
| resnet50 | classification | hailo10h | split | b020 | ok |  |  |  | -0.002 | -0.006 |
| resnet50 | classification | hailo10h | split | b022 | ok |  |  |  | 0.008 | -0.006 |
| resnet50 | classification | hailo10h | split | b027 | ok |  |  |  | -0.008 | -0.006 |
| resnet50 | classification | hailo10h | split | b042 | ok |  |  |  | -0.012 | -0.008 |
| resnet50 | classification | hailo10h | split | b052 | ok |  |  |  | -0.012 | -0.008 |
| resnet50 | classification | hailo10h | split | b054 | ok |  |  |  | -0.008 | -0.01 |
| resnet50 | classification | hailo10h | split | b056 | ok |  |  |  | -0.006 | -0.006 |
| resnet50 | classification | hailo10h | split | b068 | ok |  |  |  | -0.008 | 0.0 |
| resnet50 | classification | hailo10h | split | b074 | ok |  |  |  | 0.0 | -0.002 |
| resnet50 | classification | hailo10h | split | b078 | ok |  |  |  | -0.006 | -0.002 |
| resnet50 | classification | hailo10h | split | b091 | ok |  |  |  | -0.008 | -0.002 |
| resnet50 | classification | hailo10h | split | b095 | ok |  |  |  | -0.002 | -0.004 |
| resnet50 | classification | hailo10h | split | b107 | ok |  |  |  | 0.002 | 0.002 |
| resnet50 | classification | hailo10h | split | b112 | ok |  |  |  | 0.002 | -0.002 |
| resnet50 | classification | hailo10h | split | b118 | ok |  |  |  | 0.0 | 0.002 |
| resnet50 | classification | hailo10h | split | b119 | ok |  |  |  | 0.004 | 0.002 |
| resnet50 | classification | hailo8 | vendor_full | b119 | ok |  |  |  | -0.002 | -0.002 |
| resnet50 | classification | hailo8 | split | b001 | ok |  |  |  | -0.012 | -0.004 |
| resnet50 | classification | hailo8 | split | b003 | ok |  |  |  | -0.01 | 0.0 |
| resnet50 | classification | hailo8 | split | b008 | ok |  |  |  | 0.0 | -0.004 |
| resnet50 | classification | hailo8 | split | b009 | ok |  |  |  | 0.0 | -0.006 |
| resnet50 | classification | hailo8 | split | b020 | ok |  |  |  | -0.002 | -0.006 |
| resnet50 | classification | hailo8 | split | b022 | ok |  |  |  | 0.006 | -0.004 |
| resnet50 | classification | hailo8 | split | b027 | ok |  |  |  | -0.004 | -0.01 |
| resnet50 | classification | hailo8 | split | b042 | ok |  |  |  | -0.006 | -0.01 |
| resnet50 | classification | hailo8 | split | b052 | ok |  |  |  | -0.014 | -0.01 |
| resnet50 | classification | hailo8 | split | b054 | ok |  |  |  | -0.01 | -0.006 |
| resnet50 | classification | hailo8 | split | b056 | ok |  |  |  | -0.004 | -0.006 |
| resnet50 | classification | hailo8 | split | b068 | ok |  |  |  | -0.002 | 0.0 |
| resnet50 | classification | hailo8 | split | b074 | ok |  |  |  | -0.01 | -0.002 |
| resnet50 | classification | hailo8 | split | b078 | ok |  |  |  | -0.006 | -0.004 |
| resnet50 | classification | hailo8 | split | b091 | ok |  |  |  | -0.012 | -0.004 |
| resnet50 | classification | hailo8 | split | b095 | ok |  |  |  | -0.006 | -0.006 |
| resnet50 | classification | hailo8 | split | b107 | ok |  |  |  | 0.008 | 0.0 |
| resnet50 | classification | hailo8 | split | b112 | ok |  |  |  | 0.006 | 0.0 |
| resnet50 | classification | hailo8 | split | b118 | ok |  |  |  | 0.002 | 0.002 |
| resnet50 | classification | hailo8 | split | b119 | ok |  |  |  | 0.004 | 0.004 |
| resnet50 | classification | tensorrt | vendor_full | full | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | vendor_full | full | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | vendor_full | full | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b001 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b003 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b008 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b009 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b020 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b022 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b027 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b042 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b052 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b054 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b056 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b068 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b074 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b078 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b091 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b095 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b107 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b112 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b118 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | split | b119 | ok |  |  |  | 0.0 | 0.0 |
| resnet50 | classification | tensorrt | vendor_full | b119 | ok |  |  |  | 0.0 | 0.0 |
| yolo26s | detection | deepx | vendor_full | full | ok | 0.0013787870230798083 | -0.015021279456075454 | -0.006142091075082956 |  |  |
| yolo26s | detection | deepx | split | b001 | ok | -0.001807940863810531 | -0.0005158059760043687 | -0.00030713603317766847 |  |  |
| yolo26s | detection | deepx | split | b002 | ok | -0.0021557455550473836 | -0.001847172888124915 | -0.0007964138692420075 |  |  |
| yolo26s | detection | deepx | split | b005 | ok | -0.00022998274774244098 | -0.0022136251303819243 | -0.00048711223576197726 |  |  |
| yolo26s | detection | deepx | split | b038 | ok | 0.001496302028472507 | -0.0027475737865166883 | 0.0006047932873479156 |  |  |
| yolo26s | detection | deepx | split | b042 | ok | -0.0020270237201216457 | -0.004870608076453176 | -0.0027572408544664917 |  |  |
| yolo26s | detection | deepx | split | b118 | ok | -0.0017920607756271023 | -0.002467337427753069 | -0.0014438535793370733 |  |  |
| yolo26s | detection | deepx | split | b148 | ok | -0.0015135150624088212 | -0.001397069244839233 | -0.00012494377001176504 |  |  |
| yolo26s | detection | deepx | split | b181 | ok | -0.0016311513831709368 | -0.008321373360139328 | -0.0014599442106007499 |  |  |
| yolo26s | detection | deepx | split | b221 | ok | 0.0038204754859504364 | 0.001203435375401296 | 0.002176816366626755 |  |  |
| yolo26s | detection | hailo10h | vendor_full | b001 | ok | -0.055085274230430636 | -0.0616689923449909 | -0.05678649638168576 |  |  |
| yolo26s | detection | hailo10h | split | b001 | ok | -0.013104800267679795 | -0.018148031476700632 | -0.01097088519463063 |  |  |
| yolo26s | detection | hailo10h | split | b002 | ok | -0.010131723122062675 | -0.014289634901624437 | -0.010226409872325315 |  |  |
| yolo26s | detection | hailo10h | split | b005 | ok | -0.003450614918429018 | -0.009646959141782041 | -0.0051847318058032 |  |  |
| yolo26s | detection | hailo10h | split | b038 | ok | -0.004191906812905044 | -0.010788738002797671 | -0.007219585964967967 |  |  |
| yolo26s | detection | hailo10h | split | b042 | ok | -0.00645540361430974 | -0.010533151218649173 | -0.006735998980475 |  |  |
| yolo26s | detection | hailo10h | split | b118 | ok | -0.008768076936502278 | -0.012243450755751395 | -0.009716972664810086 |  |  |
| yolo26s | detection | hailo10h | split | b148 | ok | -0.017180074662855427 | -0.02086662709122833 | -0.01568369368356337 |  |  |
| yolo26s | detection | hailo10h | split | b181 | ok | -0.016218648943127967 | -0.02202920192244029 | -0.016503266934190186 |  |  |
| yolo26s | detection | hailo10h | split | b221 | ok | -0.03261491534770422 | -0.05966653015907153 | -0.04202902112135409 |  |  |
| yolo26s | detection | hailo8 | vendor_full | b001 | ok | -0.08961842901414574 | -0.0827608847086973 | -0.07796551293294679 |  |  |
| yolo26s | detection | hailo8 | split | b001 | ok | -0.01348344665573975 | -0.017190369572674946 | -0.010933319648870787 |  |  |
| yolo26s | detection | hailo8 | split | b002 | ok | -0.008159628892225212 | -0.014063767651741443 | -0.009963349199065497 |  |  |
| yolo26s | detection | hailo8 | split | b005 | ok | -0.00696080620262296 | -0.009359794467835136 | -0.007997872723372601 |  |  |
| yolo26s | detection | hailo8 | split | b038 | ok | -0.00821282913410426 | -0.010346247001302156 | -0.00875007768067082 |  |  |
| yolo26s | detection | hailo8 | split | b042 | ok | -0.009178803529184654 | -0.012848943936647816 | -0.009904336184240192 |  |  |
| yolo26s | detection | hailo8 | split | b118 | ok | -0.007745884491665467 | -0.009166844676036678 | -0.00773530521095811 |  |  |
| yolo26s | detection | hailo8 | split | b148 | ok | -0.010034747842219693 | -0.01354555187949752 | -0.011064805168644665 |  |  |
| yolo26s | detection | hailo8 | split | b181 | ok | -0.012659412146647342 | -0.016386121133397658 | -0.012644604632681633 |  |  |
| yolo26s | detection | hailo8 | split | b221 | ok | -0.04470188281692489 | -0.07149539390892379 | -0.04964016638638569 |  |  |
| yolo26s | detection | tensorrt | vendor_full | full | ok | 0.0014006011519986927 | -0.00020069235400987928 | 0.001039874359116899 |  |  |
| yolo26s | detection | tensorrt | vendor_full | full | ok | 0.00040888823937657026 | -5.310446319012341e-05 | 0.000660679672388198 |  |  |
| yolo26s | detection | tensorrt | vendor_full | full | ok | 0.0007716465261903283 | -0.00038889874104819366 | 0.0010401495386347381 |  |  |
| yolo26s | detection | tensorrt | split | b001 | ok | 0.0006100635864946247 | -0.0005147443955192399 | 0.000816780822144092 |  |  |
| yolo26s | detection | tensorrt | vendor_full | b001 | ok | 0.0014006011519986927 | -0.00020069235400987928 | 0.001039874359116899 |  |  |
| yolo26s | detection | tensorrt | split | b002 | ok | 0.001131603973779427 | -0.0004478173939013175 | 0.0009415704386290247 |  |  |
| yolo26s | detection | tensorrt | split | b005 | ok | 0.001131603973779427 | -0.0004478173939013175 | 0.0009415704386290247 |  |  |
| yolo26s | detection | tensorrt | split | b038 | ok | 0.0006963614337515134 | -0.0002850038691027401 | 0.0009056698162072108 |  |  |
| yolo26s | detection | tensorrt | split | b042 | ok | 0.0012453739854073609 | 0.0006903400072957311 | 0.0010535221390131078 |  |  |
| yolo26s | detection | tensorrt | split | b118 | ok | 0.0012453739854073609 | 0.0006903400072957311 | 0.0010535221390131078 |  |  |
| yolo26s | detection | tensorrt | split | b148 | ok | 0.0006963614337515134 | -0.0002850038691027401 | 0.0009056698162072108 |  |  |
| yolo26s | detection | tensorrt | split | b181 | ok | 0.0009984449400465278 | 0.0007646066717582056 | 0.0012939667412180667 |  |  |
| yolo26s | detection | tensorrt | split | b221 | ok | 0.001131603973779427 | -0.0004478173939013175 | 0.0009414903611165704 |  |  |
| yolov7_paper | detection | deepx | vendor_full | full | ok | 0.008010804549892447 | 0.004274438203561437 | 0.004274475012795154 |  |  |
| yolov7_paper | detection | deepx | split | b001 | ok | 0.013258600985576074 | 0.008838984552807794 | 0.009039406588135124 |  |  |
| yolov7_paper | detection | deepx | split | b002 | ok | 0.013198673785986936 | 0.008909904995545892 | 0.009076603370359038 |  |  |
| yolov7_paper | detection | deepx | split | b013 | ok | 0.011046267839351587 | 0.009076353468664755 | 0.007932419932198453 |  |  |
| yolov7_paper | detection | deepx | split | b044 | ok | 0.012543530172050676 | 0.009450252320949426 | 0.008157444866466246 |  |  |
| yolov7_paper | detection | deepx | split | b049 | ok | 0.011348528918432188 | 0.009764606802549092 | 0.007566422005783335 |  |  |
| yolov7_paper | detection | deepx | split | b065 | ok | 0.010856323047439775 | 0.008821624912100257 | 0.006845207504172113 |  |  |
| yolov7_paper | detection | deepx | split | b088 | ok | 0.011087912215971163 | 0.008970077802417764 | 0.007127456264017007 |  |  |
| yolov7_paper | detection | deepx | split | b092 | ok | 0.011014503043255686 | 0.009679163584836004 | 0.007240591688210785 |  |  |
| yolov7_paper | detection | deepx | split | b114 | ok | 0.012067318633936397 | 0.009983502955424939 | 0.007621178701796627 |  |  |
| yolov7_paper | detection | deepx | split | b134 | ok | 0.010308074325987127 | 0.008153344600433765 | 0.006448075038722079 |  |  |
| yolov7_paper | detection | deepx | split | b155 | ok | 0.011669050048262353 | 0.009421467074737122 | 0.007794324000836295 |  |  |
| yolov7_paper | detection | deepx | split | b165 | ok | 0.01108107548207049 | 0.009173165732017263 | 0.0074812430080652415 |  |  |
| yolov7_paper | detection | deepx | split | b186 | ok | 0.010409972766912245 | 0.0072339563031155185 | 0.005904783026204563 |  |  |
| yolov7_paper | detection | deepx | split | b189 | ok | 0.009464025510346086 | 0.007184028428158573 | 0.005339180464939308 |  |  |
| yolov7_paper | detection | deepx | split | b222 | ok | 0.00708089597560102 | 0.005186023432208087 | 0.00498852736717742 |  |  |
| yolov7_paper | detection | deepx | split | b228 | ok | 0.007941466907389838 | 0.005151609274199109 | 0.0050627127566863495 |  |  |
| yolov7_paper | detection | deepx | split | b262 | ok | 0.011308797605630971 | 0.007306012675387441 | 0.007347211544401877 |  |  |
| yolov7_paper | detection | deepx | split | b270 | ok | 0.01090935046720043 | 0.00703260495816127 | 0.006999708628881274 |  |  |
| yolov7_paper | detection | deepx | split | b306 | ok | 0.012953608708068942 | 0.010724394657824265 | 0.008735764505397037 |  |  |
| yolov7_paper | detection | deepx | split | b307 | ok | 0.012592076381096828 | 0.009884499264235513 | 0.008536468624589233 |  |  |
| yolov7_paper | detection | hailo10h | vendor_full | b306 | ok | 0.012423522969578826 | -0.016890858246548346 | -0.031878303041460276 |  |  |
| yolov7_paper | detection | hailo10h | split | b001 | ok | -0.4687736095713063 | -0.38281339975534984 | -0.35289840020193247 |  |  |
| yolov7_paper | detection | hailo10h | split | b002 | ok | 0.009959007532216013 | 0.009292129181915576 | 0.006852824897274901 |  |  |
| yolov7_paper | detection | hailo10h | split | b013 | ok | 0.008443091381894585 | 0.006135805854850462 | 0.005610459718742522 |  |  |
| yolov7_paper | detection | hailo10h | split | b044 | ok | 0.010905032992215569 | 0.005918094095322124 | 0.005694594567752287 |  |  |
| yolov7_paper | detection | hailo10h | split | b049 | ok | -0.026938685562719722 | -0.021154261256872364 | -0.024711160715392755 |  |  |
| yolov7_paper | detection | hailo10h | split | b065 | ok | -0.5973630231150453 | -0.4885298674409785 | -0.4520187916528286 |  |  |
| yolov7_paper | detection | hailo10h | split | b088 | ok | -0.13360635437956525 | -0.12037513139888206 | -0.10959346858111418 |  |  |
| yolov7_paper | detection | hailo10h | split | b092 | ok | 0.011397105414826192 | 0.007696883350905792 | 0.006340869660443171 |  |  |
| yolov7_paper | detection | hailo10h | split | b114 | ok | -0.010923156789550026 | -0.005171527992011926 | -0.008907917503654883 |  |  |
| yolov7_paper | detection | hailo10h | split | b134 | ok | 0.012886072398338722 | 0.009934286243918566 | 0.007599402056675086 |  |  |
| yolov7_paper | detection | hailo10h | split | b155 | ok | 0.010048391066934226 | 0.007701497069458607 | 0.006016069261154389 |  |  |
| yolov7_paper | detection | hailo10h | split | b165 | ok | 0.010749980403423898 | 0.0072215882212956495 | 0.005851677816895939 |  |  |
| yolov7_paper | detection | hailo10h | split | b186 | ok | 0.003075163551412685 | 0.0010185456198483211 | 0.0015582112382894198 |  |  |
| yolov7_paper | detection | hailo10h | split | b189 | ok | 0.012908395733868816 | 0.006789712888179422 | 0.0057764729228572675 |  |  |
| yolov7_paper | detection | hailo10h | split | b222 | ok | 0.014030866247445206 | 0.010640958250306642 | 0.007063028338724908 |  |  |
| yolov7_paper | detection | hailo10h | split | b228 | ok | -0.04663989027722337 | -0.027171354904992118 | -0.027071430575987765 |  |  |
| yolov7_paper | detection | hailo10h | split | b262 | ok | 0.014977967941967596 | 0.006942500671980489 | 0.007322407955866361 |  |  |
| yolov7_paper | detection | hailo10h | split | b270 | ok | -0.0843994967750098 | -0.07445918489063141 | -0.06964179015686128 |  |  |
| yolov7_paper | detection | hailo10h | split | b306 | ok | 0.013373676180323368 | 0.003022580835415012 | -0.010649687512685524 |  |  |
| yolov7_paper | detection | hailo10h | split | b307 | ok | -0.2807401575778448 | -0.22595743929738488 | -0.21241485637378799 |  |  |
| yolov7_paper | detection | hailo8 | vendor_full | b306 | ok | 0.0002846130252918133 | -0.02124133356985186 | -0.03723541125000479 |  |  |
| yolov7_paper | detection | hailo8 | split | b001 | ok | -0.4687736095713063 | -0.38281339975534984 | -0.35289840020193247 |  |  |
| yolov7_paper | detection | hailo8 | split | b002 | ok | 0.009758829146549908 | 0.008849893718736623 | 0.006712614724707688 |  |  |
| yolov7_paper | detection | hailo8 | split | b013 | ok | 0.008764604023556388 | 0.007901509417829522 | 0.006050166975070603 |  |  |
| yolov7_paper | detection | hailo8 | split | b044 | ok | 0.009693838226249363 | 0.008835691871988294 | 0.007548926274043244 |  |  |
| yolov7_paper | detection | hailo8 | split | b049 | ok | -0.028999066247724636 | -0.021634080996829175 | -0.025216711810467196 |  |  |
| yolov7_paper | detection | hailo8 | split | b065 | ok | -0.5973630231150453 | -0.4885298674409785 | -0.4520187916528286 |  |  |
| yolov7_paper | detection | hailo8 | split | b088 | ok | -0.1563937079161405 | -0.1354662199163496 | -0.12225062144505289 |  |  |
| yolov7_paper | detection | hailo8 | split | b092 | ok | 0.004468100517988294 | 0.006645189085514203 | 0.004596532168475331 |  |  |
| yolov7_paper | detection | hailo8 | split | b114 | ok | -0.01675417819383107 | -0.008805641170480438 | -0.011091496174149895 |  |  |
| yolov7_paper | detection | hailo8 | split | b134 | ok | 0.006913161974879789 | 0.008960154482928806 | 0.005741263240999939 |  |  |
| yolov7_paper | detection | hailo8 | split | b155 | ok | 0.007789198897483973 | 0.010959514612239707 | 0.007155422013492785 |  |  |
| yolov7_paper | detection | hailo8 | split | b165 | ok | 0.00765001056992487 | 0.011402512889466088 | 0.007606183103387121 |  |  |
| yolov7_paper | detection | hailo8 | split | b186 | ok | -0.00240370214612462 | 0.002219692840803311 | -3.134013047573214e-05 |  |  |
| yolov7_paper | detection | hailo8 | split | b189 | ok | 0.006902106331274083 | 0.012039319923756175 | 0.006837961982778862 |  |  |
| yolov7_paper | detection | hailo8 | split | b222 | ok | 0.004895068963270521 | 0.007131748830918105 | 0.005966729402846427 |  |  |
| yolov7_paper | detection | hailo8 | split | b228 | ok | -0.04813934601658931 | -0.029018664476231137 | -0.027227277600824273 |  |  |
| yolov7_paper | detection | hailo8 | split | b262 | ok | 0.010150479907077736 | 0.013659189661761939 | 0.00808113385992365 |  |  |
| yolov7_paper | detection | hailo8 | split | b270 | ok | -0.08606468207378049 | -0.07713888539001357 | -0.07094550401769989 |  |  |
| yolov7_paper | detection | hailo8 | split | b306 | ok | 0.012071359288500783 | 0.0029889432639621516 | -0.010608777983095563 |  |  |
| yolov7_paper | detection | hailo8 | split | b307 | ok | -0.26849074509252135 | -0.21671500497498775 | -0.20396338664278957 |  |  |
| yolov7_paper | detection | tensorrt | vendor_full | full | ok | 0.01280948177422625 | 0.010109501044348934 | 0.009080979740708206 |  |  |
| yolov7_paper | detection | tensorrt | vendor_full | full | ok | 0.012768770868677892 | 0.00999410644837534 | 0.009153877477447392 |  |  |
| yolov7_paper | detection | tensorrt | vendor_full | full | ok | 0.012824724972395618 | 0.009981260504020262 | 0.009112014674885871 |  |  |
| yolov7_paper | detection | tensorrt | split | b001 | ok | 0.011369155406361742 | 0.009768610303797276 | 0.008499513469950093 |  |  |
| yolov7_paper | detection | tensorrt | split | b002 | ok | 0.012497876754196557 | 0.010465819455019343 | 0.009162776486782154 |  |  |
| yolov7_paper | detection | tensorrt | split | b013 | ok | 0.012639846468325944 | 0.009998121068324206 | 0.009113736476306589 |  |  |
| yolov7_paper | detection | tensorrt | split | b044 | ok | 0.013106527577827487 | 0.010264495155303754 | 0.009256261453807146 |  |  |
| yolov7_paper | detection | tensorrt | split | b049 | ok | 0.012665992285503025 | 0.009798108111366222 | 0.008939641456091996 |  |  |
| yolov7_paper | detection | tensorrt | split | b065 | ok | 0.012786502682484047 | 0.010100118096659727 | 0.008981672386353001 |  |  |
| yolov7_paper | detection | tensorrt | split | b088 | ok | 0.012719320295618397 | 0.010060271454772174 | 0.009008148193064336 |  |  |
| yolov7_paper | detection | tensorrt | split | b092 | ok | 0.012755257606801518 | 0.009734762113283224 | 0.009125727960507923 |  |  |
| yolov7_paper | detection | tensorrt | split | b114 | ok | 0.012682652938188932 | 0.0099735294275059 | 0.009095604328051399 |  |  |
| yolov7_paper | detection | tensorrt | split | b134 | ok | 0.012644332920265677 | 0.010045069817564256 | 0.009101060976338837 |  |  |
| yolov7_paper | detection | tensorrt | split | b155 | ok | 0.012777512125892287 | 0.00993938417275353 | 0.009059934106812217 |  |  |
| yolov7_paper | detection | tensorrt | split | b165 | ok | 0.012461340552804567 | 0.009799420306145612 | 0.008870111151533966 |  |  |
| yolov7_paper | detection | tensorrt | split | b186 | ok | 0.012510142176605732 | 0.009605252396057196 | 0.008775585407833741 |  |  |
| yolov7_paper | detection | tensorrt | split | b189 | ok | 0.012684548926530592 | 0.00994108242194841 | 0.00892280870338552 |  |  |
| yolov7_paper | detection | tensorrt | split | b222 | ok | 0.012565001893309113 | 0.00966665042140108 | 0.008760401550219399 |  |  |
| yolov7_paper | detection | tensorrt | split | b228 | ok | 0.012502144059479914 | 0.009724287330956705 | 0.008883028317076935 |  |  |
| yolov7_paper | detection | tensorrt | split | b262 | ok | 0.012642757801136217 | 0.01004061456954125 | 0.009104687653223753 |  |  |
| yolov7_paper | detection | tensorrt | split | b270 | ok | 0.012502037014554102 | 0.01001912252147602 | 0.00905532586711022 |  |  |
| yolov7_paper | detection | tensorrt | split | b306 | ok | 0.012742404009003394 | 0.010867334913351678 | 0.009258379759912394 |  |  |
| yolov7_paper | detection | tensorrt | vendor_full | b306 | ok | 0.01280948177422625 | 0.010109501044348934 | 0.009080979740708206 |  |  |
| yolov7_paper | detection | tensorrt | split | b307 | ok | 0.012573311031602419 | 0.010100693679829631 | 0.009111533530130278 |  |  |
