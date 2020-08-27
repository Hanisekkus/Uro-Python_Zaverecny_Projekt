from tkinter import *
from tkinter import tix

WIDTH = 1440
HEIGHT = 900

DARK_COLOR = "#262626"
LIGHT_COLOR = "#F4F4F4"


class App( object ):

    _buy = True
    _own = True
    _usr = True
    _bookSec = { "Drama": 0, "Komedie" :  0, "Roman": 0,
                 "Kronika": 0, "Atlas" : 0, "Encyklopedie": 0,
                 "Akcni": 0, "Romance" : 0, "Historicne" : 0
                }
    _secFrame = []
    _secLabel = []
    _books =    {"Id":[ 0, 1, 2, 3, 4, 5 ],
                 "Nazev":[ "Romeo a Julie", "Figarova svatba", "Dekameron", "Božská komedie", "Sluha dvou pánů", "Odysseia"],
                 "Autor":[ "William Shakespeare", "Beaumarchais Pierre", "Boccaccio Giovanni", "Dante Alighieri", "Goldoni Carlo", "Homér"],
                 "Cena": [ 100, 90, 75, 110, 100, 150 ],
                 "Vlastneno": [ False, True, False, False, False, True ] }
    _bookFrame = []
    _bookPic = []
    _bookPicHref = []
    _bookTitle = []
    _bookAuthor = []
    _bookPrice = []
    _bookOwned = []
    _chaLabel = []
    _uchaLabel = []
    _lPan = True
    _rPan = True
    _darkSch = True

    def _colorized( self ):
        self._root.configure( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._secWin.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._footer.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelname.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelname.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._labelLogin.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelLogin.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._labelPic.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._sidePanelBG.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelBook.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelBook.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._labelOwn.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelOwn.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._labelOwnRadBut.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelBuyout.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labelBuyout.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._labelBuyoutRadBut.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._contentPanel.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._userPan.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._userLabelSch.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._userLabelSch.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._userSwitchSch.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._userLabelPri.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._userLabelPri.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._labVer.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._labVer.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._lPanHidShoBut.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._rPanHidShoBut.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._rFrame.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._cFrame.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._lFrame.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._ulFrame.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._nmBook.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._nmBook.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._auBook.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._auBook.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._cTextBox.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        self._cTextBox.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        self._butBc.config( bg = from_rgb( ( 57, 57, 57 ) ) if self._darkSch else  from_rgb( ( 230, 230, 230 ) ) )
        ## -- User icon
        self._iconUser = PhotoImage( file = "img/icon.png" )
        self._labelPic.config( image = self._iconUser ) 
        ## -- Search bar
        self._seaPic = PhotoImage( file = "img/searchField.png" if self._darkSch else "img/searchFieldLight.png" )
        self._seaBar.config( image = self._seaPic )
        self._seaIn.config( bg = from_rgb( ( 57, 57, 57 ) ) if self._darkSch else from_rgb( ( 230, 230, 230 ) ) )
        self._seaIn.config( fg = from_rgb( ( 230, 230, 230 ) ) if self._darkSch else from_rgb( ( 57, 57, 57 ) ) )
        self._seaIn.config( insertbackground = from_rgb( ( 230, 230, 230 ) ) if self._darkSch else from_rgb( ( 57, 57, 57 ) ) )
        ## -- Orders
        for book in self._bookFrame:
            book.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        for title in self._bookTitle:
            title.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
            title.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        for author in self._bookAuthor:
            author.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
            author.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        for price in self._bookPrice:
            price.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        for owned in self._bookOwned:
            owned.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
        for label in self._secLabel:
            label.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
            label.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        for label in self._uchaLabel:
            label.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
            label.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        for label in self._chaLabel:
            label.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )
            label.config( fg = LIGHT_COLOR if self._darkSch else DARK_COLOR )
        for label in self._bookPicHref:
            label.config( bg = DARK_COLOR if self._darkSch else LIGHT_COLOR )

    def __init__( self, root ):
        ## -- BEGIN
        self._root = root
        self._secWin = Frame( self._root, relief = SOLID, width = WIDTH, height = HEIGHT )
        self._secWinF( 0 )

        self._footerShadow = Frame( self._root, relief = SOLID, width = WIDTH, height = 55, background = from_rgb( ( 45, 196, 154 ) ) )
        self._footerShadow.grid()
        self._footerColored = Frame( self._footerShadow, relief = SOLID, width = WIDTH, height = 51, background = from_rgb( ( 50, 217, 169 ) ) )
        self._footerColored.place( x = 0, y = 0 )
        self._footer = Frame( self._footerShadow, relief = SOLID, width = WIDTH, height = 48 )
        self._footer.place( x = 0, y = 0 )

        self._labelname = Label( self._footerShadow, text = "Jan Kusák", font = ( "Helvetika", 16, "bold" ),
        fg = from_rgb( ( 217, 217, 217 ) ) )
        self._labelname.place( x = 1186, y = 10 )

        self._footerLoginFrame = Frame( self._footerShadow, relief = SOLID, width = 95, height = 30, background = from_rgb( ( 50, 217, 169 ) ) )
        self._footerLoginFrame.place( x = 1300, y = 10 )

        self._labelLogin = Label( self._footerLoginFrame, text = "Kus0054", font = ( "Helvetika", 16, "bold" ) )
        self._labelLogin.place( x = 2, y = 0 )

        self._labelPic = Label( self._footerShadow, relief = SOLID, highlightthickness = 0, bd = 0, cursor = "hand2" ) 
        self._labelPic.place( x = 1400, y = 8 )
        self._labelPic.bind( "<Button-1>", self._user )

        self._sidePanel = Frame( self._root, relief = SOLID, width = 300, height = HEIGHT - 75, background = from_rgb( ( 45, 196, 154 ) ) )
        self._sidePanel.place( x = 0, y = 75 )

        self._sidePanelBG = Frame( self._sidePanel, relief = SOLID, width = 298, height = HEIGHT - 75 )
        self._sidePanelBG.place( x = 0, y = 0 )

        self._labelBook = Label( self._sidePanel, text = "Knihy", font = ( "Helvetika", 30, "bold" ) )
        self._labelBook.place( x = 100, y = 25 )

        self._labelOwn = Label( self._sidePanel, text = "Vlastněné", font = ( "Helvetika", 20, "normal" ), cursor = "hand2" )
        self._labelOwn.place( x = 30, y = 110 )
        self._labelOwn.bind( "<Button-1>", self._own )

        self._labelOwnRadBut = Label( self._sidePanel, relief = SOLID, highlightthickness = 0, bd = 0, cursor = "hand2" ) 
        self._iconOwn = PhotoImage( file = "img/radioButton.png" )
        self._labelOwnRadBut.config( image = self._iconOwn, width = 34, height = 34 )
        self._labelOwnRadBut.place( x = 180, y = 113 )
        self._labelOwnRadBut.bind( "<Button-1>", self._own )

        self._labelBuyout = Label( self._sidePanel, text = "Na trhu", font = ( "Helvetika", 20, "normal" ), cursor = "hand2" )
        self._labelBuyout.place( x = 30, y = 170 )
        self._labelBuyout.bind( "<Button-1>", self._buyout )

        self._labelBuyoutRadBut = Label( self._sidePanel, relief = SOLID, highlightthickness = 0, bd = 0, cursor = "hand2" ) 
        self._iconBuy = PhotoImage( file = "img/radioButton.png" )
        self._labelBuyoutRadBut.config( image = self._iconBuy, width = 34, height = 34 )
        self._labelBuyoutRadBut.place( x = 180, y = 173 )
        self._labelBuyoutRadBut.bind( "<Button-1>", self._buyout )

        self._sidePanelCutter = Frame( self._sidePanel, relief = SOLID, width = 250, height = 2, background = from_rgb( ( 45, 196, 154 ) ) )
        self._sidePanelCutter.place( x = 25, y = 260 )

        self._contentPanel = Frame( self._root, relief = SOLID, width = WIDTH - 300, height = HEIGHT - 55 )
        self._contentPanel.place( x = 300, y = 55 )

        ## -- User Menu
        self._userF()

        ## -- Search bar
        self._seaPic = PhotoImage( file = "img/searchField.png" )
        self._seaBar = Label( self._contentPanel, relief = SOLID, image = self._seaPic, border = 0 )
        self._seaBar.place( x = 314, y = 40 )

        self._seaIn = Entry( self._seaBar, relief = SOLID, font = ( "Helvetika", 18, "italic" ), width = 36, border = 0 )
        self._seaIn.insert( END, "Najdi si svoji knížku..." )
        self._seaIn.configure(  justify = 'right' )
        self._seaIn.bind( "<Return>", self._seaInF )
        
        self._seaIn.place( x = 20, y = 18 )
        self._seaIn.focus()

        ## -- Books 
        self._crtBoo()

        ## -- Section 
        self._crtSec()

        ## -- Version frame
        self._sidePanelVer = Frame( self._sidePanel, relief = SOLID, width = 300, height = 2, background = from_rgb( ( 45, 196, 154 ) ) )
        self._sidePanelVer.place( x = 0, y = 780 )

        self._labVer = Label( self._sidePanel, text = "v.1.0.0.0", font = ( "Helvetika", 12, "bold", "italic" ), width = 29,
        background = from_rgb( ( 38, 38, 38 ) ), fg = from_rgb( ( 217, 217, 217 ) ) )
        self._labVer.place( x = 0, y = 790 )
        self._labVer.configure( anchor = "center" )

        self._colorized()
        ## -- END

    def _userF( self ):
        self._userPan = Frame( self._contentPanel, relief = SOLID, width = 260, height = 100,
         highlightthickness = 3, highlightbackground = from_rgb( ( 45, 196, 154 ) ) )
        ## -- User Dark/Light Scheme
        self._userLabelSch = Label( self._userPan, text = "Tmavý režim", font = ( "Helvetika", 12, "bold" ), width = 20 )
        self._userLabelSch.config( anchor = "w" )
        self._userLabelSch.place( x = 9, y = 15 )
        ## -- Switchers
        self._userSwitchPic = PhotoImage( file = "img/slideLSide.png")
        self._userSwitchSch = Label( self._userPan, border = 0, image = self._userSwitchPic, cursor = "hand2" )
        self._userSwitchSch.place( x = 170, y = 10 )
        self._userSwitchSch.bind( "<Button-1>", lambda event : self._userSwitchF() )
        ## -- User Cutter
        frame = Frame( self._userPan, relief = SOLID, border = 0, height = 1, width = 260, background = from_rgb( ( 45, 196, 154 ) ) )
        frame.place( x = 0, y = 50 )
        ## -- Money on account
        self._userLabelPri = Label( self._userPan, text = "Peníze na účtě: 1 000 000 Kč", font = ( "Helvetika", 12, "bold" ), width = 24 )
        self._userLabelPri.config( anchor = "c" )
        self._userLabelPri.place( x = 0, y = 60 )


    def _userSwitchF( self ):
        self._userSwitchPic = PhotoImage( file = "img/slideRSide.png" ) if self._darkSch else PhotoImage( file = "img/slideLSide.png" )
        self._darkSch = False if self._darkSch else True
        self._userLabelSch['text'] = ( "Tmavý režim" ) if self._darkSch else ( "Světlý režim" )
        self._userSwitchSch.config( image = self._userSwitchPic )
        self._userSwitchSch.place( x = 170, y = 10 )
        self._colorized()


    def _hidShoLPanF( self, event ):
        if( self._lPan ):
            self._lFrame.place_forget()
            self._lFrameBor.place_forget()
            self._ulFrame.place( x = 0, y = 0 )
            self._ulFrameBor.place( x = 0, y = 212 )
            self._cFrame.config( width = 1140 ) if self._rPan else self._cFrame.config( width = 1440 )
            self._cFrame.place( x = 0, y = 0 )
            self._lPanHidShoPic = PhotoImage( file = "img/showL.png" )
            self._lPanHidShoBut.config( image = self._lPanHidShoPic )
            self._lPanHidShoBut.place( x = 0, y = 50 )
            self._rPanHidShoBut.place( x = 1108, y = 50 ) if self._rPan else self._rPanHidShoBut.place( x = 1408, y = 50 )
            self._cTextBox.config( width = 76 ) if self._rPan else self._cTextBox.config( width = 103 )
            self._cTextBox.place( x = 250, y = 50 )
            self._lPan = False
        else:
            self._lFrame.place( x = 0, y = 0 )
            self._lFrameBor.place( x = 0, y = 0 )
            self._ulFrame.place_forget()
            self._ulFrameBor.place_forget()
            self._cFrame.config( width = 840 ) if self._rPan else self._cFrame.config( width = 1140 )
            self._cFrame.place( x = 300, y = 0 )
            self._lPanHidShoPic = PhotoImage( file = "img/hideL.png" )
            self._lPanHidShoBut.config( image = self._lPanHidShoPic )
            self._lPanHidShoBut.place( x = 0, y = 50 )
            self._rPanHidShoBut.place( x = 808, y = 50 ) if self._rPan else self._rPanHidShoBut.place( x = 1108, y = 50 )
            self._cTextBox.config( width = 67 ) if self._rPan else self._cTextBox.config( width = 94 )
            self._cTextBox.place( x = 50, y = 50 )
            self._lPan = True

    def _lPanHidShoButF( self ):
        self._lPanHidShoPic = PhotoImage( file = "img/hideL.png" )
        self._lPanHidShoBut = Label( self._cFrame , image = self._lPanHidShoPic, border = 0, cursor = "hand2" )
        self._lPanHidShoBut.place( x = 0, y = 50 )
        self._lPanHidShoBut.bind( "<Button-1>", self._hidShoLPanF )


    def _hidShoRPanF( self, event ):
        if( self._rPan ):
            self._rFrame.place_forget()
            self._rFrameBor.place_forget()
            self._cFrame.config( width = 1140 ) if self._lPan else self._cFrame.config( width = 1440 )
            self._cFrame.place( x = 300, y = 0 ) if self._lPan else self._cFrame.place( x = 0, y = 0 )
            self._rPanHidShoPic = PhotoImage( file = "img/showR.png" )
            self._rPanHidShoBut.config( image = self._rPanHidShoPic )
            self._rPanHidShoBut.place( x = 1108, y = 50 ) if self._lPan else self._rPanHidShoBut.place( x = 1408, y = 50 )
            self._cTextBox.config( width = 94 ) if self._lPan else self._cTextBox.config( width = 100 )
            self._rPan = False
        else:
            self._rFrame.place( x = 1141, y = 0 )
            self._rFrameBor.place( x = 1140, y = 0 )
            self._cFrame.config( width = 840 ) if self._lPan else self._cFrame.config( width = 1140 )
            self._cFrame.place( x = 300, y = 0 ) if self._lPan else self._cFrame.place( x = 0, y = 0 )
            self._rPanHidShoPic = PhotoImage( file = "img/hideR.png" )
            self._rPanHidShoBut.config( image = self._rPanHidShoPic )
            self._rPanHidShoBut.place( x = 808, y = 50 ) if self._lPan else self._rPanHidShoBut.place( x = 1108, y = 50 )
            self._cTextBox.config( width = 67 ) if self._lPan else self._cTextBox.config( width = 73 )
            self._rPan = True

    def _rPanHidShoButF( self ):
        self._rPanHidShoPic = PhotoImage( file = "img/hideR.png" )
        self._rPanHidShoBut = Label( self._cFrame , image = self._rPanHidShoPic, border = 0, cursor = "hand2" )
        self._rPanHidShoBut.place( x = 808, y = 50 )
        self._rPanHidShoBut.bind( "<Button-1>", self._hidShoRPanF )

    def _cText( self ):
        self._cTextBox = Text( self._cFrame, width = 67, height = 36, font = ( "Helvetika", 14, "normal" )
        , border = 0 )

        for id in range( 0, 20 ):
            self._cTextBox.insert( END, "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\n"
            +" Phasellus rhoncus. In dapibus augue non sapien. Ut tempus purus at lorem.\n"
            +" Aliquam erat volutpat. Nunc auctor. Aliquam ornare wisi eu metus.\n"
            +" Praesent in mauris eu tortor porttitor accumsan. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n"
            +" Integer in sapien.\n" )

        self._cTextBox.config( state = DISABLED )
        self._cTextBox.place( x = 50, y = 50 )

    def _secWinF( self, index ):

        ## -- Right panel
        self._rFrameBor = Frame( self._secWin, relief = SOLID, width = 300, height = HEIGHT, background = from_rgb( ( 45, 196, 154 ) ) )
        self._rFrameBor.place( x = 1140, y = 0 )
        self._rFrame = Frame( self._secWin, relief = SOLID, width = 299, height = HEIGHT )
        self._rFrame.place( x = 1141, y = 0 )

        ## -- Center panel
        self._cFrame = Frame( self._secWin, relief = SOLID, width = 840, height = HEIGHT )
        self._cFrame.place( x = 300, y = 0 )

        ## -- Left panel
        self._lFrameBor = Frame( self._secWin, relief = SOLID, width = 300, height = HEIGHT, background = from_rgb( ( 45, 196, 154 ) ) )
        self._lFrameBor.place( x = 0, y = 0 )
        self._lFrame = Frame( self._lFrameBor, relief = SOLID, width = 299, height = HEIGHT )
        self._lFrame.place( x = 0, y = 0 )

        ## -- Left panel under
        self._ulFrameBor = Frame( self._secWin, relief = SOLID, width = 200, height = 600, background = from_rgb( ( 45, 196, 154 ) ) )
        self._ulFrame = Frame( self._ulFrameBor, relief = SOLID, width = 199, height = 600 )

        ## -- Left panel hide/show button
        self._lPanHidShoButF()

        ## -- Right panel hide/show button
        self._rPanHidShoButF()

        ## -- Center text
        self._cText()

        ## -- Name of book
        self._nmBook = Label( self._lFrame, text = self._books.get( "Nazev", "" )[ index ], font = ( "Helvetika", 20, "bold" ) ) 
        self._nmBook.place( x = 47, y = 65  )
        
        ## -- Author of book
        self._auBook = Label( self._lFrame, text = self._books.get( "Autor", "" )[ index ], font = ( "Helvetika", 12, "normal" ) ) 
        self._auBook.place( x = 50, y = 100 )

        ## -- Line cut in left panel
        self._lFrameCut = Frame(  self._lFrame, relief = SOLID, width = 300, height = 2, background = from_rgb( ( 45, 196, 154 ) ) )
        self._lFrameCut.place( x = 0, y = 200 )

        self._lFrameCut = Frame(  self._lFrame, relief = SOLID, width = 300, height = 2, background = from_rgb( ( 45, 196, 154 ) ) )
        self._lFrameCut.place( x = 0, y = 800 )
                
        ## -- Chapter Creator
        self._chFrame = Frame( self._lFrame, relief = SOLID, width = 50, height = 10, background = from_rgb( ( 45, 196, 154 ) ), border = 0 )
        self._chFrame.place( x = 93, y = 274 )
        self._uchFrame = Frame( self._ulFrame, relief = SOLID, width = 50, height = 10, background = from_rgb( ( 45, 196, 154 ) ), border = 0 )
        self._uchFrame.place( x = 93, y = 74 )

        for counter in range( 0, 10 ):
            label = Label ( self._lFrame, text = "Kapitola " + str( counter + 1 ), font = ( "Helvetika", 14, "normal" ), width = 10, relief = SOLID,
             border = 0, padx = 5, pady = 5, cursor = "hand2" )
            label.bind( "<Button-1>", lambda event, index = counter : self._chChap( index ) )
            label.config( anchor = "e" )
            label.place( x = 20, y = 250 + 50 * counter )
            self._chaLabel.append( label )

            label = Label( self._ulFrame, text = "Kapitola " + str( counter + 1 ), font = ( "Helvetika", 14, "normal" ), width = 10, relief = SOLID,
             border = 0, padx = 5, pady = 5, cursor = "hand2" ) 
            label.bind( "<Button-1>", lambda event, index = counter : self._chChap( index ) )
            label.config( anchor = "e" )
            label.place( x = 20, y = 50 + 50 * counter )
            self._uchaLabel.append( label )

        ## -- Button Back
        self._butBc = Label( self._lFrame, text = "Zpátky", font = ( "Helvetika", 12, "bold" ),  width = 20, height = 2, 
        highlightthickness = 2 , fg = from_rgb( ( 191, 4, 38 ) ), relief = SOLID, cursor = "hand2" )
        self._butBc.configure( highlightbackground = from_rgb( ( 191, 4, 38 ) ), highlightcolor = from_rgb( ( 191, 4, 38 ) ) )
        self._butBc.place( x = 40, y = 827 )
        self._butBc.bind( "<Button-1>", self._bcFirWin )

    def _chChap( self, index ):
        self._chFrame.place( x = 93, y = 274 + index * 50 )
        self._uchFrame.place( x = 93, y = 74 + index * 50 )        

    def _booCli( self, index ):
        self._secWin.grid()
        self._footerShadow.grid_forget()
        self._sidePanel.place_forget()
        self._contentPanel.place_forget()
        self._secWinF( index )
        self._colorized()

    def _bcFirWin( self, event ):
        self._secWin.grid_forget()
        self._footerShadow.grid()
        self._sidePanel.place( x = 0, y = 75 )
        self._contentPanel.place( x = 300, y = 55 )
        self._lPan = True
        self._rPan = True

    def _crtBoo( self ):
        counterCol = 0
        counterRow = 0
        counter = 0

        for id in self._books.get( "Id", "" ):
            self._bookFrame.append( Frame( self._contentPanel, relief = SOLID, width = 300, height = 350, background = from_rgb( ( 38, 38, 38 ) ) ) )
            self._bookFrame[ id ].place( x = 100 + 350 * counterCol, y = 150 + 370 * counterRow )
            
            counterCol += 1
            if( counterCol == 3 ):
                counterCol = 0
                counterRow += 1

        for BooKey in self._books.keys():
            for key in self._books.get( BooKey, "" ):
                if ( BooKey == "Nazev" ):
                    self._bookPic.append( PhotoImage( file = "img/bookIcon.png" ) )
                    self._bookPicHref.append( Label( self._bookFrame[ counter ], relief = SOLID, image = self._bookPic[ counter ], border = 0, cursor = "hand2" ) )
                    self._bookPicHref[ counter ].place( x = 27, y = 0 )
                    self._bookPicHref[ counter ].bind( "<Button-1>", lambda event, index = counter : self._booCli( index ) )

                    self._bookTitle.append( Label ( self._bookFrame[ counter ], text = key, font = ( "Helvetika", 20, "bold" ), relief = SOLID, border = 0,
                    width = 18 ) )
                    self._bookTitle[ counter ].place( x = 0, y = 200 )

                    counter += 1

                if ( BooKey == "Autor" ):
                    self._bookAuthor.append( Label( self._bookFrame[ counter ], text = key, font = ( "Helvetika", 14, "normal" ), relief = SOLID, border = 0,
                    width = 28 ) )
                    self._bookAuthor[ counter ].place( x = 0, y = 250 )
            
                    counter += 1

                if ( BooKey == "Cena" ):
                    self._bookPrice.append( Label( self._bookFrame[ counter ], text = "Cena:" + str( key ) + "$", font = ( "Helvetika", 14, "bold" ), relief = SOLID, border = 0,
                    width = 25, fg = from_rgb( ( 191, 4, 38 ) ) ) )
                    self._bookPrice[ counter ].place( x = 0, y = 290 )

                    counter += 1

                if ( BooKey == "Vlastneno" ):
                    if (key):
                        self._bookOwned.append( Label( self._bookFrame[ counter ], text = "Zakoupeno", font = ( "Helvetika", 14, "bold" ), relief = SOLID, border = 0,
                        width = 25, fg = from_rgb( ( 45, 196, 154 ) ) ) )
                    else:
                        self._bookOwned.append( Label( self._bookFrame[ counter ], text = "Zakoupit", font = ( "Helvetika", 14, "bold" ), relief = SOLID, border = 0,
                        width = 25, fg = from_rgb( ( 217, 217, 217 ) ), cursor = "hand2" ) )
                    self._bookOwned[ counter ].place( x = 0, y = 320 )
                    counter += 1

            counter = 0


    def _seaInF( self, event ):
        print( "Zadana kniha" )

    def _crtSec( self ):
        
        counter = 0

        for sec in self._bookSec.keys():

            self._secFrame.append( Frame( self._sidePanel, relief = SOLID, width = 3, height = 25, background = from_rgb( ( 45, 196, 154 ) ) ) )
            self._secFrame[ counter ].place( x = 27, y = 280 + 37 * counter )
            
            self._secLabel.append( Label( self._sidePanel, text = sec, font = ( "Helvetika", 12 ), cursor = "hand2" ) )
            self._secLabel[ counter ].place( x = 30, y = 280 + 37 * counter )
            self._secLabel[ counter ].bind( "<Button-1>", lambda event, index = counter : self._cliSec( index ) )

            counter += 1    
        
        return True

    def _cliSec( self, index ):

        for frame in self._secFrame:
            frame.config( background = from_rgb( ( 45, 196, 154 ) ) )
        
        for label in self._secLabel:
            label.config( font = ( "Helvetika", 12, "normal" ))

        self._secFrame[index].config( background = from_rgb( ( 255, 176, 59 ) ) )
        self._secLabel[index].config( font = ( "Helvetika", 12, "bold", "italic" ) )

    def _user( self, event ):
        if( self._usr ):
            self._userPan.place( x = 880, y = -5)
            self._usr = False
        else:
            self._userPan.place_forget()
            self._usr = True

    def _own( self, event ):
        if( self._own ):
            self._own = False
            iconOwn = PhotoImage( file = "img/radioButtonFilled.png" )
            self._labelOwnRadBut.config( image = iconOwn )
            self._labelOwnRadBut.image = iconOwn
        else:
            self._own = True
            iconOwn = PhotoImage( file = "img/radioButton.png" )
            self._labelOwnRadBut.config( image = iconOwn )
            self._labelOwnRadBut.image = iconOwn
        

    def _buyout( self, event ):
        if( self._buy ):
            self._buy = False
            iconBuy = PhotoImage( file = "img/radioButtonFilled.png" )
            self._labelBuyoutRadBut.config( image = iconBuy )
            self._labelBuyoutRadBut.image = iconBuy
        else:
            self._buy = True
            iconBuy = PhotoImage( file = "img/radioButton.png" )
            self._labelBuyoutRadBut.config( image = iconBuy )
            self._labelBuyoutRadBut.image = iconBuy

def from_rgb( rgb ):
    return "#%02x%02x%02x" % rgb

def main():
    root = tix.Tk()
    root.wm_title( "Kus0054" )
    root.geometry( str( WIDTH ) + "x" + str( HEIGHT ) )
    root.resizable( False, False )
    app = App( root )
    root.mainloop()

main()
