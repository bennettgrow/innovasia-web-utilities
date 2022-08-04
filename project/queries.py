
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


def itemsalescheck(ID='%', SITE='%', EQUALITY="LIKE", YEAR='%', DESC='%'):

    base = '''

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
    '''
    id = " AND [Inventory ID] LIKE '" + ID + "'"
    site = " AND [Site ID] LIKE '" + SITE + "'"
    year = " AND [Fiscal Year] " + EQUALITY + " '" + YEAR + "'"
    desc = " AND [Inventory Description] LIKE '" + DESC + "'"
    order = ' ORDER BY [Inventory ID] ASC'

    sqlstr = base + id + site + year + desc + order
    return sqlstr