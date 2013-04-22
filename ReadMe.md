#CleanTabAnalys
CleanTabAnalys is actually now part of EpicorAutoPilot (Now even Gooeyier!)

What this does is turn OpenEdge Progress's TabAnalys output (_proutil dbname -C tabanalys) into a nice, neat CSV ready for actual use

Default output on this has random linebreaks, and table sizes are not "sortable" by size, since they use the '9.0K' and '25.4M' labels. This fixes all of that.

#BEFORE:
    PUB.PRDeduct               0    0.0B     0     0     0          0    0.0     0.0
    PUB.PrefScheme             0    0.0B     0     0     0          0    0.0     0.0
    PUB.PrefSchemeCtry                  
                            0    0.0B     0     0     0          0    0.0     0.0
    PUB.PRElecDp               0    0.0B     0     0     0          0    0.0     0.0
    PUB.PREmpDed               0    0.0B     0     0     0          0    0.0     0.0
    PUB.PREmpMas             251   98.8K   315   443   403        251    1.0     1.0
    PUB.PREmpRt                2  250.0B   125   125   125          2    1.0     1.0
    PUB.PREmpTax               0    0.0B     0     0     0          0    0.0     0.0
    PUB.Preview                0    0.0B     0     0     0          0    0.0     0.0
    PUB.PRHoldy                0    0.0B     0     0     0          0    0.0     0.0
    PUB.PriceGroup             1  126.0B   126   126   126          1    1.0     1.0
    PUB.PriceGrpValBrk                  
                               0    0.0B     0     0     0          0    0.0     0.0
    PUB.PriceLst              24    3.6K   130   175   154         24    1.0     2.6
    PUB.PriceLstGroups                  
                               0    0.0B     0     0     0          0    0.0     0.0
    PUB.PriceLstParts        761  100.5K   127   140   135        761    1.0     1.5
    PUB.PrjMkUp                0    0.0B     0     0     0          0    0.0     0.0
    PUB.PrjRoleRt              0    0.0B     0     0     0          0    0.0     0.0
    PUB.ProcessSet            10  994.0B    73   116    99         10    1.0     1.0
    PUB.ProcessTask           21    3.7K   172   193   181         21    1.0     1.0
    PUB.ProcessTaskParam                
                             877  128.7K   108   844   150        877    1.0     1.0
    PUB.ProdCal                9    3.3K   344   388   375          9    1.0     1.3
    PUB.ProdCalDay             0    0.0B     0     0     0          0    0.0     0.0

#AFTER:

    PUB.PRDeduct,0,0,0,0,0,0,0.0,0.0
    PUB.PrefScheme,0,0,0,0,0,0,0.0,0.0
    PUB.PrefSchemeCtry,0,0,0,0,0,0,0.0,0.0
    PUB.PRElecDp,0,0,0,0,0,0,0.0,0.0
    PUB.PREmpDed,0,0,0,0,0,0,0.0,0.0
    PUB.PREmpMas,251,98800,315,443,403,251,1.0,1.0
    PUB.PREmpRt,2,250,125,125,125,2,1.0,1.0
    PUB.PREmpTax,0,0,0,0,0,0,0.0,0.0
    PUB.Preview,0,0,0,0,0,0,0.0,0.0
    PUB.PRHoldy,0,0,0,0,0,0,0.0,0.0
    PUB.PriceGroup,1,126,126,126,126,1,1.0,1.0
    PUB.PriceGrpValBrk,0,0,0,0,0,0,0.0,0.0
    PUB.PriceLst,24,3600,130,175,154,24,1.0,2.6
    PUB.PriceLstGroups,0,0,0,0,0,0,0.0,0.0
    PUB.PriceLstParts,761,100500,127,140,135,761,1.0,1.5
    PUB.PrjMkUp,0,0,0,0,0,0,0.0,0.0
    PUB.PrjRoleRt,0,0,0,0,0,0,0.0,0.0
    PUB.ProcessSet,10,994,73,116,99,10,1.0,1.0
    PUB.ProcessTask,21,3700,172,193,181,21,1.0,1.0
    PUB.ProcessTaskParam,877,128700,108,844,150,877,1.0,1.0
    PUB.ProdCal,9,3300,344,388,375,9,1.0,1.3
    PUB.ProdCalDay,0,0,0,0,0,0,0.0,0.0
