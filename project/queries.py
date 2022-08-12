
from ast import Eq


def stockcheck(ID='%', SITE='%', DESC='%', EQUALITY="LIKE", QTY="QtyAvail", FILTER="%"):

    base = '''
    WITH comb AS
    (
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.QtyOnPO, site.QtyCustOrd, site.SiteID, inv.StkUnit
    FROM INNOINCAPP.dbo.ItemSite AS site
    LEFT JOIN INNOINCAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.QtyOnPO, site.QtyCustOrd, site.SiteID, inv.StkUnit
    FROM INNOCNAPP.dbo.ItemSite AS site
    LEFT JOIN INNOCNAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.QtyOnPO, site.QtyCustOrd, site.SiteID, inv.StkUnit
    FROM INNOKKAPP.dbo.ItemSite AS site
    LEFT JOIN INNOKKAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.QtyOnPO, site.QtyCustOrd, site.SiteID, inv.StkUnit
    FROM INNOMYRAPP.dbo.ItemSite AS site
    LEFT JOIN INNOMYRAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.QtyOnPO, site.QtyCustOrd, site.SiteID, inv.StkUnit
    FROM INNOSGDAPP.dbo.ItemSite AS site
    LEFT JOIN INNOSGDAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.QtyOnPO, site.QtyCustOrd, site.SiteID, inv.StkUnit
    FROM INNOTHBAPP.dbo.ItemSite AS site
    LEFT JOIN INNOTHBAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    )

    SELECT *
    FROM comb
    WHERE QtyOnHand > '0' 
    '''
    id = " AND InvtID LIKE '" + ID + "'"
    site = " AND SiteID LIKE '" + SITE + "'"
    desc = " AND Descr LIKE '" + DESC + "'"
    qty = " AND " + QTY + " " + EQUALITY + " '" + FILTER + "'"
    order = ' ORDER BY ' + QTY + ' DESC'

    sqlstr = base + id + desc + site + qty + order
    return sqlstr


def lotcheck(ID='%', SITE='%'):

    base = '''

    WITH comb AS
    (
    SELECT * FROM INNOINCAPP.dbo.LotSerMst
    UNION ALL
    SELECT * FROM INNOCNAPP.dbo.LotSerMst
    UNION ALL
    SELECT * FROM INNOKKAPP.dbo.LotSerMst
    UNION ALL
    SELECT * FROM INNOMYRAPP.dbo.LotSerMst
    UNION ALL
    SELECT * FROM INNOSGDAPP.dbo.LotSerMst
    UNION ALL
    SELECT * FROM INNOTHBAPP.dbo.LotSerMst
    )

    SELECT InvtID, SiteID, LotSerNbr, QtyAvail, QtyOnHand
    FROM comb
    WHERE QtyOnHand > '0'
    '''
    id = " AND InvtID LIKE '" + ID + "'"
    site = " AND SiteID LIKE '" + SITE + "'"
    order = ' ORDER BY InvtID ASC'

    sqlstr = base + id + site + order
    return sqlstr

'''
def itemsalescheck(ID='%', SITE='%', EQUALITY="LIKE", YEAR='%', DESC='%'):

    base = 

    WITH comb AS
    (
    SELECT [Inventory ID], [Inventory Description], [Site ID], [Site Name], [Fiscal Year], [Year To Date Sales], [Year To Date Quantity Sold] FROM INNOINCAPP.dbo.QQ_itemhist
    UNION ALL
    SELECT [Inventory ID], [Inventory Description], [Site ID], [Site Name], [Fiscal Year], [Year To Date Sales], [Year To Date Quantity Sold] FROM INNOCNAPP.dbo.QQ_itemhist
    UNION ALL
    SELECT [Inventory ID], [Inventory Description], [Site ID], [Site Name], [Fiscal Year], [Year To Date Sales], [Year To Date Quantity Sold] FROM INNOKKAPP.dbo.QQ_itemhist
    UNION ALL
    SELECT [Inventory ID], [Inventory Description], [Site ID], [Site Name], [Fiscal Year], [Year To Date Sales], [Year To Date Quantity Sold] FROM INNOMYRAPP.dbo.QQ_itemhist
    UNION ALL
    SELECT [Inventory ID], [Inventory Description], [Site ID], [Site Name], [Fiscal Year], [Year To Date Sales], [Year To Date Quantity Sold] FROM INNOSGDAPP.dbo.QQ_itemhist
    UNION ALL
    SELECT [Inventory ID], [Inventory Description], [Site ID], [Site Name], [Fiscal Year], [Year To Date Sales], [Year To Date Quantity Sold] FROM INNOTHBAPP.dbo.QQ_itemhist
    )

    SELECT * FROM comb
    WHERE [Year To Date Sales] > 0
    
    id = " AND [Inventory ID] LIKE '" + ID + "'"
    site = " AND [Site ID] LIKE '" + SITE + "'"
    year = " AND [Fiscal Year] " + EQUALITY + " '" + YEAR + "'"
    desc = " AND [Inventory Description] LIKE '" + DESC + "'"
    order = ' ORDER BY [Inventory ID] ASC'

    sqlstr = base + id + site + year + desc + order
    return sqlstr
'''

def itemsalescheck(ID='%', SITE='%', EQUALITY="LIKE", YEAR='%', DESC='%'):

    databases = ["INNOINCAPP", "INNOCNAPP", "INNOKKAPP", "INNOMYRAPP", "INNOSGDAPP", "INNOTHBAPP"]

    sqlstr = '''
    WITH comb AS
    (
    '''

    for db in databases:
        sqlstr += "SELECT "
        sqlstr += db + ".dbo.QQ_itemhist.[Inventory ID],"
        sqlstr += db + ".dbo.QQ_itemhist.[Inventory Description],"
        sqlstr += db + ".dbo.QQ_itemhist.[Site ID],"
        sqlstr += db + ".dbo.QQ_itemhist.[Site Name],"
        sqlstr += db + ".dbo.QQ_itemhist.[Fiscal Year],"
        sqlstr += db + ".dbo.QQ_itemhist.[Year To Date Sales],"
        sqlstr += db + ".dbo.QQ_itemhist.[Year To Date Quantity Sold]"
        sqlstr += '''
        FROM ''' + db + '''.dbo.QQ_itemhist '''
        
        if db != databases[-1]:
            sqlstr += '''
             UNION ALL
            '''


    sqlstr += '''
    )
    SELECT * FROM comb
    WHERE [Year To Date Sales] > 0
    '''

    sqlstr += " AND [Inventory ID] LIKE '" + ID + "'"
    sqlstr += " AND [Site ID] LIKE '" + SITE + "'"
    sqlstr += " AND [Fiscal Year] " + EQUALITY + " '" + YEAR + "'"
    sqlstr += " AND [Inventory Description] LIKE '" + DESC + "'"
    sqlstr += ' ORDER BY [Inventory ID] ASC'

    return sqlstr

'''
SELECT TOP 400 
INNOINCAPP.dbo.QQ_itemhist.[Inventory ID],
INNOINCAPP.dbo.QQ_itemhist.[Inventory Description],
INNOINCAPP.dbo.QQ_itemhist.[Site ID],
INNOINCAPP.dbo.QQ_itemhist.[Site Name],
INNOINCAPP.dbo.QQ_itemhist.[Fiscal Year],
INNOINCAPP.dbo.QQ_itemhist.[Year To Date Sales],
INNOINCAPP.dbo.QQ_itemhist.[Year To Date Quantity Sold],
INNOINCAPP.dbo.ItemXRef.AlternateID,
INNOINCAPP.dbo.ItemXRef.EntityID,
INNOINCAPP.dbo.ItemXRef.Descr
FROM INNOINCAPP.dbo.QQ_itemhist
LEFT JOIN INNOINCAPP.dbo.ItemXRef
ON INNOINCAPP.dbo.QQ_itemhist.[Inventory ID] = INNOINCAPP.dbo.ItemXRef.InvtID
WHERE INNOINCAPP.dbo.QQ_itemhist.[Year To Date Sales] > 0
'''


def vendorpoquery(SITE='%', EQUALITY="LIKE", YEAR='%', DESC='%'):


    sqlstr =    '''
    WITH comb AS (
    SELECT CpnyID, VendID, FiscYr, YTDPurch
    FROM INNOINCAPP.dbo.APHist

    UNION ALL

    SELECT CpnyID, VendID, FiscYr, YTDPurch
    FROM INNOCNAPP.dbo.APHist

    UNION ALL

    SELECT CpnyID, VendID, FiscYr, YTDPurch
    FROM INNOKKAPP.dbo.APHist

    UNION ALL

    SELECT CpnyID, VendID, FiscYr, YTDPurch
    FROM INNOMYRAPP.dbo.APHist

    UNION ALL

    SELECT CpnyID, VendID, FiscYr, YTDPurch
    FROM INNOSGDAPP.dbo.APHist

    UNION ALL

    SELECT CpnyID, VendID, FiscYr, YTDPurch
    FROM INNOTHBAPP.dbo.APHist

    )
    SELECT * FROM comb
    '''

    sqlstr += "WHERE YTDPurch > 0 AND VendID LIKE '" + DESC + "' AND FiscYr " + EQUALITY + " '" + YEAR + "' AND CpnyID LIKE '" + SITE + "'"
    sqlstr += "ORDER BY FiscYr DESC, VendID ASC"

    return sqlstr




