<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <style>
                    body {
                    background-color: white;
                    font-family: Geneva;
                    }
                    h1 {
                    color: white;
                    text-align: center;
                    }  
                    table {
                    margin: 10px -1 330px; 
                    border: 1;
                    background: cornflowerblue
                    }
                    th {
                    background-color: yellow;
                    }
                    tr {
                    background-color: white;
                    }
                    #th0 {
                    text-align: center;
                    color: red;
                    background-color: #E6E6FA;
                    font-size:14px;
                    font-style: italic;
                    }
                </style>
            </head>
            <body> 
                <title>Statistika</title>
                <h2>Statistika</h2>
                <table>    
                    <tr>
                        <td id="th0">Ukupno: <xsl:value-of select="count(distinct-values(//autor/@ime))" /></td>
                        <td id="th0">Ukupno: <xsl:value-of select="count(//pesma/@naslovPesme)" /></td>
                        <td id="th0">Ukupno: <xsl:value-of select="count(distinct-values(//album/@naziv))" /></td>
                    </tr>
                    <tr>
                        <th>Autori</th>
                        <th>Pesme</th>
                        <th>Albumi</th>
                    </tr>
                    <xsl:for-each-group select="//autor" group-by="@ime">
                        <xsl:sort select="count(.//pesma/@naslovPesme)" data-type="number" order="descending"/>    
                        <tr> 
                            <td><xsl:value-of select="@ime" /></td> 
                            <td><xsl:number value="count(.//pesma/@naslovPesme)"/></td>
                            <td><xsl:number value="count(.//album/@naziv)"/></td>
                        </tr>  
                    </xsl:for-each-group>
                </table> 
                <table>
                    <tr>
                        <th>Muskarci</th>
                        <th>Zene</th>
                        <th>Sastavi</th>
                    </tr>  
                    <tr> 
                        <td><xsl:value-of select="count(//autor[@pol='Muski'])" /></td> 
                        <td><xsl:value-of select="count(//autor[@pol='Zenski'])" /></td>
                        <td><xsl:value-of select="count(//autor[@pol='Grupa'])" /></td>
                    </tr>  
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>