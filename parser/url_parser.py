from bs4 import BeautifulSoup
import json
import re

html = """<div id="main_sidebar">
    <div id="main_sidebar_flexroot">
      <div id="logobox">
        <a href="https://alertcalifornia.org">
          <img src="images/logo-ac-ucsd.svg" class="ac-logo" alt="ALERTCalifornia">
        </a>
      </div> <!-- logobox -->
        <div class="clear"></div>
      
      <div id="autocomplete-box-container">
       
         
            
            <div id="filter_input_widget">
          
                <div class="column">
                  <div class="name">360°</div>    
                  <div class="widget"> 
                      <label class="alert-toggle-widget">
                      <input id="filter-pano" type="checkbox" class="atw-checkbox atw-filter-pano" checked="">
                      <span class="atw-slider atw-slider-pano"></span>
                      </label>
                  </div>   
                </div>
                
                <div class="column">
                  <div class="name">Single</div>    
                  <div class="widget"> 
                      <label class="alert-toggle-widget">   
                      <input id="filter-single" type="checkbox" class="atw-checkbox atw-filter-single" checked="">
                      <span class="atw-slider"></span>
                      </label>
                  </div>   
                </div>
                <div class="column">
                  <div class="name">Offline</div>    
                  <div class="widget"> 
                      <label class="alert-toggle-widget"> 
                  <input id="filter-offline" type="checkbox" class="atw-checkbox atw-filter-offline" checked="">
                  <span class="atw-slider atw-slider-offline"></span>
                  </label>
                  </div>   
                </div>

            </div>                  
                          
            <div id="autocomplete-box">
              <input id="autocomplete-search-box" type="search" autocomplete="off" name="SuggestBox_0" class="ac-input">
              <div id="autocomplete-suggest-box" class="ac-suggest ac-hide"></div>
            </div>

         
      </div>
      

        <div id="show-on-map-widget" class="hidden">
        <div class="som-focus desktop-focus">
          <img src="images/btn-focus-01.svg" alt="">
        </div>
        <div id="som-thumb"></div>
        <div class="som-focus mobile">
          <img src="images/btn-focus-01.svg" alt="">
        </div>
        <div class="som-dismiss desktop-dismiss">
          <img src="images/btn-closefocus-01.svg" alt="">
        </div>
        <div class="som-dismiss mobile">
          <img src="images/btn-closefocus-01.svg" alt="">
        </div>
      </div>
      
      <div id="quilt"><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AlabamaHills1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Alabama Hills 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AlabamaHills2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Alabama Hills 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AlisoLaguna1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Aliso Laguna 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AlisoLaguna2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Aliso Laguna 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AllenPeak/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Allen Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Almaden1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Almaden 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Almaden2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Almaden 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-DeerCanyon1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Anaheim Deer Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-DeerCanyon2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Anaheim Deer Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AntelopeEagleLake1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Antelope Eagle Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AntelopeEagleLake2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Antelope Eagle Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AntelopeMtn/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Antelope Mtn Susanville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AntelopeYreka1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Antelope Mtn Yreka 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AntelopeYreka2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Antelope Mtn Yreka 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AnthonyPeakLookout1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Anthony Peak Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AnthonyPeakLookout2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Anthony Peak Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Arcadia1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Arcadia 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Arcadia2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Arcadia 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Argonaut/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Argonaut</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Artois/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Artois</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Artois</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Artois2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Artois 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AtascaderoHwy411/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Atascadero HWY41 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AtascaderoHwy412/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Atascadero HWY41 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Atlas/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Atlas Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-AtlasPeakWest/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Atlas Peak West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Avalon1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Avalon 1 (Catalina)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Avalon2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Avalon 2 (Catalina)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaileyCanyon1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bailey Canyon Debris Basin 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaileyCanyon2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bailey Canyon Debris Basin 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaileyPeak1/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bailey Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaileyPeak2/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bailey Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldHillEast/latest-thumb.jpg?rqts=1742521019" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Hill East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Baldhillwest/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Hill West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldJesse/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Jesse 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldJesse2/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bald Jesse 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Bald Mtn Butte 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Bald Mtn Butte 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnGuinda1/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn Guinda 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnGuinda2/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bald Mtn Guinda 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnLaPorte/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn La Porte</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnNapa/latest-thumb.jpg?rqts=1742520594" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn Napa</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnSequoia1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn Sequoia 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnSequoia2/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn Sequoia 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnTower1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn Tower (LAC) 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldMtnTower2/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bald Mtn Tower (LAC) 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldwinHills1/latest-thumb.jpg?rqts=1742507111" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Baldwin Hills 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldwinHills2/latest-thumb.jpg?rqts=1742507105" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Baldwin Hills 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldwinLake1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Baldwin Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BaldwinLake2/latest-thumb.jpg?rqts=1742507105" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Baldwin Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BallRock/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ball Rock</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Ballard Ridge 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Ballard Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BannerMtn1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Banner Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BannerMtn2/latest-thumb.jpg?rqts=1742507105" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Banner Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BarnhamNorth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barham North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BarnhamSouth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barham South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BarnabeEast/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barnabe Peak East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BarnabeWest/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barnabe Peak West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BarrRanch/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barr Ranch 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BarrRanch2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barr Ranch 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Kneeland/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Barry Ridge (Kneeland)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Bealville1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bealville 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Bealville2/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bealville 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearClover1/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Clover 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearClover2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bear Clover 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnFresno1/latest-thumb.jpg?rqts=1742520587" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Mtn Fresno 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnFresno2/latest-thumb.jpg?rqts=1742520587" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bear Mtn Fresno 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnNorth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Mtn North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnShasta/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Mtn Shasta 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnShasta2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Mtn Shasta 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnSouth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Mtn South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnKern1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Mtn. Kern 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearMtnKern2/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bear Mtn. Kern 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearPeakNorth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Peak North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearPeakSouth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bear Peak South 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BearPeakSouth2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bear Peak South 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Beckworth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Beckwourth Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Beckworth2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Beckwourth Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BelAirRidge1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bel Air Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BelAirRidge2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bel Air Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-UpperBellNorth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bell Canyon North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-UpperBellSouth/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bell Canyon South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BenBolte1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ben Bolte 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BenBolte2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Ben Bolte 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Berkeley/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Berkeley Downtown</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Berryessa/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Berryessa Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BigBlack/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Big Black Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BigJohn1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Big John</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BigRock/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Big Rock Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BigValley1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Big Valley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BigValley2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Big Valley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Biggs1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Biggs</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Birch/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Birch Hill 1 (Palomar)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Birch2/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Birch Hill 2 (Palomar)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BirdSprings1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bird Springs 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BirdSprings2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bird Springs 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlackMtnLassen1/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Black Mtn Lassen</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlackMtnMarin/latest-thumb.jpg?rqts=1742507112" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Black Mtn Marin</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-LittleBlack/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Black Mtn San Diego</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlackMtSCC/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Black Mtn SCC</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlackMtnSLO/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Black Mtn SLO</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Black Mtn. Lookout (Riverside) 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlackMtnRiverside2/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Black Mtn. Lookout (Riverside) 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Black Oak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BloomerLookout1/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bloomer Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BloomerLookout2/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bloomer Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlueCanyon/latest-thumb.jpg?rqts=1742507114" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Blue Canyon</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Blue Mountain (Modoc) 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Blue Mountain (Modoc) 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlueMtnCalaveras1/latest-thumb.jpg?rqts=1742507119" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Blue Mtn Calaveras 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlueMtnCalaveras2/latest-thumb.jpg?rqts=1742507119" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Blue Mtn Calaveras 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Blue Mtn Kern 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Blue Mtn Kern 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlueRidge1/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Blue Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BlueRidge2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Blue Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bodega Bay</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bolinas</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bonny Doon</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Boonville Mtn 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Boonville Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Boucher Hill East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Boucher Hill West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Box Springs Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Box Springs Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Box Springs Mtn East 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Box Springs Mtn East 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Brain Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Brain Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BreckenridgePeak1/latest-thumb.jpg?rqts=1742507120" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Breckenridge Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BreckenridgePeak2/latest-thumb.jpg?rqts=1742507120" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Breckenridge Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BrionesTabletop/latest-thumb.jpg?rqts=1742507120" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Briones Tabletop</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Briones-Rancho de la Rosa</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Brookdale/latest-thumb.jpg?rqts=1742507120" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Brookdale</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BryantCanyon1/latest-thumb.jpg?rqts=1742507120" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bryant Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bryant Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BuckRock1/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buck Rock 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-BuckRock2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Buck Rock 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buckhorn Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buckingham Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Buckingham Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buena Vista Amador 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buena Vista Amador 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buena Vista Kern 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Buena Vista Kern 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buffalo Bump North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Buffalo Bump South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Bunch Grass Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Bunch Grass Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Burnt Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Burnt Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Burstein</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Butler Hill 1 (South Mtn)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Butler Hill 2 (South Mtn)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Butt Lake</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cactus Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cactus Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">California Valley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">California Valley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Camarillo Ranch 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Camarillo Ranch 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cambria 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cambria 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cameron</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Canyonback Trail TCM 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Canyonback Trail TCM 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Capell Valley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Capell Valley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Carbon Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Carbon Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Carol Drive Santa Clara 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Carol Drive Santa Clara 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Cartago1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cartago 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Cartago2/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cartago 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Castanea Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Castro Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Castro Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-CedarCanyon1/latest-thumb.jpg?rqts=1742507120" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cedar Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-CedarCanyon2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cedar Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cedar Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cedar Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-CerroGordo1/latest-thumb.jpg?rqts=1742520588" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cerro Gordo 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-CerroGordo2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cerro Gordo 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Chabot</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chalk Mtn Lookout</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cherry Lake Rd</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chews Ridge Observatory</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chilcoot</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chinese Wall</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chino Hills 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Chino Hills 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chino Hills West 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Chino Hills West 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cisco Buttes 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cisco Buttes 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cleland Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cleland Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cloudcroft Debris Basin 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cloudcroft Debris Basin 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cobb Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cobb Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cohasset Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cohasset Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Colby Mtn. 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Colby Mtn. 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Cold Springs Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Coll of San Mateo Bldg10</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Coll of San Mateo Bldg36</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">College Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">College Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Crook1/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Colvin Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Crook2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Colvin Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Concow Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Constantia</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cooksie</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Coon Hollow 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Coon Hollow 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cordelia Green Valley</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Coronado Hills N</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Coronado Hills S</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cow Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cow Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cowles Mtn</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">CRD 60</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Crest 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Crest 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Crestline Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Crestline Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Crimea Fire 1 (Red Tower)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Crimea Fire 2 (Red Tower)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cross 1 (Oakview 1)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Cross 2 (Oakview 2)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">CSM Cañada Bldg 9</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ctry Club Hts 1 (Carmel)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Ctry Club Hts 2 (Carmel)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cuesta Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cuesta Peak 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Cummings Mtn 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Cummings Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cummings Skyway</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cupertino Hills</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cuyamaca Peak North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Cuyamaca Peak South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dangermond 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dangermond 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Deadmans Ridge East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Deadmans Ridge West</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Deadwood Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-Deadwood2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Deadwood Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Decker 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Decker 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Deer Creek HWY 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Deer Creek HWY 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Deer Horn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Deer Horn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Deer Park West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-DelilahLookout1/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Delilah Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-DelilahLookout2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Delilah Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Devils Garden 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Devils Garden 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dew Drop 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dew Drop 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Doe Mill Road</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dream Inn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dry Creek 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dry Creek 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ducket Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Ducket Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Duckwall 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Duckwall 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dulcinea</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-DuncanRanch1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Duncan Ranch 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-DuncanRanch2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Duncan Ranch 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dunlap Acres 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Dunlap Acres 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Dyer Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Dyer Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Eagle Rock Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Eagle Rock Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Eagles Nest</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">East Los Molinos</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">East Quincy</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Eden Valley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Eden Valley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Edith Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Edith Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Eighmy</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Eighmy 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Eighmy 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-ElPaso1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">El Paso 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-ElPaso2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">El Paso 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">El Rancho 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">El Rancho 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Elk Creek 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Elk Creek 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Elsinore Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Elsinore Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Encinal Canyon (Malibu) 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Encinal Canyon (Malibu) 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Escabroso 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Escabroso 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Evora Road</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fairview Alameda 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Fairview Alameda 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Falcons View</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-FayRanch1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fay Ranch Rd 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-FayRanch2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Fay Ranch Rd 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Felicita San Diego</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Felicita San Diego 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Figueroa 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Figueroa 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fish Rock 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Fish Rock 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fish Rock East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Flatiron East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Flatiron West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Flea Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Flea Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Flournoy</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fontana 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Fontana 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Foothills Park</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fort Jones 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fort Jones 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fowler Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fowler Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Freeman 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Freeman 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Fremont Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-GarcesHwy1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Garces HWY 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-GarcesHwy2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Garces HWY 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Garden Bar</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Garin Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Georgetown 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Georgetown 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Georgetown 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Geyser Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Geyser Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gibraltar 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Gibraltar 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Girard Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Girard Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Goat Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Goat Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gold Country</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gold Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Gold Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Golden Gate</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gonzales 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gonzales 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gorman 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Gorman 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grapevine 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Grapevine 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grass Mountain 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grass Mountain 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grass Mountain Los Angeles 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grass Mountain Los Angeles 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Greeley Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Greeley Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Green Peak North 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Green Peak South 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Greenwood Rd East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Greenwood Rd North</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Grizzly Peak 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Grizzly Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grizzly Peak KPFA</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Grizzly Peak Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Grizzly Peak Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gypsum Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Gypsum Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Gypsum Canyon South 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Gypsum Canyon South 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Halls Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Halls Ridge 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hamilton 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hamilton 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hamilton City 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hamilton City 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hamilton Mtn 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hamilton Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hammond Ranch 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Hammond Ranch 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hanging Tree 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Hanging Tree 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Happy Camp 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Happy Camp 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hawkeye Ranch</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hawkins Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hayfork Divide 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hayfork Divide 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Healdsburg 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Healdsburg 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Heaps Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Heaps Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Henrietta Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Henrietta Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Herd Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Herd Peak 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hi Mtn 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hi Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Higgins Canyon</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">High Divide 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">High Divide 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">High Glade Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">High Glade Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">High Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">High Plateau</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">High Point (North)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">High Point (South)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Highland Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Highline Trail</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Hobron</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Holiday Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Holiday Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hollywood 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Hollywood 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hopland 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Hopland 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hornbrook 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Hornbrook 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Horse Mountain 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Horse Mountain 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hotchkiss Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Hotchkiss Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Howell Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Howell Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-HuntingtonLake1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Huntington Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-HuntingtonLake2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Huntington Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">HWY 101 Blueberry 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">HWY 101 Blueberry 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Idyllwild 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Idyllwild 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Indian Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Indian Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Inks Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Inskip Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Inskip Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Iron Mountain 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Iron Mountain 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Jackson Butte 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Jackson Butte 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Jacobs Ladder</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Jarbo Gap</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Jasper Ridge Bio Presv</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-JoaquinRidge/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Joaquin Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Johnstone Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Johnstone Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Jones Ridge</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Jordan Peak 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Jordan Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Keig/ Yankee Point</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Keller Peak 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Keller Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Kelseyville 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Kelseyville 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Kennedy Mine</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Kenwood Ranch Upper 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Kenwood Ranch Upper 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-KingGeorge1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">King George Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-KingGeorge2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">King George Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Kingsville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Kregor Peak</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/unavailable-thumb2.jpg" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">KRN HQ TEST 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">La Panza</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">La Porte</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">LACFD Camp Nine 1 (Loop)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">LACFD Camp Nine 2 (Loop)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">LACFD Helibase 69 Bravo E</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">LACFD Helibase 69 Bravo W</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ladera Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ladera Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lafayette Dunsyre Dr</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lafayette Lucas Dr</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Laguna Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Laguna Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Berryessa East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Perris North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lake Perris South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Shastina</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Spaulding</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Spaulding 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Wohlford 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lake Wohlford 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lakeview Big Bear 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lakeview Big Bear 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lamont 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lamont 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lane Hill (Pescadero)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Las Virgenes 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Las Virgenes 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Laughlin Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Laughlin Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Laytonville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">League 22</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Lebec Oaks 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lebec Oaks 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lexington Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lexington Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Likely Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Likely Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lime Saddle</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Limekiln Canyon</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Little Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Little Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Logtown</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lohman Ridge (Pike)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Loma Prieta</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-LonePine1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lone Pine 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-LonePine2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lone Pine 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Longvale 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Longvale 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lopez Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Los Alamos 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Los Alamos 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Los Pinos North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Los Pinos South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lower Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lower Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lower Meyers Grade 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Lower Meyers Grade 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lower Mt Veeder 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lower Mt Veeder 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">LPD Mobile (HWY 24)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lula Vineyard</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lyons Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Lyons Peak 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Maddock Canyon</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Magic Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Magic Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mail Ridge (Satterlee)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mail Ridge 2 (Satterlee)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mammoth Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mammoth Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Marion Ridge North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Marion Ridge South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-MarzanoPeak1/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Marzano Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-MarzanoPeak2/latest-thumb.jpg?rqts=1742507122" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Marzano Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Matilija 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Matilija 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">McCabe Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">McCabe Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-McKinzieRidge/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">McKenzie Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">McKittrick Summit North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">McKittrick Summit South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Meadow Lakes 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Meadow Lakes 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Meadow Valley</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Meadowbrook 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Meadowbrook 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mebane 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mebane 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Merced 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Merced 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Merrell Rd</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mesa Grande North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mesa Grande South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Meyers</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Miami Peak 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Miami Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Milias Ranch 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Milias Ranch 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Millers Ranch 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Millers Ranch 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Minnesota Hill 1 (Fallbrook)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Minnesota Hill 2 (Fallbrook)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mission Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mission Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Moccasin Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Moccasin Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mohrhardt Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mohrhardt Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mojave Admin 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mojave Admin 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Montara Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Montebello Preserve</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Monument Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Moonraker</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Moraga Alta Mesa</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Moraga Fay Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Morgan Summit</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mount McDill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mount McDill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mountain Gate 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mountain Gate 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mt. Abel 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mt. Abel 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Adelaide 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mt. Adelaide 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Adelaide North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Allison</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Ararat 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Ararat 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Aukum 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Aukum 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Bielawski</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Bradley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Bradley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Bullion 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Bullion 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Burdell 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Burdell 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Burdell South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Chual</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Danaher</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. David (North)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. David (South)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Diablo</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mt. Diablo FLIR</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Diablo North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Diablo West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Disappointment 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Disappointment 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Elizabeth 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Elizabeth 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Emma 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Emma 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Frazier 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Frazier 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Hamilton SCC 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Hamilton SCC 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Hamilton SCC 3</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Harvard 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Harvard 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Helen 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Helen 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Jackson</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Jackson West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Konocti</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Laguna Obsv North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Laguna Obsv South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Lee N</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Lee S</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Lewis Tuolumne 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Lewis Tuolumne 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Lukens 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Lukens 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Madonna</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Oso</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Provo</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Rincon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Rincon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Rodini 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mt. Rodini 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. San Miguel North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. San Miguel South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Sanel 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mt. Sanel 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Tamalpais East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Tamalpais West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Vaca 5</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Vaca 8 North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Vaca 8 South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Vision</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Wilson East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Wilson West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Woodson</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Zion 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mt. Zion 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mtn High East 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Mtn High East 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mtn High North 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mtn High North 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mtn High West 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Mtn High West 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Muir Beach Overlook</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Mulholland Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Nichol Knob</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">North Fork 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">North Fork 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">North Placerville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">North Portola</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Nostalgia Bonsall 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Nostalgia Bonsall 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oak Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Oak Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oak Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oak Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oakland Clorox</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oakland Coliseum</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oat Mtn North 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Oat Mtn North 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oat Mtn South 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oat Mtn South 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Olancha 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Olancha 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Omo Ranch Rd 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Omo Ranch Rd 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Onyx Peak South 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Onyx Peak South 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Orcutt 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Orcutt 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oregon House</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oregon Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Oregon Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oregon Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oregon Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oroville Ca St Parks</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ortega Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ortega Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Osborn Preserve 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Osborn Preserve 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Otay Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Otay Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Outingdale</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Oven Lid 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Oven Lid 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-OwensMtn/latest-thumb.jpg?rqts=1742508102" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Owens Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-OwensMtn2/latest-thumb.jpg?rqts=1742508102" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Owens Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pacheco Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pacheco Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Palo Escrito 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Palo Escrito 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Palomar Observatory North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Palomar Observatory South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Panic Point</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Panoche Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Panoche Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Paradise Craggy 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Paradise Craggy 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Parkfield 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Parkfield 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Patton Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Patton Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Paynes Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">PCWA Auburn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">PCWA Foresthill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">PCWA Foresthill 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Pecwan 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Pecwan 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pelato Peak East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pelato Peak West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pena Adobe 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pena Adobe 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Penman Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Penman Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Penn Valley</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pepperwood Preserve</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Petaluma 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Petaluma 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Philo 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Philo 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pierce Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pierce Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pillar Point</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pilot Hill El Dorado 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pilot Hill El Dorado 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pine Creek</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pine Mountain Los Angeles 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pine Mountain Los Angeles 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pine Mtn</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Pine Mtn Kern 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Pine Mtn Kern 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Piney Creek 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Piney Creek 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pinole Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pinyon Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pinyon Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pitts</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Platte Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Platte Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pleasants North 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pleasants North 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pleasants West 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Pleasants West 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Plowshare Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pole Mtn Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pole Mtn Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ponderosa</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Poplar Lane</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Poplar Lane 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Portal Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Portal Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Portnoff Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Portnoff Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pratt Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Pratt Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Prefumo Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Prefumo Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Presson Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Presson Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Prunedale 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Prunedale 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Purissima</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Quail Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Quail Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Quail Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Quail Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Quartzite Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Quartzite Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Radio Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Radio Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rainbow Lake</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ranchita 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ranchita 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rancho Carrillo 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rancho Carrillo 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rancho Cucamonga FTC 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rancho Cucamonga FTC 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rancho La Habra 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rancho La Habra 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ranger Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Ranger Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rasnow Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rasnow Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rattlesnake Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rattlesnake Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Reche Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Reche Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Corral Rd 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Corral Rd 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mountain Riverside Co. North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mountain Riverside Co. South</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Red Mtn Del Norte 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Red Mtn Del Norte 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mtn Glenn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Red Mtn Glenn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mtn North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mtn South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mtn Ventura 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Mtn Ventura 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Red Top 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Red Top 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Redondo Mesa 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Redondo Mesa 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Redwood City 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Redwood City 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Redwood Valley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Redwood Valley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Refugio 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Refugio 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Richardson Springs Rd</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ridgeline 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Ridgeline 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ridgewood</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ridgewood Grade 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ridgewood Grade 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rimel 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Rimel 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rincon del Diablo N</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rincon del Diablo S</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rock Creek</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rockpile 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rockpile 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rocks Road 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rocks Road 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rocky Butte</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rocky Butte Trail 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rocky Butte Trail 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-RockyHill/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rocky Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-RockyHill2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rocky Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rocky Point 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rocky Point 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rocky Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rodeo Valley</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rosamond 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Rosamond 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Mtn (Modoc) 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Round Mtn (Modoc) 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-RoundMtnFresno/latest-thumb.jpg?rqts=1742508102" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Mtn Fresno</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-RoundMtnFresno2/latest-thumb.jpg?rqts=1742508102" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Mtn Fresno 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Mtn Paskenta 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Round Mtn Paskenta 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Mtn Shasta</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Mtn Shasta 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Round Top</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ruby Bluff 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Ruby Bluff 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Running Springs 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Running Springs 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Rutherford</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Saddle Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Saddle Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Saddle Timber 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Saddle Timber 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Saddleback Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Saddleback Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sage Brush Flats</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sage Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sage Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Saint John Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Saint John Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Antonio</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Benito 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">San Benito 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Benito Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">San Benito Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Bruno Mountain</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Clemente North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Clemente South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Jose Foothills</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Juan Hills North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Juan Hills South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Luis Obispo ECC</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Luis Reservoir 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">San Luis Reservoir 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Marcos Peak N</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Marcos Peak S</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Pedro</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Rafael Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Sevaine Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">San Sevaine Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">San Timoteo 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">San Timoteo 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">San Vicente 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">San Vicente 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Santa Barbara Mesa</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Santa Rita Quarry 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Santa Rita Quarry 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Santa Ynez Peak</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Santa Ynez Peak West 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Santa Ynez Peak West 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Santiago Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Santiago Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Santiago Peak CalOES N</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Santiago Peak CalOES S</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sawmill Kern 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sawmill Kern 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sawmill Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sawmill Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Schill Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Schill Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Scotts Valley</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">SE Pope Valley</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sears Point</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sedgwick Reserve Fire Lookout N</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sedgwick Reserve Fire Lookout S</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Seigler Mtn 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Seigler Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shaffer Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shandon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Shandon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shasta Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shasta Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shasta Ski Park</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shingletown</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shirley Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shirley Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Shoeinhorse Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Shoeinhorse Mtn 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sierra Buttes 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sierra Buttes 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Madre Bridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Madre Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Madre Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sierra Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Pelona 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Pelona 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sierra Vista</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sierra Vista 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Signal Peak NVCO 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Signal Peak NVCO 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">SignalPeak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">SignalPeak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Siller Bros Tower</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Silver Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Silver Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Silver Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Siri</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sites 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sites 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sky Oaks North</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sky Oaks South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Skyline 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Skyline 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Skyline College</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Slate Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sleepy Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sloan 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sloan 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sloat Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Smith Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Snag Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Snag Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Snow Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Snow Peak 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Snow Summit South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Snow Summit West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Soda Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Soda Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Soledad Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Soledad Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Somerset</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sonoma Mtn</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sonora Peak East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sonora Peak West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">South Forks Lookout 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">South Forks Lookout 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">South Mountain East 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">South Mountain East 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">South Oroville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Southworth</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Spanish Mine 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Spanish Mine 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Spinks Canyon</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">SRVFD Station 31</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">St. Helena North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">St. Helena South Napa</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Stanford Dish</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Star Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Star Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Starletta</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Starr Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Starr Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Stoney Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Stover Mtn.</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Strawberry 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Strawberry 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Strawberry Peak Arrowhead 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Strawberry Peak Arrowhead 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sugar Hill 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Sugar Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sugarloaf Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sugarloaf Shasta 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sugarloaf Shasta 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Suisun Valley</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sulphur Mtn 1 (Willet)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sulphur Mtn 2 (Willet)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunol Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunol Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunset Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sunset Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunset Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sunset Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunset Redlands 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunset Redlands 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sunset Redlands 3</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sutro Tower 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sutro Tower 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sutter Buttes</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sweeney Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Sycamore Flat 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Sycamore Flat 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Table 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Table 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Talega North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Talega South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tassajara Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tecuya Mtn 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Tecuya Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tehachapi Obsv 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Tehachapi Obsv 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tehama Carmel 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Telegraph Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Telegraph Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Temescal Trailhead 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Temescal Trailhead 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Templeton 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Templeton 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Ten Mile</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Thumb Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Thumb Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Thunder Valley Casino East</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Thunder Valley Casino West</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Timber Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Timber Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tobias Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Tobias Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-ToddEymannRd1/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Todd Eymann Rd 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-ToddEymannRd2/latest-thumb.jpg?rqts=1742520584" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Todd Eymann Rd 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Top Of The World (Laguna) 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Top Of The World (Laguna) 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Topanga Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Topanga Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Topanga Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Topanga Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Topatopa Foothills 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Topatopa Foothills 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Toro Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Toro Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tudor</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tunitas</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tuscan Butte 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Tuscan Butte 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">TV Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">TV Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Twin Sisters East 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Twin Sisters East 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Twin Sisters North 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Twin Sisters North 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Two Harbors 1 (Catalina)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Two Harbors 2 (Catalina)</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">UCSB Campus</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">UCSD Laboratory Camera 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">UCSD Laboratory Camera 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">UCSD QI Test 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">UCSD QI Test 2</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">UCSD SIO Test 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">UCSD SIO Test 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">UCSD TDLLN 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">UCSD TDLLN 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Upper Bear</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Upper Bear 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Upper Lake 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Upper Lake 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Upper Meyers Grade 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Upper Meyers Grade 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Upper Ojai 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Upper Ojai 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Vacaville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Valley Springs</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Verdugo Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Verdugo Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Volcan South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Volcan Tract III North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Volcan Tract III South</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Volcanoville</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Vollmer Peak</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Vollmer Tower Top</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Walker Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Walker Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Walnut Grove 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Walnut Grove 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Watsonville 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Watsonville 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Weed 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Weed 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Weir Canyon Eastridge 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Weir Canyon Eastridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Weir Canyon North 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Weir Canyon North 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Weir Canyon Serrano 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Weir Canyon Serrano 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">West Gonzales 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">West Gonzales 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">West Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">West Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">West Point CA</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">West Prospect Peak 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">West Prospect Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Westridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Westridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wheeler Canyon 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Wheeler Canyon 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Whipple Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Whitaker Middle Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Whitaker Middle Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Whitaker Ridge 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Whitaker Ridge 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">White Star North</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">White Star South</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-WhitneyPortal1/latest-thumb.jpg?rqts=1742508102" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Whitney Portal 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="https://cameras.alertcalifornia.org/public-camera-data/Axis-WhitneyPortal2/latest-thumb.jpg?rqts=1742508102" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Whitney Portal 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wiedemann Hill</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Wild Frontier 1</div>
  </div><div class="alert-ctt-root fadein alert-ctt-filter-hidden" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-stale">Wild Frontier 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wild Horse Valley 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Wild Horse Valley 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wildcat Canyon</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">William Rust Summit</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Williams</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Williams Hill 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Williams Hill 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Willis Peak 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Willis Peak 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Willow Creek</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wilshire 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Wilshire 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Winters 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Winters 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wolf Mtn 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wolf Mtn 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Wolfback Ridge</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Yankee Hill</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Yosemite Lakes</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Yosemite West 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Yosemite West 2</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-active">Zinfandel 1</div>
  </div><div class="alert-ctt-root fadein" draggable="true">
    <img class="alert-ctt-thumb" src="images/blank_thumb.png" width="240" height="135">
    <div class="alert-ctt-name alert-ctt-patrol">Zinfandel 2</div>
  </div></div>
    </div>
    
  </div>"""

soup = BeautifulSoup(html, "html.parser")

camera_data = []

for root_div in soup.select('div.alert-ctt-root.fadein'):
    # Find the <img> inside this .alert-ctt-root
    img_tag = root_div.find('img', class_='alert-ctt-thumb')
    if not img_tag:
        continue

    src = img_tag.get('src', '')
    # Check if src starts with cameras.alertcalifornia.org
    if src.startswith('https://cameras.alertcalifornia.org/public-camera-data/'):
        # Strip query params
        # e.g. turn "https://.../Axis-DeerCanyon1/latest-thumb.jpg?rqts=1742521019" -> "...latest-thumb.jpg"
        stripped_src = re.sub(r'\?.*$', '', src)

        # Get camera name from the adjacent .alert-ctt-name div
        name_div = root_div.find('div', class_=re.compile('alert-ctt-name'))
        camera_name = name_div.get_text(strip=True) if name_div else "Unknown"

        camera_data.append({
            "name": camera_name,
            "thumbnail_url": stripped_src
        })

# Convert to JSON (if desired)
json_output = json.dumps(camera_data, indent=2)
with open('camera_data.json', 'w') as f:
    f.write(json_output)