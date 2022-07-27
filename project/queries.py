
def stockcheck(ID='%', SITE='%'):

    base = '''
    WITH comb AS
    (
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.SiteID, site.DfltPOUnit
    FROM INNOINCAPP.dbo.ItemSite AS site
    LEFT JOIN INNOINCAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.SiteID, site.DfltPOUnit
    FROM INNOCNAPP.dbo.ItemSite AS site
    LEFT JOIN INNOCNAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.SiteID, site.DfltPOUnit
    FROM INNOKKAPP.dbo.ItemSite AS site
    LEFT JOIN INNOKKAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.SiteID, site.DfltPOUnit
    FROM INNOMYRAPP.dbo.ItemSite AS site
    LEFT JOIN INNOMYRAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.SiteID, site.DfltPOUnit
    FROM INNOSGDAPP.dbo.ItemSite AS site
    LEFT JOIN INNOSGDAPP.dbo.Inventory AS inv
    ON site.InvtID=inv.InvtID
    UNION ALL
    SELECT site.InvtID, inv.Descr, site.QtyAvail, site.QtyOnHand, site.SiteID, site.DfltPOUnit
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
    order = ' ORDER BY InvtID ASC'

    sqlstr = base + id + site + order
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

    SELECT TOP 100 InvtID, SiteID, LotSerNbr, QtyAvail, QtyOnHand, SrcOrdNbr
    FROM comb
    WHERE QtyOnHand > '0'
    '''
    id = " AND InvtID LIKE '" + ID + "'"
    site = " AND SiteID LIKE '" + SITE + "'"
    order = ' ORDER BY InvtID ASC'

    sqlstr = base + id + site + order
    return sqlstr
