<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output indent="yes" />
    <xsl:strip-space elements="*"/>
    <xsl:template match="text()[not(string-length(normalize-space()))]"/>
    <xsl:template match="/*">
        <xsl:copy>
            <xsl:apply-templates select="@*"/>
            <xsl:apply-templates>
                <xsl:sort select="@*" />
            </xsl:apply-templates>
        </xsl:copy>
    </xsl:template>
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()">
                <xsl:sort select="@*" />
            </xsl:apply-templates>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>