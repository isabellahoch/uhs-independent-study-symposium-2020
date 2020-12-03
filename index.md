<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
   <style>
    a {
        color:#ab192d !important;
    }
    .nav > li {
        margin-right: 10px;
    }
    .container {
        font-family: 'Open Sans', sans-serif !important;
    }
    .btn:focus {
        box-shadow: none !important;
    }
    .nav-tabs .nav-link:focus, .nav-tabs .nav-link:hover {
        border-color: #e9ecef #e9ecef #dee2e6;
        border-bottom-style: hidden;
    }

    .nav-tabs .nav-link {
        border: 1px solid transparent;
        border-top-left-radius: .25rem;
        border-top-right-radius: .25rem;
        color: #fff;
    }
    .nav-link .active {
        color:#000 !important
    }
   </style>
   <link href="https://fonts.googleapis.com/css2?family=Montserrat&family=Open+Sans:wght@300;400;700&display=swap&family=Luckiest+Guy&display=swap&family=Bebas+Neue&family=Roboto:wght@300;400" rel="stylesheet">
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body class="bg-light" style="background: linear-gradient(90deg, rgba(171,25,45,1) 44%, rgba(231,1,1,1) 100%) !important;">
    <div class="container">
        <!-- <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">UHS VIRTUAL CLUB FAIR</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
          
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                  <a class="nav-link" href="#" class="show-all">Browse <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Search by Type
                  </a>
                  <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#affinity-groups" id="show-affinity-groups">Affinity Group</a>
                    <a class="dropdown-item" href="#clubs" id="show-clubs">Club</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="/" class="show-all">Browse All</a>
                  </div>
                </li>
                <li class="nav-item">
                  <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                </li>
              </ul>
            </div>
          </nav> -->
          <div class="row text-center align-items-center justify-content-center" style="padding:25px">
            <img style="width:80%" src="https://drive.google.com/uc?export=view&id=1g_Ef0TgigUoPqqKm9V6O421fndpy9pxU">
            <!-- <h1>VIRTUAL CLUB FAIR</h1> -->
          </div>
        <div class="row" style="padding:25px">
            <div class="col-lg-8">
                <ul class="nav nav-tabs" style="font-family: 'Bebas Neue', cursive; color: #fff">
                    <li class="nav-item">
                    <button class="btn nav-link show-all active" id="show-all" style="font-size:1.5rem">Browse All</button>
                    </li>
                    <li class="nav-item"><button class="btn nav-link" id="show-affinity-groups" style="font-size:1.5rem">Affinity Groups</button></li>
                    <li class="nav-item"><button class="btn nav-link" id="show-clubs" style="font-size:1.5rem">Clubs</button></li>
                    <li class="nav-item"><button class="btn nav-link" id="show-carousel" style="font-size:1.5rem">Slideshow</button></li>
                    <li class="nav-item"><button class="btn nav-link" style="display:none" id="club-detail-view"></button></li>
                </ul>
            </div>
            <div class="col-lg-4" id="search-div">
                <form class="form-inline my-2 my-lg-0">
                    <!-- <input class="form-control mr-sm-2" id="search" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-danger my-2 my-sm-0" type="submit">Search</button> -->
                    <div class="form-group has-search" style="width:100%">
                        <span class="fa fa-search form-control-feedback" style="position: absolute;
                        z-index: 2;
                        display: block;
                        width: 2.375rem;
                        height: 2.375rem;
                        line-height: 2.375rem;
                        text-align: center;
                        pointer-events: none;
                        color: #aaa;"></span>
                        <input type="text" class="form-control" style="padding-left: 2.375rem; width:100%; height:50px" id="search" placeholder="Search">
                      </div>
                </form>
            </div>
        </div>
        <div class="card-columns" id="cards" style="font-family: 'Roboto', sans-serif;">
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1bZonWqkSHVC1gGGKLwwDkG6Y2tBxYUJE" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Model United Nations</strong></h5>
                        <p class="card-text">Model UN is a club dedicated to teaching students about international affairs through a UN simulation that takes place in competitive conferences. We use meetings to educate and prepare for conferences, which we attend several times throughout the year. As one of only two clubs with overnight trips, delegates have plenty of opportunities to make friends and lifelong enemies. From ordering six pints of ice cream to the hotel at 1 AM, to aggressively debating the delegation of The Seychelles, to awkwardly greeting the delegation of Italy dressed in full Roman armor, Model UN is an experience you won&#39;t forget.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emilia&amp;const_search_last_name=Fowler">Emilia Fowler</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jeanette&amp;const_search_last_name=Nguyen">Jeanette Nguyen</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Dan&amp;const_search_last_name=Huguenin">Dan Huguenin</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Rochelle&amp;const_search_last_name=Devault">Rochelle Devault</a></p>
                        <p class="card-text">Meeting Time: Wednesday Lunch</p>
                        <a href="mailto:emilia.fowler_21@sfuhs.org"><i class="fa fa-envelope"></i> emilia.fowler_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card affinity-group">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1YQ-7OVMQZsHQK9FPbBIpSUABdVgNrkwt" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">International Club</strong></h5>
                        <p class="card-text">International club will be a space for people who have citizenship in countries outside of the U.S., are from a country outside of the U.S., or have parents from a country outside of the U.S. to talk about what its like to hold membership in two places that could possibly be thousands of miles apart. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mirabelle&amp;const_search_last_name=Brettkelly">Mirabelle Brettkelly</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Isabella&amp;const_search_last_name=Hochschild">Isabella Hochschild</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Roselyne&amp;const_search_last_name=Pilaar">Roselyne Pilaar</a></p>
                        <p class="card-text">Meeting Time: Tuesday Lunch</p>
                        <a href="mailto:mirabelle.brettke_21@sfuhs.org"><i class="fa fa-envelope"></i> mirabelle.brettke_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card affinity-group">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=14K3Y3heQscDppBd-oPr92d-q-N-nF-kN" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Riot</strong></h5>
                        <p class="card-text">We are a women of color club/affinity space! We work to make sure all WOC at UHS feel comfortable in this community and provide a space for the discussion of many related issues. Although we are an affinity space, we frequently hold open meetings or meetings in collaboration with other clubs like SWEAR, Men&#39;s Group, Spectra, and more. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Maya&amp;const_search_last_name=Patel">Maya Patel</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Samantha&amp;const_search_last_name=Lee">Samantha Lee</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a></p>
                        <p class="card-text">Meeting Time: Wednesday Clubs/Affinity</p>
                        <a href="mailto:maya.patel_21@sfuhs.org"><i class="fa fa-envelope"></i> maya.patel_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card affinity-group">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1w9hu5LswmVIxBiScZ01WnV6pEbXvqIt9" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">LatinX United</strong></h5>
                        <p class="card-text">LatinX United is an affinity club for members of the UHS community who identify as LatinX. We host weekly meetings to discuss current events, connect as a community, and act as resources for each other. We also organize and host fundraisers for causes that affect LatinX people in the Bay Area and around the world.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Evan-Carlo&amp;const_search_last_name=Fowler">Evan-Carlo Fowler</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mica&amp;const_search_last_name=Clark-Herrera">Mica Clark-Herrera</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=and&amp;const_search_last_name=Brandly">Brandly Mazariegos</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jessica&amp;const_search_last_name=Osorio">Jessica Osorio </a></p>
                        <p class="card-text">Meeting Time: Tuesday Lunch</p>
                        <a href="mailto:evancarlo.fowler_21@sfuhs.org"><i class="fa fa-envelope"></i> evancarlo.fowler_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1oMZqQG5Dxi1xmW7QsYrcDbhYAjL3pB_R" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Sunrise Movement- UHS Hub</strong></h5>
                        <p class="card-text">This is a high school hub of the larger Sunrise Movement which is a non-profit working to raise awareness of and pass the Green New Deal. If enacted, the Green New Deal would force the US to become more active in fighting climate change as well as produce many sustainable jobs. 

We plan to host a space through which UHS students can take part in the political fight against climate change and take part in the Sunrise Movement. We will be discussing our thoughts on the Green New Deal, ideas we have, and current events related to the Sunrise Movement and the Green New Deal. If you are passionate about climate change and the Green New Deal as well as are interested in getting politically involved but don&#39;t necessarily know how, join use, and we can work together to hopefully one day get the Green New Deal passed. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alicia&amp;const_search_last_name=Lopez-Guerra">Alicia Lopez-Guerra</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hannah&amp;const_search_last_name=Urisman">Hannah Urisman</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Annabelle&amp;const_search_last_name=Brauer">Annabelle Brauer</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Rochelle&amp;const_search_last_name=Devault">Rochelle Devault </a></p>
                        <p class="card-text">Meeting Time: Thursday Lunch</p>
                        <a href="mailto:alicia.lopezguerr_22@sfuhs.org"><i class="fa fa-envelope"></i> alicia.lopezguerr_22@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card affinity-group">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1gWtAqOvic-aiMzAP31hLzExfnENj6Yue" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Black Student Union (BSU)</strong></h5>
                        <p class="card-text">We welcome any and all members of the UHS community who identify as being a part of the African diaspora (e.g. black, African American, black-biracial, etc.). Come out for a guaranteed good time so you&#39;re ready to hang with everyone in person when it&#39;s safe to have irl cookouts :)</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jasmine&amp;const_search_last_name=Gonzalez">Jasmine Gonzalez</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Anna&amp;const_search_last_name=Elgin">Anna Elgin</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alyanna&amp;const_search_last_name=Hughes">Alyanna Hughes</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a></p>
                        <p class="card-text">Meeting Time: Wednesday Clubs/Affinity</p>
                        <a href="mailto:jasmine.gonzalez_21@sfuhs.org"><i class="fa fa-envelope"></i> jasmine.gonzalez_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card affinity-group">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1u3Xm3qeYvmgPNB67hhgJA5C7BedKkHL-" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Financial Aid and Socio-Economic Status Club (FASES)</strong></h5>
                        <p class="card-text">FASES is a space for members of the UHS community to discuss wealth, financial aid, and the local + societal implications of both. Sometimes we&#39;ll be an affinity space for students on financial aid, and sometimes our meetings will be open to all!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jasmine&amp;const_search_last_name=Gonzalez">Jasmine Gonzalez</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Frank&amp;const_search_last_name=Wercinski">Frank Wercinski</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Chloe&amp;const_search_last_name=Richmond">Chloe Richmond</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Gaby&amp;const_search_last_name=Garcia">Gaby Garcia</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Drew&amp;const_search_last_name=Phillips">Drew Phillips </a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jenny&amp;const_search_last_name=Schneider">Jenny Schneider</a></p>
                        <p class="card-text">Meeting Time: Thursday Lunch</p>
                        <a href="mailto:jasmine.gonzalez_21@sfuhs.org"><i class="fa fa-envelope"></i> jasmine.gonzalez_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1SDHm11___kNChZi_a5a_1xSWObn5He2h" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Baking Club</strong></h5>
                        <p class="card-text">With the rise of quarantine banana bread, sourdough starters, and all sorts of pandemic baking, we thought it would be the perfect time to bring back Baking Club in a virtual environment. We&#39;ll be playing music and/or screen sharing the Great British Baking Show while we bake and chat from our own kitchens and everyone is invited to join! Each meeting, we&#39;ll all bake a recipe that we voted on the previous meeting, but you can bake whatever you want as well (it&#39;s also okay just to log on to hang out and watch other people bake!) This club is open to all students and faculty, no matter your baking skill level! (p.s. our header photo is from the Club Fair last year! Fingers crossed that we&#39;ll bring treats to more in-person meetings if we get the chance to go back on campus soon)</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Isabella&amp;const_search_last_name=Hochschild">Isabella Hochschild</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mirabelle&amp;const_search_last_name=Brettkelly">Mirabelle Brettkelly</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jessica&amp;const_search_last_name=Osorio">Jessica Osorio</a></p>
                        <p class="card-text">Meeting Time: Tuesday Lunch</p>
                        <a href="mailto:isabella.hochschi_21@sfuhs.org"><i class="fa fa-envelope"></i> isabella.hochschi_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1VxSCyWj6MufV1GDXmgG5wlRjv6UhNxpi" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Board Game Club</strong></h5>
                        <p class="card-text">A club for playing board games, especially but not limited to Secret Hitler (and now with online alternatives!)</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Pierce&amp;const_search_last_name=Hoenigman">Pierce Hoenigman</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sandeep&amp;const_search_last_name=Bhuta">Sandeep Bhuta</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">SWEAR (Students for Women&#39;s Equality and Rights)</strong></h5>
                        <p class="card-text">SWEAR (Students for Women’s Equality and Rights) is a space on campus created to discuss all things pertaining to self-identifying women/people who identify with the female experience, including current events, mental health, sex, and other various topics. We believe intersectionality is vital to any conversation about the female experience and we strive for our meetings to be welcoming to people from all backgrounds and experiences. We believe amplifying the voices of women of color at UHS is essential to our community. We host both closed and open meetings as well as events like the Mental Health Workshop and the SWEAR Sleepover.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Evers">Elizabeth Evers</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Walcott">Sarah Walcott</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sara&amp;const_search_last_name=Tagol">Sara Tagol</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lindsay&amp;const_search_last_name=Eiseman,">Lindsay Eiseman,</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Katherine&amp;const_search_last_name=Holden">Katherine Holden</a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jessica&amp;const_search_last_name=Osorio">Jessica Osorio</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1AP-Epdfzp_H4SZGc4BUKmF7tudGxK9ap" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Student Council</strong></h5>
                        <p class="card-text">Student council is a faculty-supported leadership group dedicated toward teaching students leadership skills while simultaneously assisting the school with a number of tasks. Elected students organize spirit events and interface with faculty regularly to advocate for their constituents.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=David&amp;const_search_last_name=Wignall">David Wignall</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a></p>
                        <p class="card-text">Meeting Time: Thursday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">MENA </strong></h5>
                        <p class="card-text">MENA stands for Middle Eastern North African and is an affinity space for all people who identify with the term. We mainly have closed meetings available only to those who identify as MENA to discuss topics that relate to our community.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sara&amp;const_search_last_name=Tagol">Sara Tagol</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Darius&amp;const_search_last_name=Yamini">Darius Yamini </a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Dr.&amp;const_search_last_name=Ahmed">Dr. Ahmed </a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1gjGWsrLkSdFSrdFoye1qMQ45b2EbZ1-U" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">The Devils&#39; Advocate</strong></h5>
                        <p class="card-text">The Devils&#39; Advocate is the student-run school newspaper, reporting on multiple categories, including current events, sports, arts, and more, of UHS and the world at-large. We believe that journalism has the power to make each reader’s life richer and fosters the vibrance of the UHS community. In pursuit of the truth and honoring journalistic integrity, the DA welcomes and encourages all voices to be represented in our paper. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jeanette&amp;const_search_last_name=Nguyen">Jeanette Nguyen</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Evan&amp;const_search_last_name=Carlo-Fowler">Evan Carlo-Fowler</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Zach&amp;const_search_last_name=Beischer">Zach Beischer</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ryan&amp;const_search_last_name=O&#39;Donnell">Ryan O&#39;Donnell</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=17xBTZFUg-Qhg8vDSlV3zR-9Dv9Xq2wjQ" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Rock History and Appreciation Club</strong></h5>
                        <p class="card-text">Not an affinity space.  It&#39;s a club for people to listen to, learn about, and enjoy rock music.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Maggie&amp;const_search_last_name=Carlson">Maggie Carlson</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sandeep&amp;const_search_last_name=Bhuta">Sandeep Bhuta</a></p>
                        <p class="card-text">Meeting Time: Wednesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1SuaKY2cFu8qcFiYjDpjXy-rQrFUEoqOZ" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">AAPI</strong></h5>
                        <p class="card-text">AAPI or Asian American/Pacific Islander is UHS&#39;s Asian affinity space. AAPI provides a safe space for AAPI students and faculty in the UHS community to  connect with one another and share their experiences. It is closed to those who identify as Asian, Asian American, and Pacific Islander, though some meetings will be open to all who have an interest in learning more about Asian culture. Meetings include discussions about heavier topics (ex. mental health, covid-inflicted racism, normalized cultural appropriation) as well as more light-hearted activities (ex. potlucks, movie screenings, field trips) to foster learning opportunities.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jeanette&amp;const_search_last_name=Nguyen">Jeanette Nguyen</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mason&amp;const_search_last_name=Villegas">Mason Villegas</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Cheung">Sarah Cheung</a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Pierre&amp;const_search_last_name=Carmona">Pierre Carmona</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Joanne&amp;const_search_last_name=Sugiyama">Joanne Sugiyama</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Red Cross Club</strong></h5>
                        <p class="card-text">This is a club for anyone interested in community service and public health. Due to online school, we will be meeting over zoom to discuss COVID-19, public health issues, as well as discussing drives and other activities for the future. We want to provide a space for students interested in helping their community as well as being knowledgeable about public health inequality. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sydney&amp;const_search_last_name=Srivastava">Sydney Srivastava</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jane&amp;const_search_last_name=Shvartsman">Jane Shvartsman</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a></p>
                        <p class="card-text">Meeting Time: Monday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Men of Color Group</strong></h5>
                        <p class="card-text">This is an affinity group for men of color to talk about issues or attitudes that have been perpetuated in our respective communities.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Kai&amp;const_search_last_name=Martell">Kai Martell</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Luqmaan&amp;const_search_last_name=Shaikh">Luqmaan Shaikh</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1CWJ-jp_qMol2H009SzD9pIqKlGv705Qt" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Dungeons and Dragons Club</strong></h5>
                        <p class="card-text">A club for people to play Dungeons and Dragons.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ella&amp;const_search_last_name=Barrett">Ella Barrett</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Victoria&amp;const_search_last_name=Mann">Victoria Mann</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Madeline&amp;const_search_last_name=Boyle">Madeline Boyle</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Albert&amp;const_search_last_name=Boyle">Albert Boyle</a></p>
                        <p class="card-text">Meeting Time: Monday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1fk0NpBGB_oc4tfxS-lZ00EUqtrt-yKF5" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Riot </strong></h5>
                        <p class="card-text">We are a Women of Color club/affinity space. We work to make all WOC at UHS feel comfortable in this community and to provide a space for the discussion of many, many related issues!  Although we are a closed affinity space, we frequently hold open meetings, or meetings in collaboration with other clubs like SWEAR, Men&#39;s group, Spectra, and more. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sami&amp;const_search_last_name=Lee">Sami Lee</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Maya&amp;const_search_last_name=Patel">Maya Patel</a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Tilda&amp;const_search_last_name=Kapuya">Tilda Kapuya (uncertain)</a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=180Oon8EWDpXqOyGpv55HtYLs1V56-RIn" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Understanding Whiteness</strong></h5>
                        <p class="card-text">Understanding Whiteness is a discussion space for students who identify as white. The space will be used to talk about and further understand whiteness and how that plays a role in our classrooms, clubs and other UHS spaces. We will focus on whiteness at UHS, in the Bay Area and in the world at large, and how we see whiteness appear in current events. This is a white affinity because we want to create a sustained space for the white members of the UHS community to talk about race. We will be working in partnership with the adult Understanding Whiteness group for some meetings, and hopefully with other affinity spaces as well. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Chloe&amp;const_search_last_name=Richmond">Chloe Richmond (&#39;21)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emmy&amp;const_search_last_name=Etlin">Emmy Etlin (&#39;21)</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jen&amp;const_search_last_name=Kent">Jen Kent</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1vVu2mj2nsjr33PrC2naYaE6ET7NwApu9" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Yearbook</strong></h5>
                        <p class="card-text">Yearbook is a club focused on capturing the moments shared by the UHS community. This will be an open space to all who want to participate and learn/apply aspects of graphic design and photography! Despite the fact that we may not have the chance to be together for a while, we still want to create an aspect of our school that lets all of us participate with one another. We can&#39;t wait to see what comes up!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lauren&amp;const_search_last_name=Teotico">Lauren Teotico &#39;21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Pierce&amp;const_search_last_name=Hoenigman">Pierce Hoenigman &#39;21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Janavi&amp;const_search_last_name=Padala">Janavi Padala &#39;21</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Janine&amp;const_search_last_name=Navalta">Janine Navalta &#39;22</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Faris">Elizabeth Faris</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=143xdpESH3A_Q6ZAKBN5BWszq2H7PQ9mm" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Spectra</strong></h5>
                        <p class="card-text">Spectra will serve as an affinity safe space space for LGBT+ students and faculty. In addition to providing an affinity space, we will hold open meetings and hold discussions to educate the broader UHS community about the issues our community faces.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nico&amp;const_search_last_name=Brubaker">Nico Brubaker</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=Vidal">Ariane Vidal</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hannah&amp;const_search_last_name=Urisman">Hannah Urisman</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Andrew&amp;const_search_last_name=Galatas">Andrew Galatas</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Family Matters Affinity Group</strong></h5>
                        <p class="card-text">Part of the UHS mission statement: &#34;Together we work to build and sustain a community of diverse backgrounds, perspectives, and talents.&#34; We will create a safe space for people with diverse family structures (e.g. adopted, trans-racially adopted, single parent, divorced parents, blended households, etc.) to share experiences and support each other and enlarge our visibility in the UHS community. Our goal is to acknowledge our family differences and make them more visible in the community;  when we can see each other more clearly, our community becomes stronger.
</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alex&amp;const_search_last_name=Perry">Alex Perry</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lucas&amp;const_search_last_name=Perry">Lucas Perry</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Eric&amp;const_search_last_name=Johnson">Eric Johnson</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Body Positive Club</strong></h5>
                        <p class="card-text">This club is focused on spreading body positivity and love in the UHS community and beyond. Throughout the year we will cover topics ranging from eating disorders to social media to the culture around bodies at UHS. The meetings are always open to everyone. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Evers">Elizabeth Evers</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Robbie&amp;const_search_last_name=Grisso">Robbie Grisso</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Athena&amp;const_search_last_name=Nooney">Athena Nooney</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a></p>
                        <p class="card-text">Meeting Time: Thursday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1dT7fV3YwhOCkmAwWK7cDspJG8giKp2nN" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Jewish Club</strong></h5>
                        <p class="card-text">Jewish Club welcomes all members of the UHS community to discuss different aspects of the Jewish identity. Together, we will celebrate holidays, discuss controversies in the Jewish community and exchange stories of different Jewish experiences. In the past, some of our most successful meetings have been about Jews and sports, Israel and Palestine, and Jewish comedy. We encourage you to come to our meetings, whether you identify as Jewish, Jew-ish or neither!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emmy&amp;const_search_last_name=Etlin">Emmy Etlin (‘21)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Eve&amp;const_search_last_name=Andersen">Eve Andersen (‘21)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Noah&amp;const_search_last_name=Mays-Smith">Noah Mays-Smith (‘22)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jacob&amp;const_search_last_name=Neplokh">Jacob Neplokh (‘23)</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Carol&amp;const_search_last_name=Coles">Carol Coles</a></p>
                        <p class="card-text">Meeting Time: Thursday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1ttXHVyJTOQ7wBtLrMUYHu1imjdGnWV3a" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Interfaith</strong></h5>
                        <p class="card-text">Interfaith is a club for students and faculty to have open conversations about faith and spirituality. With UHS being a secular school, we recognize that it may be difficult to find safe spaces to discuss faith; therefore, we hope to provide such a space with our club. We would also like to emphasize that we are not an affinity group; anyone is welcome at our meetings, regardless of their religious affiliation or lack thereof. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=Vidal">Ariane Vidal</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Erica&amp;const_search_last_name=Cooper">Erica Cooper</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Clarissa&amp;const_search_last_name=Dann">Clarissa Dann</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Kate&amp;const_search_last_name=Garrett">Kate Garrett</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Book Club</strong></h5>
                        <p class="card-text">For our club, we plan to read a book and discuss it and possibly discuss movies too. It will take a while to read the book or watch the movie so we won&#39;t meet consecutively.  

We invite everyone to come out. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jack&amp;const_search_last_name=Clancy">Jack Clancy</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hayley&amp;const_search_last_name=Beale">Hayley Beale </a></p>
                        <p class="card-text">Meeting Time: TBD</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1LzLOB0I_eCVo1O6cBKd03arznTpnXwff" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Financial Aid and Socio-Economic Status  (FASES)</strong></h5>
                        <p class="card-text">FASES is a club focused on addressing and tackling issues of socio-economic status and wealth within our community and beyond. We hold both affinity meetings for students on financial aid and open meetings for all to attend.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jasmine&amp;const_search_last_name=Gonzalez">Jasmine Gonzalez</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Frank&amp;const_search_last_name=Wercinski">Frank Wercinski</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Chloe&amp;const_search_last_name=Richmond">Chloe Richmond</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Drew&amp;const_search_last_name=Phillips">Drew Phillips</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Gaby&amp;const_search_last_name=Garcia">Gaby Garcia</a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jenny&amp;const_search_last_name=Schneider">Jenny Schneider</a></p>
                        <p class="card-text">Meeting Time: Thursday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">BioMed club</strong></h5>
                        <p class="card-text">BioMed club is focusing on topics such as vaccine development, clinical trials, and health inequalities. We aim to have speakers every other month covering different topics and meetings in between speakers to debrief and learn about our next speaker. There&#39;s no need to come to every meeting; if you see a topic that interests you feel free to drop in!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lucy&amp;const_search_last_name=Falzone">Lucy Falzone</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Meryl&amp;const_search_last_name=Sampson">Meryl Sampson</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emma&amp;const_search_last_name=Hartmann">Emma Hartmann</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1wyrKwmQ5qOBkhg59tobzl-5pL0wYR6BM" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">UNICEF Club</strong></h5>
                        <p class="card-text">We are focused on fundraising, advocacy/raising awareness, community building, and volunteering locally. This is a club open to everyone and we would love new faces! </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mirabel&amp;const_search_last_name=Haskin">Mirabel Haskin Fernald</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Katie&amp;const_search_last_name=Crawford">Katie Crawford</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=undecided-&amp;const_search_last_name=we">undecided- we will email Alexandra when we know. </a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1biN1bF3j2qp61vNp1uCHLBlWNJNE2ShF" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Science Olympiad</strong></h5>
                        <p class="card-text">A chill club to explore scientific topics not formally taught by UHS and a chance to pursue other scientific interests with your peers in a semi-competitive or fun and experimental environment. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Christian&amp;const_search_last_name=Canete">Christian Canete</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Cheung">Sarah Cheung</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ella&amp;const_search_last_name=Barrett">Ella Barrett</a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Luke&amp;const_search_last_name=Probst">Luke Probst</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ozzie&amp;const_search_last_name=Nevarez">Ozzie Nevarez</a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Men&#39;s Group</strong></h5>
                        <p class="card-text">Men&#39;s Group strives to be a space for men to examine, critique, and reflect on issues of masculinity, as well as a safe space for men to be open and vulnerable. We will have some meetings, closed to self-indentified males. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Owen&amp;const_search_last_name=Myers">Owen Myers (2021)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Drew&amp;const_search_last_name=Phillips">Drew Phillips (2021)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Frank&amp;const_search_last_name=Wercinski">Frank Wercinski (2021)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Luqmaan&amp;const_search_last_name=Shaikh">Luqmaan Shaikh (2021)</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Marcus&amp;const_search_last_name=Caimi">Marcus Caimi</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1X800rNe-dESui73xF6zMMm9WShH6Q2kx" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Disney Club</strong></h5>
                        <p class="card-text">We plan on doing screenings of your favorite Disney and Pixar movies! We are always open to suggestions so if you have a childhood fav you&#39;d like us to screen, let us know. Anyone who still feels like a child at heart is encouraged to come :) </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Katie&amp;const_search_last_name=Hartel">Katie Hartel</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sara&amp;const_search_last_name=Tagol">Sara Tagol</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Schaffernoth">Elizabeth Schaffernoth</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1r4zT6QBHRw4yNHs8Q_rkRac9gAjFByUu" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Satonics</strong></h5>
                        <p class="card-text">This club is UHS’s a cappella group and is open to anyone who is accepted via an informal audition. We make music entirely with our voices and sing a variety of music, from pop songs to jazz arrangements, and perform at concerts and competitions. We will be holding auditions through Zoom next Friday (29th) and Saturday (30th), with more information to sign up in an email. We especially encourage underclassmen and those with lower voices to audition! Until further notice from the high school a cappella competition we participate in (Varsity Vocals ICHSA), our group will perform for school concerts through pre-recorded songs.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Cheung">Sarah Cheung</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Matthew&amp;const_search_last_name=Gin,">Matthew Gin,</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Madelyn&amp;const_search_last_name=Ocker">Madelyn Ocker</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Joel&amp;const_search_last_name=Chapman">Joel Chapman</a></p>
                        <p class="card-text">Meeting Time: Monday lunch</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1iRw4xM3-Ss7EvGAItqS2jeVYPSppBvdv" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Multiracial Club</strong></h5>
                        <p class="card-text">An affinity space for students and faculty that self-identify as biracial or multiracial. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Arianna&amp;const_search_last_name=Schwartz">Arianna Schwartz ’22</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Phia&amp;const_search_last_name=Black">Phia Black ’23</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Owen&amp;const_search_last_name=Myers">Owen Myers ’21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Amelie&amp;const_search_last_name=Scheil">Amelie Scheil &#39;21</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lauren&amp;const_search_last_name=Schneider">Lauren Schneider &#39;21</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1UgyFO_nPxNFkkr_EXDUL6gY6fxzD9rwv" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Artivism Club</strong></h5>
                        <p class="card-text">The purpose of Artivism club is to explore the intersection of art and activism, through art projects, fundraisers, and club meetings. We plan to collaborate with clubs such as BSU, Riot, and SWEAR in order to explore art as a vehicle for social justice. Previous projects include a mural for Summerbridge (featured in the hallway of Upper campus), poster-making sessions, and lunch workshops on color theory/design principles. Our meetings are open to everyone, regardless of identity or prior artistic experience! </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Amelie&amp;const_search_last_name=Scheil">Amelie Scheil</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jiho&amp;const_search_last_name=Lee">Jiho Lee</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jenifer&amp;const_search_last_name=Kent">Jenifer Kent</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1ilPU8lENicf97gsFnfbO56i5T9cqV57J" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Girls Who Code</strong></h5>
                        <p class="card-text">Girls Who Code is a national non-profit organization working to close the gender gap in technology. Our club educates, equips, and inspires girls with the computing skills they&#39;ll need to pursue 21st-century opportunities.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Amelie&amp;const_search_last_name=Scheil">Amelie Scheil &#39;21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Isabella&amp;const_search_last_name=Hochschild">Isabella Hochschild &#39;21</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alicia&amp;const_search_last_name=Lopez-Guerra">Alicia Lopez-Guerra &#39;22</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Leah&amp;const_search_last_name=Dorazio">Leah Dorazio</a></p>
                        <p class="card-text">Meeting Time: Monday lunch</p>
                        <a href="mailto:amelie.scheil_21@sfuhs.org"><i class="fa fa-envelope"></i> amelie.scheil_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1Nv-_3OZIR3FI1Z4P0BGK_CRtBghmwvRt" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Hapa (half white half asian affinity group)</strong></h5>
                        <p class="card-text">Hapa is a term used to describe a person who is half asian and half white. This affinity group, with closed meetings, will delve into the complexity that arises with a dual identity. </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Anna&amp;const_search_last_name=Neumann-Loreck">Anna Neumann-Loreck</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lauren&amp;const_search_last_name=Schneider">Lauren Schneider</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Andrew&amp;const_search_last_name=Galatas">Andrew Galatas </a></p>
                        <p class="card-text">Meeting Time: Thursday lunch</p>
                        <a href="mailto:lauren.schneider_21@sfuhs.org"><i class="fa fa-envelope"></i> lauren.schneider_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1M4wtD2PLLN4TN94RMQRujwIsQ9SGFh_V" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Avatar: The Last Airbender Club</strong></h5>
                        <p class="card-text">Our club welcomes fans of the Avatar universe, including Avatar: The Last Airbender and Legend of Korra. I think we can all agree that it is the best show ever written, so we decided to make a club to appreciate its brilliance. We will watch episodes, discuss opinions and themes, take fun &#34;which bender am I&#34; quizzes and appreciate the show and its excellence.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=Vidal">Ariane Vidal</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hannah&amp;const_search_last_name=Urisman">Hannah Urisman</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Adrian&amp;const_search_last_name=Acu">Adrian Acu</a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        <a href="mailto:hannah.urisman_22@sfuhs.org"><i class="fa fa-envelope"></i> hannah.urisman_22@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1ZnMS1INYZDiydg5lmq5WPDAvAQpedMIi" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Conservative Club</strong></h5>
                        <p class="card-text">UHS Conservative Club is a club dedicated to promoting substantive discussion of political ideas. We believe that when 80% of liberal students feel confident sharing their political views, but 80% of conservative students do not, real debate can never be achieved. To join, you don&#39;t need to hold any particular viewpoints on any issue, and you don&#39;t even need to be conservative (in fact, we welcome and value differing perspectives). All you need to believe is that UHS, and the United States as a whole, will be a better place if we allow open and honest debate and exchange of ideas, and that echo chambers aren&#39;t good for anyone. Our goal is to provide a forum for conservative thought that is mainstream in the United States, but not often represented at UHS.

We will meet every few weeks to discuss current events, the political climate on campus and in the country, or host a guest speaker.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Dan&amp;const_search_last_name=Huguenin">Dan Huguenin</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Tyler&amp;const_search_last_name=Sisitsky">Tyler Sisitsky</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Kate&amp;const_search_last_name=Garrett">Kate Garrett</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        <a href="mailto:dan.huguenin_21@sfuhs.org"><i class="fa fa-envelope"></i> dan.huguenin_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1LnaXI2SXVKV7XrUJj68h3vSKzChiIsow" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">White Folks Committed to Anti-Racism Affinity Space</strong></h5>
                        <p class="card-text">“I can’t build externally what I haven’t built internally.”
Dr. Cornel West
 
 
This is an invitation for all folks who identify as white and are striving toward an identity of anti-racist. This is a space to gather and process the complexity of what it means to be white identifying human beings at this time with a focus on building a competent and firm foundation of anti-racism. This is a supportive and safe space. We will make mistakes. We will have all the best intentions and still have a negative impact. This is a space to learn and grow together, that our intentions may align with our actions, that we may shift to being influential as opposed to impactful. We will bring all our humanness to the table and hold space for all of it.
 </p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=(we&amp;const_search_last_name=want">(we want but don&#39;t have yet!)</a></p>
                        <p class="card-text">Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lindsay&amp;const_search_last_name=Repko">Lindsay Repko</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lisa&amp;const_search_last_name=Carroll">Lisa Carroll</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        <a href="mailto:lisa.carroll@sfuhs.org"><i class="fa fa-envelope"></i> lisa.carroll@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Mental Health Coalition</strong></h5>
                        <p class="card-text">Mental Health Advocacy</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=TBD:&amp;const_search_last_name=currently">TBD: currently in process</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lindsay&amp;const_search_last_name=Repko">Lindsay Repko (may add others)</a></p>
                        <p class="card-text">Meeting Time: Tuesday lunch</p>
                        <a href="mailto:lindsay.repko@sfuhs.org"><i class="fa fa-envelope"></i> lindsay.repko@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">HIstory of History of History of History of Surf Club Club Club Club Club</strong></h5>
                        <p class="card-text">This club will tell the historic odyssey of surf club at UHS. It will then delve deeper into topics of surf history and culture. From there, we will approach a variety of modern issues such as global warming, environmental preservation and sustainability, and more.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ren&amp;const_search_last_name=Zanze">Ren Zanze (President)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mica&amp;const_search_last_name=(President)">Mica (President)  </a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Scott&amp;const_search_last_name=Laughlin">Scott Laughlin</a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        <a href="mailto:ren.zanze_21@sfuhs.org"><i class="fa fa-envelope"></i> ren.zanze_21@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1e74BJbPfHCyirNbM4MExRl3h_7QralGf" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Women&#39;s Health Club</strong></h5>
                        <p class="card-text">The mission of our club is to spread awareness about how common sexual assault/rape is in our society and educate students through stories, guest speakers, social media, documentaries, and other sources. We hope to become advocates for change by working with organizations in San Francisco as well as providing a safe space for UHS students to learn and talk about these issues. This club will have a few closed meetings but will mostly be open for everyone.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ria&amp;const_search_last_name=Dhillon">Ria Dhillon</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Malia&amp;const_search_last_name=House">Malia House</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Barbara&amp;const_search_last_name=Holler">Barbara Holler </a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        <a href="mailto:malia.house_22@sfuhs.org"><i class="fa fa-envelope"></i> malia.house_22@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1NRLA2QMsogjPDLYodEcZylLaSaCA6CnQ" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">The Radio Broadcast Club</strong></h5>
                        <p class="card-text">In this club we will listen to old radio theater broadcasts as well as rewrite them or recreate them! As a form of online drama!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Harper&amp;const_search_last_name=Clementz">Harper Clementz (10th) </a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=(11th)">Ariane (11th)</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ryan&amp;const_search_last_name=O’Donnell">Ryan O’Donnell </a></p>
                        <p class="card-text">Meeting Time: Friday lunch</p>
                        <a href="mailto:harper.clementz_23@sfuhs.org"><i class="fa fa-envelope"></i> harper.clementz_23@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1KLk4U3iXsTpiP4IfoYO1QuLHydSTBmPi" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">UHS Business Club</strong></h5>
                        <p class="card-text">Selling short; econometrics; balance sheets...what does this all mean? The UHS Business Club provides opportunities for its members to learn about the inner workings of the business world. Through activities such as case studies, ethical debates, and projects, we will introduce our club members to careers in the business sector, current events in the finance field, and experimentation with basic business transactions. With introductions to management, marketing and investing games, get ready for some fun dives into the business world. We are open to all who would like to join!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mericel&amp;const_search_last_name=Tao">Mericel Tao</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Caroline&amp;const_search_last_name=Hall-Sherr">Caroline Hall-Sherr</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=David&amp;const_search_last_name=Roth">David Roth</a></p>
                        <p class="card-text">Meeting Time: Monday lunch</p>
                        <a href="mailto:mericel.tao_22@sfuhs.org"><i class="fa fa-envelope"></i> mericel.tao_22@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=121_Q-W2qgbuep_Bl5Rms8v8Uh2DHuze2" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">UHS SWENext Club</strong></h5>
                        <p class="card-text">From bridges to spaceships, computers to cars, engineers are the force behind many of the objects we interact with. The Society of Women Engineers (SWE) seeks to increase the representation of women in the engineering field and revamp the dynamics of the engineering workforce. Our UHS SWENext Club combines group activities, discussions about current events in engineering, and lessons about engineering to expand on SWE’s mission of empowering women engineers. Most of the activity and learning based meetings will be open to non-male identifying students, but meetings discussing current events will be open to all!</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Danielle&amp;const_search_last_name=Cuthbert">Danielle Cuthbert</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mericel&amp;const_search_last_name=Tao">Mericel Tao</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Megan&amp;const_search_last_name=Storti">Megan Storti</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        <a href="mailto:danielle.cuthbert_22@sfuhs.org"><i class="fa fa-envelope"></i> danielle.cuthbert_22@sfuhs.org</a>
                    </div>
                </div>
            
                <div class="card club">
                <img class="card-img-top" src="https://drive.google.com/uc?export=view&amp;id=1gzLIHou05Ff8ukISzaEUHX3q6aEHHPCF" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title"><strong style="color: #ab192d;">Investment Club</strong></h5>
                        <p class="card-text">This is a club open to all students with an interest in investing and the financial world. No experience is required, we’ll learn together how to track a portfolio and research stocks. The club will have various speakers with years of experience in finance and will be an interactive space for students to learn more about investing.</p>
                        <p class="card-text">Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Owen&amp;const_search_last_name=Flanagan">Owen Flanagan</a></p>
                        <p class="card-text">Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Michael&amp;const_search_last_name=Novak">Michael Novak (UHS Chief Financial Operations Officer)</a></p>
                        <p class="card-text">Meeting Time: Wednesday clubs/affinity</p>
                        <a href="mailto:owen.flanagan_21@sfuhs.org"><i class="fa fa-envelope"></i> owen.flanagan_21@sfuhs.org</a>
                    </div>
                </div>
            
            <!-- <div class="card p-3">
            <blockquote class="blockquote mb-0 card-body">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                <footer class="blockquote-footer">
                <small class="text-muted">
                    Someone famous in <cite title="Source Title">Source Title</cite>
                </small>
                </footer>
            </blockquote>
            </div>
            <div class="card">
            <img class="card-img-top" src="..." alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
            </div>
            <div class="card bg-primary text-white text-center p-3">
            <blockquote class="blockquote mb-0">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat.</p>
                <footer class="blockquote-footer">
                <small>
                    Someone famous in <cite title="Source Title">Source Title</cite>
                </small>
                </footer>
            </blockquote>
            </div>
            <div class="card text-center">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This card has supporting text below as a natural lead-in to additional content.</p>
                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
            </div>
            <div class="card">
            <img class="card-img" src="..." alt="Card image">
            </div>
            <div class="card p-3 text-right">
            <blockquote class="blockquote mb-0">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
                <footer class="blockquote-footer">
                <small class="text-muted">
                    Someone famous in <cite title="Source Title">Source Title</cite>
                </small>
                </footer>
            </blockquote>
            </div>
            <div class="card">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This card has even longer content than the first to show that equal height action.</p>
                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
            </div> -->
        </div>
        <div id="carousel" class="carousel slide" data-ride="carousel" data-interval=2000 style="display:none">
            <ol class="carousel-indicators">
              <li data-target="#carousel" data-slide-to="0" class="active"></li>
              
              
              
              
              <li data-target="#carousel" data-slide-to="1"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="2"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="3"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="4"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="5"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="6"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="7"></li>
              
              
              
              
              
              <li data-target="#carousel" data-slide-to="1"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="3"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="4"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="6"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="7"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="8"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="9"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="10"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="11"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="12"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="13"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="14"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="15"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="19"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="20"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="21"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="22"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="23"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="25"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="27"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="28"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="29"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="30"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="31"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="32"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="33"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="34"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="35"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="37"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="38"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="39"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="40"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="41"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="42"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="43"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="44"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="45"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="46"></li>
              
              
              
              <li data-target="#carousel" data-slide-to="47"></li>
              
              
            </ol>
            <div class="carousel-inner">
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1bZonWqkSHVC1gGGKLwwDkG6Y2tBxYUJE" alt="Model United Nations">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="model-united-nations-link" style="background-color:#fff;color:#000 !important">Model United Nations</button></h5>
                    <p>Model UN is a club dedicated to teaching students about international affairs through a UN simulation that takes place in competitive conferences. We use meetings to educate and prepare for conferences, which we attend several times throughout the year. As one of only two clubs with overnight trips, delegates have plenty of opportunities to make friends and lifelong enemies. From ordering six pints of ice cream to the hotel at 1 AM, to aggressively debating the delegation of The Seychelles, to awkwardly greeting the delegation of Italy dressed in full Roman armor, Model UN is an experience you won&#39;t forget.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1YQ-7OVMQZsHQK9FPbBIpSUABdVgNrkwt" alt="International Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="international-club-link" style="background-color:#fff;color:#000 !important">International Club</button></h5>
                    <p>International club will be a space for people who have citizenship in countries outside of the U.S., are from a country outside of the U.S., or have parents from a country outside of the U.S. to talk about what its like to hold membership in two places that could possibly be thousands of miles apart. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=14K3Y3heQscDppBd-oPr92d-q-N-nF-kN" alt="Riot">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="riot-link" style="background-color:#fff;color:#000 !important">Riot</button></h5>
                    <p>We are a women of color club/affinity space! We work to make sure all WOC at UHS feel comfortable in this community and provide a space for the discussion of many related issues. Although we are an affinity space, we frequently hold open meetings or meetings in collaboration with other clubs like SWEAR, Men&#39;s Group, Spectra, and more. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1w9hu5LswmVIxBiScZ01WnV6pEbXvqIt9" alt="LatinX United">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="latinx-united-link" style="background-color:#fff;color:#000 !important">LatinX United</button></h5>
                    <p>LatinX United is an affinity club for members of the UHS community who identify as LatinX. We host weekly meetings to discuss current events, connect as a community, and act as resources for each other. We also organize and host fundraisers for causes that affect LatinX people in the Bay Area and around the world.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1oMZqQG5Dxi1xmW7QsYrcDbhYAjL3pB_R" alt="Sunrise Movement- UHS Hub">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="sunrise-movement--uhs-hub-link" style="background-color:#fff;color:#000 !important">Sunrise Movement- UHS Hub</button></h5>
                    <p>This is a high school hub of the larger Sunrise Movement which is a non-profit working to raise awareness of and pass the Green New Deal. If enacted, the Green New Deal would force the US to become more active in fighting climate change as well as produce many sustainable jobs. 

We plan to host a space through which UHS students can take part in the political fight against climate change and take part in the Sunrise Movement. We will be discussing our thoughts on the Green New Deal, ideas we have, and current events related to the Sunrise Movement and the Green New Deal. If you are passionate about climate change and the Green New Deal as well as are interested in getting politically involved but don&#39;t necessarily know how, join use, and we can work together to hopefully one day get the Green New Deal passed. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1gWtAqOvic-aiMzAP31hLzExfnENj6Yue" alt="Black Student Union (BSU)">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="black-student-union-(bsu)-link" style="background-color:#fff;color:#000 !important">Black Student Union (BSU)</button></h5>
                    <p>We welcome any and all members of the UHS community who identify as being a part of the African diaspora (e.g. black, African American, black-biracial, etc.). Come out for a guaranteed good time so you&#39;re ready to hang with everyone in person when it&#39;s safe to have irl cookouts :)</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1u3Xm3qeYvmgPNB67hhgJA5C7BedKkHL-" alt="Financial Aid and Socio-Economic Status Club (FASES)">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="financial-aid-and-socio-economic-status-club-(fases)-link" style="background-color:#fff;color:#000 !important">Financial Aid and Socio-Economic Status Club (FASES)</button></h5>
                    <p>FASES is a space for members of the UHS community to discuss wealth, financial aid, and the local + societal implications of both. Sometimes we&#39;ll be an affinity space for students on financial aid, and sometimes our meetings will be open to all!</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1SDHm11___kNChZi_a5a_1xSWObn5He2h" alt="Baking Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="baking-club-link" style="background-color:#fff;color:#000 !important">Baking Club</button></h5>
                    <p>With the rise of quarantine banana bread, sourdough starters, and all sorts of pandemic baking, we thought it would be the perfect time to bring back Baking Club in a virtual environment. We&#39;ll be playing music and/or screen sharing the Great British Baking Show while we bake and chat from our own kitchens and everyone is invited to join! Each meeting, we&#39;ll all bake a recipe that we voted on the previous meeting, but you can bake whatever you want as well (it&#39;s also okay just to log on to hang out and watch other people bake!) This club is open to all students and faculty, no matter your baking skill level! (p.s. our header photo is from the Club Fair last year! Fingers crossed that we&#39;ll bring treats to more in-person meetings if we get the chance to go back on campus soon)</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1VxSCyWj6MufV1GDXmgG5wlRjv6UhNxpi" alt="Board Game Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="board-game-club-link" style="background-color:#fff;color:#000 !important">Board Game Club</button></h5>
                    <p>A club for playing board games, especially but not limited to Secret Hitler (and now with online alternatives!)</p>
                  </div>
              </div>
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1AP-Epdfzp_H4SZGc4BUKmF7tudGxK9ap" alt="Student Council">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="student-council-link" style="background-color:#fff;color:#000 !important">Student Council</button></h5>
                    <p>Student council is a faculty-supported leadership group dedicated toward teaching students leadership skills while simultaneously assisting the school with a number of tasks. Elected students organize spirit events and interface with faculty regularly to advocate for their constituents.</p>
                  </div>
              </div>
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1gjGWsrLkSdFSrdFoye1qMQ45b2EbZ1-U" alt="The Devils&#39; Advocate">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="the-devils&#39;-advocate-link" style="background-color:#fff;color:#000 !important">The Devils&#39; Advocate</button></h5>
                    <p>The Devils&#39; Advocate is the student-run school newspaper, reporting on multiple categories, including current events, sports, arts, and more, of UHS and the world at-large. We believe that journalism has the power to make each reader’s life richer and fosters the vibrance of the UHS community. In pursuit of the truth and honoring journalistic integrity, the DA welcomes and encourages all voices to be represented in our paper. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=17xBTZFUg-Qhg8vDSlV3zR-9Dv9Xq2wjQ" alt="Rock History and Appreciation Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="rock-history-and-appreciation-club-link" style="background-color:#fff;color:#000 !important">Rock History and Appreciation Club</button></h5>
                    <p>Not an affinity space.  It&#39;s a club for people to listen to, learn about, and enjoy rock music.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1SuaKY2cFu8qcFiYjDpjXy-rQrFUEoqOZ" alt="AAPI">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="aapi-link" style="background-color:#fff;color:#000 !important">AAPI</button></h5>
                    <p>AAPI or Asian American/Pacific Islander is UHS&#39;s Asian affinity space. AAPI provides a safe space for AAPI students and faculty in the UHS community to  connect with one another and share their experiences. It is closed to those who identify as Asian, Asian American, and Pacific Islander, though some meetings will be open to all who have an interest in learning more about Asian culture. Meetings include discussions about heavier topics (ex. mental health, covid-inflicted racism, normalized cultural appropriation) as well as more light-hearted activities (ex. potlucks, movie screenings, field trips) to foster learning opportunities.</p>
                  </div>
              </div>
              
              
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1CWJ-jp_qMol2H009SzD9pIqKlGv705Qt" alt="Dungeons and Dragons Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="dungeons-and-dragons-club-link" style="background-color:#fff;color:#000 !important">Dungeons and Dragons Club</button></h5>
                    <p>A club for people to play Dungeons and Dragons.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1fk0NpBGB_oc4tfxS-lZ00EUqtrt-yKF5" alt="Riot ">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="riot--link" style="background-color:#fff;color:#000 !important">Riot </button></h5>
                    <p>We are a Women of Color club/affinity space. We work to make all WOC at UHS feel comfortable in this community and to provide a space for the discussion of many, many related issues!  Although we are a closed affinity space, we frequently hold open meetings, or meetings in collaboration with other clubs like SWEAR, Men&#39;s group, Spectra, and more. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=180Oon8EWDpXqOyGpv55HtYLs1V56-RIn" alt="Understanding Whiteness">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="understanding-whiteness-link" style="background-color:#fff;color:#000 !important">Understanding Whiteness</button></h5>
                    <p>Understanding Whiteness is a discussion space for students who identify as white. The space will be used to talk about and further understand whiteness and how that plays a role in our classrooms, clubs and other UHS spaces. We will focus on whiteness at UHS, in the Bay Area and in the world at large, and how we see whiteness appear in current events. This is a white affinity because we want to create a sustained space for the white members of the UHS community to talk about race. We will be working in partnership with the adult Understanding Whiteness group for some meetings, and hopefully with other affinity spaces as well. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1vVu2mj2nsjr33PrC2naYaE6ET7NwApu9" alt="Yearbook">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="yearbook-link" style="background-color:#fff;color:#000 !important">Yearbook</button></h5>
                    <p>Yearbook is a club focused on capturing the moments shared by the UHS community. This will be an open space to all who want to participate and learn/apply aspects of graphic design and photography! Despite the fact that we may not have the chance to be together for a while, we still want to create an aspect of our school that lets all of us participate with one another. We can&#39;t wait to see what comes up!</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=143xdpESH3A_Q6ZAKBN5BWszq2H7PQ9mm" alt="Spectra">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="spectra-link" style="background-color:#fff;color:#000 !important">Spectra</button></h5>
                    <p>Spectra will serve as an affinity safe space space for LGBT+ students and faculty. In addition to providing an affinity space, we will hold open meetings and hold discussions to educate the broader UHS community about the issues our community faces.</p>
                  </div>
              </div>
              
              
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1dT7fV3YwhOCkmAwWK7cDspJG8giKp2nN" alt="Jewish Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="jewish-club-link" style="background-color:#fff;color:#000 !important">Jewish Club</button></h5>
                    <p>Jewish Club welcomes all members of the UHS community to discuss different aspects of the Jewish identity. Together, we will celebrate holidays, discuss controversies in the Jewish community and exchange stories of different Jewish experiences. In the past, some of our most successful meetings have been about Jews and sports, Israel and Palestine, and Jewish comedy. We encourage you to come to our meetings, whether you identify as Jewish, Jew-ish or neither!</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1ttXHVyJTOQ7wBtLrMUYHu1imjdGnWV3a" alt="Interfaith">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="interfaith-link" style="background-color:#fff;color:#000 !important">Interfaith</button></h5>
                    <p>Interfaith is a club for students and faculty to have open conversations about faith and spirituality. With UHS being a secular school, we recognize that it may be difficult to find safe spaces to discuss faith; therefore, we hope to provide such a space with our club. We would also like to emphasize that we are not an affinity group; anyone is welcome at our meetings, regardless of their religious affiliation or lack thereof. </p>
                  </div>
              </div>
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1LzLOB0I_eCVo1O6cBKd03arznTpnXwff" alt="Financial Aid and Socio-Economic Status  (FASES)">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="financial-aid-and-socio-economic-status--(fases)-link" style="background-color:#fff;color:#000 !important">Financial Aid and Socio-Economic Status  (FASES)</button></h5>
                    <p>FASES is a club focused on addressing and tackling issues of socio-economic status and wealth within our community and beyond. We hold both affinity meetings for students on financial aid and open meetings for all to attend.</p>
                  </div>
              </div>
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1wyrKwmQ5qOBkhg59tobzl-5pL0wYR6BM" alt="UNICEF Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="unicef-club-link" style="background-color:#fff;color:#000 !important">UNICEF Club</button></h5>
                    <p>We are focused on fundraising, advocacy/raising awareness, community building, and volunteering locally. This is a club open to everyone and we would love new faces! </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1biN1bF3j2qp61vNp1uCHLBlWNJNE2ShF" alt="Science Olympiad">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="science-olympiad-link" style="background-color:#fff;color:#000 !important">Science Olympiad</button></h5>
                    <p>A chill club to explore scientific topics not formally taught by UHS and a chance to pursue other scientific interests with your peers in a semi-competitive or fun and experimental environment. </p>
                  </div>
              </div>
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1X800rNe-dESui73xF6zMMm9WShH6Q2kx" alt="Disney Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="disney-club-link" style="background-color:#fff;color:#000 !important">Disney Club</button></h5>
                    <p>We plan on doing screenings of your favorite Disney and Pixar movies! We are always open to suggestions so if you have a childhood fav you&#39;d like us to screen, let us know. Anyone who still feels like a child at heart is encouraged to come :) </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1r4zT6QBHRw4yNHs8Q_rkRac9gAjFByUu" alt="Satonics">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="satonics-link" style="background-color:#fff;color:#000 !important">Satonics</button></h5>
                    <p>This club is UHS’s a cappella group and is open to anyone who is accepted via an informal audition. We make music entirely with our voices and sing a variety of music, from pop songs to jazz arrangements, and perform at concerts and competitions. We will be holding auditions through Zoom next Friday (29th) and Saturday (30th), with more information to sign up in an email. We especially encourage underclassmen and those with lower voices to audition! Until further notice from the high school a cappella competition we participate in (Varsity Vocals ICHSA), our group will perform for school concerts through pre-recorded songs.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1iRw4xM3-Ss7EvGAItqS2jeVYPSppBvdv" alt="Multiracial Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="multiracial-club-link" style="background-color:#fff;color:#000 !important">Multiracial Club</button></h5>
                    <p>An affinity space for students and faculty that self-identify as biracial or multiracial. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1UgyFO_nPxNFkkr_EXDUL6gY6fxzD9rwv" alt="Artivism Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="artivism-club-link" style="background-color:#fff;color:#000 !important">Artivism Club</button></h5>
                    <p>The purpose of Artivism club is to explore the intersection of art and activism, through art projects, fundraisers, and club meetings. We plan to collaborate with clubs such as BSU, Riot, and SWEAR in order to explore art as a vehicle for social justice. Previous projects include a mural for Summerbridge (featured in the hallway of Upper campus), poster-making sessions, and lunch workshops on color theory/design principles. Our meetings are open to everyone, regardless of identity or prior artistic experience! </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1ilPU8lENicf97gsFnfbO56i5T9cqV57J" alt="Girls Who Code">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="girls-who-code-link" style="background-color:#fff;color:#000 !important">Girls Who Code</button></h5>
                    <p>Girls Who Code is a national non-profit organization working to close the gender gap in technology. Our club educates, equips, and inspires girls with the computing skills they&#39;ll need to pursue 21st-century opportunities.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1Nv-_3OZIR3FI1Z4P0BGK_CRtBghmwvRt" alt="Hapa (half white half asian affinity group)">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="hapa-(half-white-half-asian-affinity-group)-link" style="background-color:#fff;color:#000 !important">Hapa (half white half asian affinity group)</button></h5>
                    <p>Hapa is a term used to describe a person who is half asian and half white. This affinity group, with closed meetings, will delve into the complexity that arises with a dual identity. </p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1M4wtD2PLLN4TN94RMQRujwIsQ9SGFh_V" alt="Avatar: The Last Airbender Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="avatar:-the-last-airbender-club-link" style="background-color:#fff;color:#000 !important">Avatar: The Last Airbender Club</button></h5>
                    <p>Our club welcomes fans of the Avatar universe, including Avatar: The Last Airbender and Legend of Korra. I think we can all agree that it is the best show ever written, so we decided to make a club to appreciate its brilliance. We will watch episodes, discuss opinions and themes, take fun &#34;which bender am I&#34; quizzes and appreciate the show and its excellence.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1ZnMS1INYZDiydg5lmq5WPDAvAQpedMIi" alt="Conservative Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="conservative-club-link" style="background-color:#fff;color:#000 !important">Conservative Club</button></h5>
                    <p>UHS Conservative Club is a club dedicated to promoting substantive discussion of political ideas. We believe that when 80% of liberal students feel confident sharing their political views, but 80% of conservative students do not, real debate can never be achieved. To join, you don&#39;t need to hold any particular viewpoints on any issue, and you don&#39;t even need to be conservative (in fact, we welcome and value differing perspectives). All you need to believe is that UHS, and the United States as a whole, will be a better place if we allow open and honest debate and exchange of ideas, and that echo chambers aren&#39;t good for anyone. Our goal is to provide a forum for conservative thought that is mainstream in the United States, but not often represented at UHS.

We will meet every few weeks to discuss current events, the political climate on campus and in the country, or host a guest speaker.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1LnaXI2SXVKV7XrUJj68h3vSKzChiIsow" alt="White Folks Committed to Anti-Racism Affinity Space">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="white-folks-committed-to-anti-racism-affinity-space-link" style="background-color:#fff;color:#000 !important">White Folks Committed to Anti-Racism Affinity Space</button></h5>
                    <p>“I can’t build externally what I haven’t built internally.”
Dr. Cornel West
 
 
This is an invitation for all folks who identify as white and are striving toward an identity of anti-racist. This is a space to gather and process the complexity of what it means to be white identifying human beings at this time with a focus on building a competent and firm foundation of anti-racism. This is a supportive and safe space. We will make mistakes. We will have all the best intentions and still have a negative impact. This is a space to learn and grow together, that our intentions may align with our actions, that we may shift to being influential as opposed to impactful. We will bring all our humanness to the table and hold space for all of it.
 </p>
                  </div>
              </div>
              
              
              
              
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1e74BJbPfHCyirNbM4MExRl3h_7QralGf" alt="Women&#39;s Health Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="women&#39;s-health-club-link" style="background-color:#fff;color:#000 !important">Women&#39;s Health Club</button></h5>
                    <p>The mission of our club is to spread awareness about how common sexual assault/rape is in our society and educate students through stories, guest speakers, social media, documentaries, and other sources. We hope to become advocates for change by working with organizations in San Francisco as well as providing a safe space for UHS students to learn and talk about these issues. This club will have a few closed meetings but will mostly be open for everyone.</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1NRLA2QMsogjPDLYodEcZylLaSaCA6CnQ" alt="The Radio Broadcast Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="the-radio-broadcast-club-link" style="background-color:#fff;color:#000 !important">The Radio Broadcast Club</button></h5>
                    <p>In this club we will listen to old radio theater broadcasts as well as rewrite them or recreate them! As a form of online drama!</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1KLk4U3iXsTpiP4IfoYO1QuLHydSTBmPi" alt="UHS Business Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="uhs-business-club-link" style="background-color:#fff;color:#000 !important">UHS Business Club</button></h5>
                    <p>Selling short; econometrics; balance sheets...what does this all mean? The UHS Business Club provides opportunities for its members to learn about the inner workings of the business world. Through activities such as case studies, ethical debates, and projects, we will introduce our club members to careers in the business sector, current events in the finance field, and experimentation with basic business transactions. With introductions to management, marketing and investing games, get ready for some fun dives into the business world. We are open to all who would like to join!</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=121_Q-W2qgbuep_Bl5Rms8v8Uh2DHuze2" alt="UHS SWENext Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="uhs-swenext-club-link" style="background-color:#fff;color:#000 !important">UHS SWENext Club</button></h5>
                    <p>From bridges to spaceships, computers to cars, engineers are the force behind many of the objects we interact with. The Society of Women Engineers (SWE) seeks to increase the representation of women in the engineering field and revamp the dynamics of the engineering workforce. Our UHS SWENext Club combines group activities, discussions about current events in engineering, and lessons about engineering to expand on SWE’s mission of empowering women engineers. Most of the activity and learning based meetings will be open to non-male identifying students, but meetings discussing current events will be open to all!</p>
                  </div>
              </div>
              
              
              
              <div class="carousel-item">
                <img class="d-block w-100" src="https://drive.google.com/uc?export=view&amp;id=1gzLIHou05Ff8ukISzaEUHX3q6aEHHPCF" alt="Investment Club">
                <div class="carousel-caption d-none d-md-block" style="background-color:#ab192d; opacity:0.75">
                    <h5><button class="btn specific-club-link" id="investment-club-link" style="background-color:#fff;color:#000 !important">Investment Club</button></h5>
                    <p>This is a club open to all students with an interest in investing and the financial world. No experience is required, we’ll learn together how to track a portfolio and research stocks. The club will have various speakers with years of experience in finance and will be an interactive space for students to learn more about investing.</p>
                  </div>
              </div>
              
              
            </div>
            <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="model-united-nations" style="background-color:#fff; padding:20px; display:none">
            <h1>Model United Nations</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1bZonWqkSHVC1gGGKLwwDkG6Y2tBxYUJE">
            <br><p>Model UN is a club dedicated to teaching students about international affairs through a UN simulation that takes place in competitive conferences. We use meetings to educate and prepare for conferences, which we attend several times throughout the year. As one of only two clubs with overnight trips, delegates have plenty of opportunities to make friends and lifelong enemies. From ordering six pints of ice cream to the hotel at 1 AM, to aggressively debating the delegation of The Seychelles, to awkwardly greeting the delegation of Italy dressed in full Roman armor, Model UN is an experience you won&#39;t forget.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emilia&amp;const_search_last_name=Fowler">Emilia Fowler</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jeanette&amp;const_search_last_name=Nguyen">Jeanette Nguyen</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Dan&amp;const_search_last_name=Huguenin">Dan Huguenin</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Rochelle&amp;const_search_last_name=Devault">Rochelle Devault</a></li>
                <br><li>Meeting Time: Wednesday Lunch</li><br>
                <li><a href="mailto:emilia.fowler_21@sfuhs.org"><i class="fa fa-envelope"></i> emilia.fowler_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="international-club" style="background-color:#fff; padding:20px; display:none">
            <h1>International Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1YQ-7OVMQZsHQK9FPbBIpSUABdVgNrkwt">
            <br><p>International club will be a space for people who have citizenship in countries outside of the U.S., are from a country outside of the U.S., or have parents from a country outside of the U.S. to talk about what its like to hold membership in two places that could possibly be thousands of miles apart. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mirabelle&amp;const_search_last_name=Brettkelly">Mirabelle Brettkelly</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Isabella&amp;const_search_last_name=Hochschild">Isabella Hochschild</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Roselyne&amp;const_search_last_name=Pilaar">Roselyne Pilaar</a></li>
                <br><li>Meeting Time: Tuesday Lunch</li><br>
                <li><a href="mailto:mirabelle.brettke_21@sfuhs.org"><i class="fa fa-envelope"></i> mirabelle.brettke_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="riot" style="background-color:#fff; padding:20px; display:none">
            <h1>Riot</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=14K3Y3heQscDppBd-oPr92d-q-N-nF-kN">
            <br><p>We are a women of color club/affinity space! We work to make sure all WOC at UHS feel comfortable in this community and provide a space for the discussion of many related issues. Although we are an affinity space, we frequently hold open meetings or meetings in collaboration with other clubs like SWEAR, Men&#39;s Group, Spectra, and more. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Maya&amp;const_search_last_name=Patel">Maya Patel</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Samantha&amp;const_search_last_name=Lee">Samantha Lee</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a></li>
                <br><li>Meeting Time: Wednesday Clubs/Affinity</li><br>
                <li><a href="mailto:maya.patel_21@sfuhs.org"><i class="fa fa-envelope"></i> maya.patel_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="latinx-united" style="background-color:#fff; padding:20px; display:none">
            <h1>LatinX United</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1w9hu5LswmVIxBiScZ01WnV6pEbXvqIt9">
            <br><p>LatinX United is an affinity club for members of the UHS community who identify as LatinX. We host weekly meetings to discuss current events, connect as a community, and act as resources for each other. We also organize and host fundraisers for causes that affect LatinX people in the Bay Area and around the world.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Evan-Carlo&amp;const_search_last_name=Fowler">Evan-Carlo Fowler</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mica&amp;const_search_last_name=Clark-Herrera">Mica Clark-Herrera</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=and&amp;const_search_last_name=Brandly">Brandly Mazariegos</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jessica&amp;const_search_last_name=Osorio">Jessica Osorio </a></li>
                <br><li>Meeting Time: Tuesday Lunch</li><br>
                <li><a href="mailto:evancarlo.fowler_21@sfuhs.org"><i class="fa fa-envelope"></i> evancarlo.fowler_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="sunrise-movement--uhs-hub" style="background-color:#fff; padding:20px; display:none">
            <h1>Sunrise Movement- UHS Hub</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1oMZqQG5Dxi1xmW7QsYrcDbhYAjL3pB_R">
            <br><p>This is a high school hub of the larger Sunrise Movement which is a non-profit working to raise awareness of and pass the Green New Deal. If enacted, the Green New Deal would force the US to become more active in fighting climate change as well as produce many sustainable jobs. 

We plan to host a space through which UHS students can take part in the political fight against climate change and take part in the Sunrise Movement. We will be discussing our thoughts on the Green New Deal, ideas we have, and current events related to the Sunrise Movement and the Green New Deal. If you are passionate about climate change and the Green New Deal as well as are interested in getting politically involved but don&#39;t necessarily know how, join use, and we can work together to hopefully one day get the Green New Deal passed. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alicia&amp;const_search_last_name=Lopez-Guerra">Alicia Lopez-Guerra</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hannah&amp;const_search_last_name=Urisman">Hannah Urisman</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Annabelle&amp;const_search_last_name=Brauer">Annabelle Brauer</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Rochelle&amp;const_search_last_name=Devault">Rochelle Devault </a></li>
                <br><li>Meeting Time: Thursday Lunch</li><br>
                <li><a href="mailto:alicia.lopezguerr_22@sfuhs.org"><i class="fa fa-envelope"></i> alicia.lopezguerr_22@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="black-student-union-(bsu)" style="background-color:#fff; padding:20px; display:none">
            <h1>Black Student Union (BSU)</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1gWtAqOvic-aiMzAP31hLzExfnENj6Yue">
            <br><p>We welcome any and all members of the UHS community who identify as being a part of the African diaspora (e.g. black, African American, black-biracial, etc.). Come out for a guaranteed good time so you&#39;re ready to hang with everyone in person when it&#39;s safe to have irl cookouts :)</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jasmine&amp;const_search_last_name=Gonzalez">Jasmine Gonzalez</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Anna&amp;const_search_last_name=Elgin">Anna Elgin</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alyanna&amp;const_search_last_name=Hughes">Alyanna Hughes</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a></li>
                <br><li>Meeting Time: Wednesday Clubs/Affinity</li><br>
                <li><a href="mailto:jasmine.gonzalez_21@sfuhs.org"><i class="fa fa-envelope"></i> jasmine.gonzalez_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="financial-aid-and-socio-economic-status-club-(fases)" style="background-color:#fff; padding:20px; display:none">
            <h1>Financial Aid and Socio-Economic Status Club (FASES)</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1u3Xm3qeYvmgPNB67hhgJA5C7BedKkHL-">
            <br><p>FASES is a space for members of the UHS community to discuss wealth, financial aid, and the local + societal implications of both. Sometimes we&#39;ll be an affinity space for students on financial aid, and sometimes our meetings will be open to all!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jasmine&amp;const_search_last_name=Gonzalez">Jasmine Gonzalez</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Frank&amp;const_search_last_name=Wercinski">Frank Wercinski</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Chloe&amp;const_search_last_name=Richmond">Chloe Richmond</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Gaby&amp;const_search_last_name=Garcia">Gaby Garcia</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Drew&amp;const_search_last_name=Phillips">Drew Phillips </a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jenny&amp;const_search_last_name=Schneider">Jenny Schneider</a></li>
                <br><li>Meeting Time: Thursday Lunch</li><br>
                <li><a href="mailto:jasmine.gonzalez_21@sfuhs.org"><i class="fa fa-envelope"></i> jasmine.gonzalez_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="baking-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Baking Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1SDHm11___kNChZi_a5a_1xSWObn5He2h">
            <br><p>With the rise of quarantine banana bread, sourdough starters, and all sorts of pandemic baking, we thought it would be the perfect time to bring back Baking Club in a virtual environment. We&#39;ll be playing music and/or screen sharing the Great British Baking Show while we bake and chat from our own kitchens and everyone is invited to join! Each meeting, we&#39;ll all bake a recipe that we voted on the previous meeting, but you can bake whatever you want as well (it&#39;s also okay just to log on to hang out and watch other people bake!) This club is open to all students and faculty, no matter your baking skill level! (p.s. our header photo is from the Club Fair last year! Fingers crossed that we&#39;ll bring treats to more in-person meetings if we get the chance to go back on campus soon)</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Isabella&amp;const_search_last_name=Hochschild">Isabella Hochschild</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mirabelle&amp;const_search_last_name=Brettkelly">Mirabelle Brettkelly</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jessica&amp;const_search_last_name=Osorio">Jessica Osorio</a></li>
                <br><li>Meeting Time: Tuesday Lunch</li><br>
                <li><a href="mailto:isabella.hochschi_21@sfuhs.org"><i class="fa fa-envelope"></i> isabella.hochschi_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="board-game-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Board Game Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1VxSCyWj6MufV1GDXmgG5wlRjv6UhNxpi">
            <br><p>A club for playing board games, especially but not limited to Secret Hitler (and now with online alternatives!)</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Pierce&amp;const_search_last_name=Hoenigman">Pierce Hoenigman</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sandeep&amp;const_search_last_name=Bhuta">Sandeep Bhuta</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="swear-(students-for-women&#39;s-equality-and-rights)" style="background-color:#fff; padding:20px; display:none">
            <h1>SWEAR (Students for Women&#39;s Equality and Rights)</h1>
            
            <br><p>SWEAR (Students for Women’s Equality and Rights) is a space on campus created to discuss all things pertaining to self-identifying women/people who identify with the female experience, including current events, mental health, sex, and other various topics. We believe intersectionality is vital to any conversation about the female experience and we strive for our meetings to be welcoming to people from all backgrounds and experiences. We believe amplifying the voices of women of color at UHS is essential to our community. We host both closed and open meetings as well as events like the Mental Health Workshop and the SWEAR Sleepover.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Evers">Elizabeth Evers</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Walcott">Sarah Walcott</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sara&amp;const_search_last_name=Tagol">Sara Tagol</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lindsay&amp;const_search_last_name=Eiseman,">Lindsay Eiseman,</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Katherine&amp;const_search_last_name=Holden">Katherine Holden</a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jessica&amp;const_search_last_name=Osorio">Jessica Osorio</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="student-council" style="background-color:#fff; padding:20px; display:none">
            <h1>Student Council</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1AP-Epdfzp_H4SZGc4BUKmF7tudGxK9ap">
            <br><p>Student council is a faculty-supported leadership group dedicated toward teaching students leadership skills while simultaneously assisting the school with a number of tasks. Elected students organize spirit events and interface with faculty regularly to advocate for their constituents.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=David&amp;const_search_last_name=Wignall">David Wignall</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a></li>
                <br><li>Meeting Time: Thursday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="mena-" style="background-color:#fff; padding:20px; display:none">
            <h1>MENA </h1>
            
            <br><p>MENA stands for Middle Eastern North African and is an affinity space for all people who identify with the term. We mainly have closed meetings available only to those who identify as MENA to discuss topics that relate to our community.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sara&amp;const_search_last_name=Tagol">Sara Tagol</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Darius&amp;const_search_last_name=Yamini">Darius Yamini </a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Dr.&amp;const_search_last_name=Ahmed">Dr. Ahmed </a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="the-devils&#39;-advocate" style="background-color:#fff; padding:20px; display:none">
            <h1>The Devils&#39; Advocate</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1gjGWsrLkSdFSrdFoye1qMQ45b2EbZ1-U">
            <br><p>The Devils&#39; Advocate is the student-run school newspaper, reporting on multiple categories, including current events, sports, arts, and more, of UHS and the world at-large. We believe that journalism has the power to make each reader’s life richer and fosters the vibrance of the UHS community. In pursuit of the truth and honoring journalistic integrity, the DA welcomes and encourages all voices to be represented in our paper. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jeanette&amp;const_search_last_name=Nguyen">Jeanette Nguyen</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Evan&amp;const_search_last_name=Carlo-Fowler">Evan Carlo-Fowler</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Zach&amp;const_search_last_name=Beischer">Zach Beischer</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ryan&amp;const_search_last_name=O&#39;Donnell">Ryan O&#39;Donnell</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="rock-history-and-appreciation-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Rock History and Appreciation Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=17xBTZFUg-Qhg8vDSlV3zR-9Dv9Xq2wjQ">
            <br><p>Not an affinity space.  It&#39;s a club for people to listen to, learn about, and enjoy rock music.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Maggie&amp;const_search_last_name=Carlson">Maggie Carlson</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sandeep&amp;const_search_last_name=Bhuta">Sandeep Bhuta</a></li>
                <br><li>Meeting Time: Wednesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="aapi" style="background-color:#fff; padding:20px; display:none">
            <h1>AAPI</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1SuaKY2cFu8qcFiYjDpjXy-rQrFUEoqOZ">
            <br><p>AAPI or Asian American/Pacific Islander is UHS&#39;s Asian affinity space. AAPI provides a safe space for AAPI students and faculty in the UHS community to  connect with one another and share their experiences. It is closed to those who identify as Asian, Asian American, and Pacific Islander, though some meetings will be open to all who have an interest in learning more about Asian culture. Meetings include discussions about heavier topics (ex. mental health, covid-inflicted racism, normalized cultural appropriation) as well as more light-hearted activities (ex. potlucks, movie screenings, field trips) to foster learning opportunities.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jeanette&amp;const_search_last_name=Nguyen">Jeanette Nguyen</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mason&amp;const_search_last_name=Villegas">Mason Villegas</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Cheung">Sarah Cheung</a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Pierre&amp;const_search_last_name=Carmona">Pierre Carmona</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Joanne&amp;const_search_last_name=Sugiyama">Joanne Sugiyama</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="red-cross-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Red Cross Club</h1>
            
            <br><p>This is a club for anyone interested in community service and public health. Due to online school, we will be meeting over zoom to discuss COVID-19, public health issues, as well as discussing drives and other activities for the future. We want to provide a space for students interested in helping their community as well as being knowledgeable about public health inequality. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sydney&amp;const_search_last_name=Srivastava">Sydney Srivastava</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jane&amp;const_search_last_name=Shvartsman">Jane Shvartsman</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a></li>
                <br><li>Meeting Time: Monday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="men-of-color-group" style="background-color:#fff; padding:20px; display:none">
            <h1>Men of Color Group</h1>
            
            <br><p>This is an affinity group for men of color to talk about issues or attitudes that have been perpetuated in our respective communities.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Kai&amp;const_search_last_name=Martell">Kai Martell</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Luqmaan&amp;const_search_last_name=Shaikh">Luqmaan Shaikh</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="dungeons-and-dragons-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Dungeons and Dragons Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1CWJ-jp_qMol2H009SzD9pIqKlGv705Qt">
            <br><p>A club for people to play Dungeons and Dragons.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ella&amp;const_search_last_name=Barrett">Ella Barrett</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Victoria&amp;const_search_last_name=Mann">Victoria Mann</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Madeline&amp;const_search_last_name=Boyle">Madeline Boyle</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Albert&amp;const_search_last_name=Boyle">Albert Boyle</a></li>
                <br><li>Meeting Time: Monday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="riot-" style="background-color:#fff; padding:20px; display:none">
            <h1>Riot </h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1fk0NpBGB_oc4tfxS-lZ00EUqtrt-yKF5">
            <br><p>We are a Women of Color club/affinity space. We work to make all WOC at UHS feel comfortable in this community and to provide a space for the discussion of many, many related issues!  Although we are a closed affinity space, we frequently hold open meetings, or meetings in collaboration with other clubs like SWEAR, Men&#39;s group, Spectra, and more. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sami&amp;const_search_last_name=Lee">Sami Lee</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Maya&amp;const_search_last_name=Patel">Maya Patel</a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alexandra&amp;const_search_last_name=Simmons">Alexandra Simmons</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Tilda&amp;const_search_last_name=Kapuya">Tilda Kapuya (uncertain)</a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="understanding-whiteness" style="background-color:#fff; padding:20px; display:none">
            <h1>Understanding Whiteness</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=180Oon8EWDpXqOyGpv55HtYLs1V56-RIn">
            <br><p>Understanding Whiteness is a discussion space for students who identify as white. The space will be used to talk about and further understand whiteness and how that plays a role in our classrooms, clubs and other UHS spaces. We will focus on whiteness at UHS, in the Bay Area and in the world at large, and how we see whiteness appear in current events. This is a white affinity because we want to create a sustained space for the white members of the UHS community to talk about race. We will be working in partnership with the adult Understanding Whiteness group for some meetings, and hopefully with other affinity spaces as well. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Chloe&amp;const_search_last_name=Richmond">Chloe Richmond (&#39;21)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emmy&amp;const_search_last_name=Etlin">Emmy Etlin (&#39;21)</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jen&amp;const_search_last_name=Kent">Jen Kent</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="yearbook" style="background-color:#fff; padding:20px; display:none">
            <h1>Yearbook</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1vVu2mj2nsjr33PrC2naYaE6ET7NwApu9">
            <br><p>Yearbook is a club focused on capturing the moments shared by the UHS community. This will be an open space to all who want to participate and learn/apply aspects of graphic design and photography! Despite the fact that we may not have the chance to be together for a while, we still want to create an aspect of our school that lets all of us participate with one another. We can&#39;t wait to see what comes up!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lauren&amp;const_search_last_name=Teotico">Lauren Teotico &#39;21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Pierce&amp;const_search_last_name=Hoenigman">Pierce Hoenigman &#39;21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Janavi&amp;const_search_last_name=Padala">Janavi Padala &#39;21</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Janine&amp;const_search_last_name=Navalta">Janine Navalta &#39;22</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Faris">Elizabeth Faris</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="spectra" style="background-color:#fff; padding:20px; display:none">
            <h1>Spectra</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=143xdpESH3A_Q6ZAKBN5BWszq2H7PQ9mm">
            <br><p>Spectra will serve as an affinity safe space space for LGBT+ students and faculty. In addition to providing an affinity space, we will hold open meetings and hold discussions to educate the broader UHS community about the issues our community faces.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nico&amp;const_search_last_name=Brubaker">Nico Brubaker</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=Vidal">Ariane Vidal</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hannah&amp;const_search_last_name=Urisman">Hannah Urisman</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Andrew&amp;const_search_last_name=Galatas">Andrew Galatas</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="family-matters-affinity-group" style="background-color:#fff; padding:20px; display:none">
            <h1>Family Matters Affinity Group</h1>
            
            <br><p>Part of the UHS mission statement: &#34;Together we work to build and sustain a community of diverse backgrounds, perspectives, and talents.&#34; We will create a safe space for people with diverse family structures (e.g. adopted, trans-racially adopted, single parent, divorced parents, blended households, etc.) to share experiences and support each other and enlarge our visibility in the UHS community. Our goal is to acknowledge our family differences and make them more visible in the community;  when we can see each other more clearly, our community becomes stronger.
</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alex&amp;const_search_last_name=Perry">Alex Perry</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lucas&amp;const_search_last_name=Perry">Lucas Perry</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Eric&amp;const_search_last_name=Johnson">Eric Johnson</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="body-positive-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Body Positive Club</h1>
            
            <br><p>This club is focused on spreading body positivity and love in the UHS community and beyond. Throughout the year we will cover topics ranging from eating disorders to social media to the culture around bodies at UHS. The meetings are always open to everyone. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Evers">Elizabeth Evers</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Robbie&amp;const_search_last_name=Grisso">Robbie Grisso</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Athena&amp;const_search_last_name=Nooney">Athena Nooney</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a></li>
                <br><li>Meeting Time: Thursday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="jewish-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Jewish Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1dT7fV3YwhOCkmAwWK7cDspJG8giKp2nN">
            <br><p>Jewish Club welcomes all members of the UHS community to discuss different aspects of the Jewish identity. Together, we will celebrate holidays, discuss controversies in the Jewish community and exchange stories of different Jewish experiences. In the past, some of our most successful meetings have been about Jews and sports, Israel and Palestine, and Jewish comedy. We encourage you to come to our meetings, whether you identify as Jewish, Jew-ish or neither!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emmy&amp;const_search_last_name=Etlin">Emmy Etlin (‘21)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Eve&amp;const_search_last_name=Andersen">Eve Andersen (‘21)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Noah&amp;const_search_last_name=Mays-Smith">Noah Mays-Smith (‘22)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jacob&amp;const_search_last_name=Neplokh">Jacob Neplokh (‘23)</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Carol&amp;const_search_last_name=Coles">Carol Coles</a></li>
                <br><li>Meeting Time: Thursday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="interfaith" style="background-color:#fff; padding:20px; display:none">
            <h1>Interfaith</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1ttXHVyJTOQ7wBtLrMUYHu1imjdGnWV3a">
            <br><p>Interfaith is a club for students and faculty to have open conversations about faith and spirituality. With UHS being a secular school, we recognize that it may be difficult to find safe spaces to discuss faith; therefore, we hope to provide such a space with our club. We would also like to emphasize that we are not an affinity group; anyone is welcome at our meetings, regardless of their religious affiliation or lack thereof. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=Vidal">Ariane Vidal</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Erica&amp;const_search_last_name=Cooper">Erica Cooper</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Clarissa&amp;const_search_last_name=Dann">Clarissa Dann</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Kate&amp;const_search_last_name=Garrett">Kate Garrett</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="book-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Book Club</h1>
            
            <br><p>For our club, we plan to read a book and discuss it and possibly discuss movies too. It will take a while to read the book or watch the movie so we won&#39;t meet consecutively.  

We invite everyone to come out. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jack&amp;const_search_last_name=Clancy">Jack Clancy</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hayley&amp;const_search_last_name=Beale">Hayley Beale </a></li>
                <br><li>Meeting Time: TBD</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="financial-aid-and-socio-economic-status--(fases)" style="background-color:#fff; padding:20px; display:none">
            <h1>Financial Aid and Socio-Economic Status  (FASES)</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1LzLOB0I_eCVo1O6cBKd03arznTpnXwff">
            <br><p>FASES is a club focused on addressing and tackling issues of socio-economic status and wealth within our community and beyond. We hold both affinity meetings for students on financial aid and open meetings for all to attend.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jasmine&amp;const_search_last_name=Gonzalez">Jasmine Gonzalez</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Frank&amp;const_search_last_name=Wercinski">Frank Wercinski</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Chloe&amp;const_search_last_name=Richmond">Chloe Richmond</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Drew&amp;const_search_last_name=Phillips">Drew Phillips</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Gaby&amp;const_search_last_name=Garcia">Gaby Garcia</a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jenny&amp;const_search_last_name=Schneider">Jenny Schneider</a></li>
                <br><li>Meeting Time: Thursday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="biomed-club" style="background-color:#fff; padding:20px; display:none">
            <h1>BioMed club</h1>
            
            <br><p>BioMed club is focusing on topics such as vaccine development, clinical trials, and health inequalities. We aim to have speakers every other month covering different topics and meetings in between speakers to debrief and learn about our next speaker. There&#39;s no need to come to every meeting; if you see a topic that interests you feel free to drop in!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lucy&amp;const_search_last_name=Falzone">Lucy Falzone</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Meryl&amp;const_search_last_name=Sampson">Meryl Sampson</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Emma&amp;const_search_last_name=Hartmann">Emma Hartmann</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="unicef-club" style="background-color:#fff; padding:20px; display:none">
            <h1>UNICEF Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1wyrKwmQ5qOBkhg59tobzl-5pL0wYR6BM">
            <br><p>We are focused on fundraising, advocacy/raising awareness, community building, and volunteering locally. This is a club open to everyone and we would love new faces! </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mirabel&amp;const_search_last_name=Haskin">Mirabel Haskin Fernald</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Katie&amp;const_search_last_name=Crawford">Katie Crawford</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=undecided-&amp;const_search_last_name=we">undecided- we will email Alexandra when we know. </a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="science-olympiad" style="background-color:#fff; padding:20px; display:none">
            <h1>Science Olympiad</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1biN1bF3j2qp61vNp1uCHLBlWNJNE2ShF">
            <br><p>A chill club to explore scientific topics not formally taught by UHS and a chance to pursue other scientific interests with your peers in a semi-competitive or fun and experimental environment. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Christian&amp;const_search_last_name=Canete">Christian Canete</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Cheung">Sarah Cheung</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ella&amp;const_search_last_name=Barrett">Ella Barrett</a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Luke&amp;const_search_last_name=Probst">Luke Probst</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ozzie&amp;const_search_last_name=Nevarez">Ozzie Nevarez</a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="men&#39;s-group" style="background-color:#fff; padding:20px; display:none">
            <h1>Men&#39;s Group</h1>
            
            <br><p>Men&#39;s Group strives to be a space for men to examine, critique, and reflect on issues of masculinity, as well as a safe space for men to be open and vulnerable. We will have some meetings, closed to self-indentified males. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Owen&amp;const_search_last_name=Myers">Owen Myers (2021)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Drew&amp;const_search_last_name=Phillips">Drew Phillips (2021)</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Frank&amp;const_search_last_name=Wercinski">Frank Wercinski (2021)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Luqmaan&amp;const_search_last_name=Shaikh">Luqmaan Shaikh (2021)</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Marcus&amp;const_search_last_name=Caimi">Marcus Caimi</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="disney-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Disney Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1X800rNe-dESui73xF6zMMm9WShH6Q2kx">
            <br><p>We plan on doing screenings of your favorite Disney and Pixar movies! We are always open to suggestions so if you have a childhood fav you&#39;d like us to screen, let us know. Anyone who still feels like a child at heart is encouraged to come :) </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Katie&amp;const_search_last_name=Hartel">Katie Hartel</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sara&amp;const_search_last_name=Tagol">Sara Tagol</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Elizabeth&amp;const_search_last_name=Schaffernoth">Elizabeth Schaffernoth</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="satonics" style="background-color:#fff; padding:20px; display:none">
            <h1>Satonics</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1r4zT6QBHRw4yNHs8Q_rkRac9gAjFByUu">
            <br><p>This club is UHS’s a cappella group and is open to anyone who is accepted via an informal audition. We make music entirely with our voices and sing a variety of music, from pop songs to jazz arrangements, and perform at concerts and competitions. We will be holding auditions through Zoom next Friday (29th) and Saturday (30th), with more information to sign up in an email. We especially encourage underclassmen and those with lower voices to audition! Until further notice from the high school a cappella competition we participate in (Varsity Vocals ICHSA), our group will perform for school concerts through pre-recorded songs.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Sarah&amp;const_search_last_name=Cheung">Sarah Cheung</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Matthew&amp;const_search_last_name=Gin,">Matthew Gin,</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Madelyn&amp;const_search_last_name=Ocker">Madelyn Ocker</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Joel&amp;const_search_last_name=Chapman">Joel Chapman</a></li>
                <br><li>Meeting Time: Monday lunch</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="multiracial-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Multiracial Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1iRw4xM3-Ss7EvGAItqS2jeVYPSppBvdv">
            <br><p>An affinity space for students and faculty that self-identify as biracial or multiracial. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Arianna&amp;const_search_last_name=Schwartz">Arianna Schwartz ’22</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Phia&amp;const_search_last_name=Black">Phia Black ’23</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Owen&amp;const_search_last_name=Myers">Owen Myers ’21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Amelie&amp;const_search_last_name=Scheil">Amelie Scheil &#39;21</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lauren&amp;const_search_last_name=Schneider">Lauren Schneider &#39;21</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Nate&amp;const_search_last_name=Lundy">Nate Lundy</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="artivism-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Artivism Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1UgyFO_nPxNFkkr_EXDUL6gY6fxzD9rwv">
            <br><p>The purpose of Artivism club is to explore the intersection of art and activism, through art projects, fundraisers, and club meetings. We plan to collaborate with clubs such as BSU, Riot, and SWEAR in order to explore art as a vehicle for social justice. Previous projects include a mural for Summerbridge (featured in the hallway of Upper campus), poster-making sessions, and lunch workshops on color theory/design principles. Our meetings are open to everyone, regardless of identity or prior artistic experience! </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Amelie&amp;const_search_last_name=Scheil">Amelie Scheil</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jiho&amp;const_search_last_name=Lee">Jiho Lee</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Jenifer&amp;const_search_last_name=Kent">Jenifer Kent</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                </li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="girls-who-code" style="background-color:#fff; padding:20px; display:none">
            <h1>Girls Who Code</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1ilPU8lENicf97gsFnfbO56i5T9cqV57J">
            <br><p>Girls Who Code is a national non-profit organization working to close the gender gap in technology. Our club educates, equips, and inspires girls with the computing skills they&#39;ll need to pursue 21st-century opportunities.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Amelie&amp;const_search_last_name=Scheil">Amelie Scheil &#39;21</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Isabella&amp;const_search_last_name=Hochschild">Isabella Hochschild &#39;21</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Alicia&amp;const_search_last_name=Lopez-Guerra">Alicia Lopez-Guerra &#39;22</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Leah&amp;const_search_last_name=Dorazio">Leah Dorazio</a></li>
                <br><li>Meeting Time: Monday lunch</li><br>
                <li><a href="mailto:amelie.scheil_21@sfuhs.org"><i class="fa fa-envelope"></i> amelie.scheil_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="hapa-(half-white-half-asian-affinity-group)" style="background-color:#fff; padding:20px; display:none">
            <h1>Hapa (half white half asian affinity group)</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1Nv-_3OZIR3FI1Z4P0BGK_CRtBghmwvRt">
            <br><p>Hapa is a term used to describe a person who is half asian and half white. This affinity group, with closed meetings, will delve into the complexity that arises with a dual identity. </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Anna&amp;const_search_last_name=Neumann-Loreck">Anna Neumann-Loreck</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lauren&amp;const_search_last_name=Schneider">Lauren Schneider</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Andrew&amp;const_search_last_name=Galatas">Andrew Galatas </a></li>
                <br><li>Meeting Time: Thursday lunch</li><br>
                <li><a href="mailto:lauren.schneider_21@sfuhs.org"><i class="fa fa-envelope"></i> lauren.schneider_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="avatar:-the-last-airbender-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Avatar: The Last Airbender Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1M4wtD2PLLN4TN94RMQRujwIsQ9SGFh_V">
            <br><p>Our club welcomes fans of the Avatar universe, including Avatar: The Last Airbender and Legend of Korra. I think we can all agree that it is the best show ever written, so we decided to make a club to appreciate its brilliance. We will watch episodes, discuss opinions and themes, take fun &#34;which bender am I&#34; quizzes and appreciate the show and its excellence.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=Vidal">Ariane Vidal</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Hannah&amp;const_search_last_name=Urisman">Hannah Urisman</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Adrian&amp;const_search_last_name=Acu">Adrian Acu</a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                <li><a href="mailto:hannah.urisman_22@sfuhs.org"><i class="fa fa-envelope"></i> hannah.urisman_22@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="conservative-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Conservative Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1ZnMS1INYZDiydg5lmq5WPDAvAQpedMIi">
            <br><p>UHS Conservative Club is a club dedicated to promoting substantive discussion of political ideas. We believe that when 80% of liberal students feel confident sharing their political views, but 80% of conservative students do not, real debate can never be achieved. To join, you don&#39;t need to hold any particular viewpoints on any issue, and you don&#39;t even need to be conservative (in fact, we welcome and value differing perspectives). All you need to believe is that UHS, and the United States as a whole, will be a better place if we allow open and honest debate and exchange of ideas, and that echo chambers aren&#39;t good for anyone. Our goal is to provide a forum for conservative thought that is mainstream in the United States, but not often represented at UHS.

We will meet every few weeks to discuss current events, the political climate on campus and in the country, or host a guest speaker.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Dan&amp;const_search_last_name=Huguenin">Dan Huguenin</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Tyler&amp;const_search_last_name=Sisitsky">Tyler Sisitsky</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Kate&amp;const_search_last_name=Garrett">Kate Garrett</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                <li><a href="mailto:dan.huguenin_21@sfuhs.org"><i class="fa fa-envelope"></i> dan.huguenin_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="white-folks-committed-to-anti-racism-affinity-space" style="background-color:#fff; padding:20px; display:none">
            <h1>White Folks Committed to Anti-Racism Affinity Space</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1LnaXI2SXVKV7XrUJj68h3vSKzChiIsow">
            <br><p>“I can’t build externally what I haven’t built internally.”
Dr. Cornel West
 
 
This is an invitation for all folks who identify as white and are striving toward an identity of anti-racist. This is a space to gather and process the complexity of what it means to be white identifying human beings at this time with a focus on building a competent and firm foundation of anti-racism. This is a supportive and safe space. We will make mistakes. We will have all the best intentions and still have a negative impact. This is a space to learn and grow together, that our intentions may align with our actions, that we may shift to being influential as opposed to impactful. We will bring all our humanness to the table and hold space for all of it.
 </p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=(we&amp;const_search_last_name=want">(we want but don&#39;t have yet!)</a></li>
                <br><li>Sponsors: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Corinne&amp;const_search_last_name=Limbach">Corinne Limbach</a>, <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lindsay&amp;const_search_last_name=Repko">Lindsay Repko</a><a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lisa&amp;const_search_last_name=Carroll">Lisa Carroll</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                <li><a href="mailto:lisa.carroll@sfuhs.org"><i class="fa fa-envelope"></i> lisa.carroll@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="mental-health-coalition" style="background-color:#fff; padding:20px; display:none">
            <h1>Mental Health Coalition</h1>
            
            <br><p>Mental Health Advocacy</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=TBD:&amp;const_search_last_name=currently">TBD: currently in process</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Lindsay&amp;const_search_last_name=Repko">Lindsay Repko (may add others)</a></li>
                <br><li>Meeting Time: Tuesday lunch</li><br>
                <li><a href="mailto:lindsay.repko@sfuhs.org"><i class="fa fa-envelope"></i> lindsay.repko@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="history-of-history-of-history-of-history-of-surf-club-club-club-club-club" style="background-color:#fff; padding:20px; display:none">
            <h1>HIstory of History of History of History of Surf Club Club Club Club Club</h1>
            
            <br><p>This club will tell the historic odyssey of surf club at UHS. It will then delve deeper into topics of surf history and culture. From there, we will approach a variety of modern issues such as global warming, environmental preservation and sustainability, and more.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ren&amp;const_search_last_name=Zanze">Ren Zanze (President)</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mica&amp;const_search_last_name=(President)">Mica (President)  </a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Scott&amp;const_search_last_name=Laughlin">Scott Laughlin</a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                <li><a href="mailto:ren.zanze_21@sfuhs.org"><i class="fa fa-envelope"></i> ren.zanze_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="women&#39;s-health-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Women&#39;s Health Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1e74BJbPfHCyirNbM4MExRl3h_7QralGf">
            <br><p>The mission of our club is to spread awareness about how common sexual assault/rape is in our society and educate students through stories, guest speakers, social media, documentaries, and other sources. We hope to become advocates for change by working with organizations in San Francisco as well as providing a safe space for UHS students to learn and talk about these issues. This club will have a few closed meetings but will mostly be open for everyone.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ria&amp;const_search_last_name=Dhillon">Ria Dhillon</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Malia&amp;const_search_last_name=House">Malia House</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Barbara&amp;const_search_last_name=Holler">Barbara Holler </a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                <li><a href="mailto:malia.house_22@sfuhs.org"><i class="fa fa-envelope"></i> malia.house_22@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="the-radio-broadcast-club" style="background-color:#fff; padding:20px; display:none">
            <h1>The Radio Broadcast Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1NRLA2QMsogjPDLYodEcZylLaSaCA6CnQ">
            <br><p>In this club we will listen to old radio theater broadcasts as well as rewrite them or recreate them! As a form of online drama!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Harper&amp;const_search_last_name=Clementz">Harper Clementz (10th) </a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ariane&amp;const_search_last_name=(11th)">Ariane (11th)</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Ryan&amp;const_search_last_name=O’Donnell">Ryan O’Donnell </a></li>
                <br><li>Meeting Time: Friday lunch</li><br>
                <li><a href="mailto:harper.clementz_23@sfuhs.org"><i class="fa fa-envelope"></i> harper.clementz_23@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="uhs-business-club" style="background-color:#fff; padding:20px; display:none">
            <h1>UHS Business Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1KLk4U3iXsTpiP4IfoYO1QuLHydSTBmPi">
            <br><p>Selling short; econometrics; balance sheets...what does this all mean? The UHS Business Club provides opportunities for its members to learn about the inner workings of the business world. Through activities such as case studies, ethical debates, and projects, we will introduce our club members to careers in the business sector, current events in the finance field, and experimentation with basic business transactions. With introductions to management, marketing and investing games, get ready for some fun dives into the business world. We are open to all who would like to join!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mericel&amp;const_search_last_name=Tao">Mericel Tao</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Caroline&amp;const_search_last_name=Hall-Sherr">Caroline Hall-Sherr</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=David&amp;const_search_last_name=Roth">David Roth</a></li>
                <br><li>Meeting Time: Monday lunch</li><br>
                <li><a href="mailto:mericel.tao_22@sfuhs.org"><i class="fa fa-envelope"></i> mericel.tao_22@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="uhs-swenext-club" style="background-color:#fff; padding:20px; display:none">
            <h1>UHS SWENext Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=121_Q-W2qgbuep_Bl5Rms8v8Uh2DHuze2">
            <br><p>From bridges to spaceships, computers to cars, engineers are the force behind many of the objects we interact with. The Society of Women Engineers (SWE) seeks to increase the representation of women in the engineering field and revamp the dynamics of the engineering workforce. Our UHS SWENext Club combines group activities, discussions about current events in engineering, and lessons about engineering to expand on SWE’s mission of empowering women engineers. Most of the activity and learning based meetings will be open to non-male identifying students, but meetings discussing current events will be open to all!</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Danielle&amp;const_search_last_name=Cuthbert">Danielle Cuthbert</a> and <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Mericel&amp;const_search_last_name=Tao">Mericel Tao</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Megan&amp;const_search_last_name=Storti">Megan Storti</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                <li><a href="mailto:danielle.cuthbert_22@sfuhs.org"><i class="fa fa-envelope"></i> danielle.cuthbert_22@sfuhs.org</a></li>
            </ul>
          </div>
          
          <div class="row text-center align-items-center justify-content-center specific-club" id="investment-club" style="background-color:#fff; padding:20px; display:none">
            <h1>Investment Club</h1>
            <img class="card-img-top" style="padding:25px" src="https://drive.google.com/uc?export=view&amp;id=1gzLIHou05Ff8ukISzaEUHX3q6aEHHPCF">
            <br><p>This is a club open to all students with an interest in investing and the financial world. No experience is required, we’ll learn together how to track a portfolio and research stocks. The club will have various speakers with years of experience in finance and will be an interactive space for students to learn more about investing.</p><br>
            <ul style="list-style:none">
                <li>Leaders: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Owen&amp;const_search_last_name=Flanagan">Owen Flanagan</a></li>
                <br><li>Sponsor: <a href="https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&amp;const_search_role_ids=6%2C2%2C1&amp;const_search_first_name=Michael&amp;const_search_last_name=Novak">Michael Novak (UHS Chief Financial Operations Officer)</a></li>
                <br><li>Meeting Time: Wednesday clubs/affinity</li><br>
                <li><a href="mailto:owen.flanagan_21@sfuhs.org"><i class="fa fa-envelope"></i> owen.flanagan_21@sfuhs.org</a></li>
            </ul>
          </div>
          
          <!-- Footer -->
<footer class="page-footer font-small">

    <!-- Copyright -->
    <div class="footer-copyright text-center py-3" style="color:#fff !important">© 2020: 
      <a href="https://www.instagram.com/uhs.stuco/" style="color:#fff !important; text-decoration:underline">UHS Student Council</a>
    </div>
    <!-- Copyright -->
  
  </footer>
  <!-- Footer -->
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <script>
        // ('#search').change( function () {
        // $('.card').show();
        // var filter = $(this).val(); // get the value of the input, which we filter on
        // Console.log($(this).val());
        // $('.container').find(".card-title:not(:contains(" + filter + "))").parent().parent().css('display','none');
        $(document).ready(function() {
            $(".carousel-item").first().addClass("active");
            $('.carousel').carousel()
            var True = true
            var False = false
            var club_data = shuffleArray([{'timestamp': '8/28/2020 10:37:32', 'email': 'emilia.fowler_21@sfuhs.org', 'name': 'Model United Nations', 'description': "Model UN is a club dedicated to teaching students about international affairs through a UN simulation that takes place in competitive conferences. We use meetings to educate and prepare for conferences, which we attend several times throughout the year. As one of only two clubs with overnight trips, delegates have plenty of opportunities to make friends and lifelong enemies. From ordering six pints of ice cream to the hotel at 1 AM, to aggressively debating the delegation of The Seychelles, to awkwardly greeting the delegation of Italy dressed in full Roman armor, Model UN is an experience you won't forget.", 'leaders': 'Emilia Fowler, Jeanette Nguyen, Dan Huguenin', 'sponsor': 'Rochelle Devault', 'meeting_time': 'Wednesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1bZonWqkSHVC1gGGKLwwDkG6Y2tBxYUJE', 'index': 0, 'id': 'model-united-nations', 'leader_array': ['Emilia Fowler', 'Jeanette Nguyen', 'Dan Huguenin'], 'leader_info': [{'name': 'Emilia Fowler', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emilia&const_search_last_name=Fowler', 'is_not_last': True}, {'name': 'Jeanette Nguyen', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jeanette&const_search_last_name=Nguyen', 'is_not_last': True, 'is_not_first': True}, {'name': 'Dan Huguenin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Dan&const_search_last_name=Huguenin', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Rochelle Devault'], 'sponsor_info': [{'name': 'Rochelle Devault', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Rochelle&const_search_last_name=Devault', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/28/2020 10:45:05', 'email': 'mirabelle.brettke_21@sfuhs.org', 'name': 'International Club', 'description': 'International club will be a space for people who have citizenship in countries outside of the U.S., are from a country outside of the U.S., or have parents from a country outside of the U.S. to talk about what its like to hold membership in two places that could possibly be thousands of miles apart. ', 'leaders': 'Mirabelle Brettkelly, Isabella Hochschild', 'sponsor': 'Roselyne Pilaar', 'meeting_time': 'Tuesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1YQ-7OVMQZsHQK9FPbBIpSUABdVgNrkwt', 'index': 1, 'id': 'international-club', 'leader_array': ['Mirabelle Brettkelly', 'Isabella Hochschild'], 'leader_info': [{'name': 'Mirabelle Brettkelly', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mirabelle&const_search_last_name=Brettkelly', 'is_not_last': True}, {'name': 'Isabella Hochschild', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Isabella&const_search_last_name=Hochschild', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Roselyne Pilaar'], 'sponsor_info': [{'name': 'Roselyne Pilaar', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Roselyne&const_search_last_name=Pilaar', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, {'timestamp': '8/28/2020 10:48:31', 'email': 'maya.patel_21@sfuhs.org', 'name': 'Riot', 'description': "We are a women of color club/affinity space! We work to make sure all WOC at UHS feel comfortable in this community and provide a space for the discussion of many related issues. Although we are an affinity space, we frequently hold open meetings or meetings in collaboration with other clubs like SWEAR, Men's Group, Spectra, and more. ", 'leaders': 'Maya Patel, Samantha Lee', 'sponsor': 'Alexandra Simmons', 'meeting_time': 'Wednesday Clubs/Affinity', 'image': 'https://drive.google.com/uc?export=view&id=14K3Y3heQscDppBd-oPr92d-q-N-nF-kN', 'index': 2, 'id': 'riot', 'leader_array': ['Maya Patel', 'Samantha Lee'], 'leader_info': [{'name': 'Maya Patel', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Maya&const_search_last_name=Patel', 'is_not_last': True}, {'name': 'Samantha Lee', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Samantha&const_search_last_name=Lee', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Alexandra Simmons'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, {'timestamp': '8/28/2020 11:38:43', 'email': 'evancarlo.fowler_21@sfuhs.org', 'name': 'LatinX United', 'description': 'LatinX United is an affinity club for members of the UHS community who identify as LatinX. We host weekly meetings to discuss current events, connect as a community, and act as resources for each other. We also organize and host fundraisers for causes that affect LatinX people in the Bay Area and around the world.', 'leaders': 'Evan-Carlo Fowler, Mica Clark-Herrera, and Brandly Mazariegos', 'sponsor': 'Jessica Osorio ', 'meeting_time': 'Tuesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1w9hu5LswmVIxBiScZ01WnV6pEbXvqIt9', 'index': 3, 'id': 'latinx-united', 'leader_array': ['Evan-Carlo Fowler', 'Mica Clark-Herrera', 'and Brandly Mazariegos'], 'leader_info': [{'name': 'Evan-Carlo Fowler', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Evan-Carlo&const_search_last_name=Fowler', 'is_not_last': True}, {'name': 'Mica Clark-Herrera', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mica&const_search_last_name=Clark-Herrera', 'is_not_last': True, 'is_not_first': True}, {'name': 'Brandly Mazariegos', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=and&const_search_last_name=Brandly', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jessica Osorio '], 'sponsor_info': [{'name': 'Jessica Osorio ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jessica&const_search_last_name=Osorio', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, {'timestamp': '8/28/2020 19:08:29', 'email': 'alicia.lopezguerr_22@sfuhs.org', 'name': 'Sunrise Movement- UHS Hub', 'description': "This is a high school hub of the larger Sunrise Movement which is a non-profit working to raise awareness of and pass the Green New Deal. If enacted, the Green New Deal would force the US to become more active in fighting climate change as well as produce many sustainable jobs. \n\nWe plan to host a space through which UHS students can take part in the political fight against climate change and take part in the Sunrise Movement. We will be discussing our thoughts on the Green New Deal, ideas we have, and current events related to the Sunrise Movement and the Green New Deal. If you are passionate about climate change and the Green New Deal as well as are interested in getting politically involved but don't necessarily know how, join use, and we can work together to hopefully one day get the Green New Deal passed. ", 'leaders': 'Alicia Lopez-Guerra, Hannah Urisman, Annabelle Brauer', 'sponsor': 'Rochelle Devault ', 'meeting_time': 'Thursday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1oMZqQG5Dxi1xmW7QsYrcDbhYAjL3pB_R', 'index': 4, 'id': 'sunrise-movement--uhs-hub', 'leader_array': ['Alicia Lopez-Guerra', 'Hannah Urisman', 'Annabelle Brauer'], 'leader_info': [{'name': 'Alicia Lopez-Guerra', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alicia&const_search_last_name=Lopez-Guerra', 'is_not_last': True}, {'name': 'Hannah Urisman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hannah&const_search_last_name=Urisman', 'is_not_last': True, 'is_not_first': True}, {'name': 'Annabelle Brauer', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Annabelle&const_search_last_name=Brauer', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Rochelle Devault '], 'sponsor_info': [{'name': 'Rochelle Devault ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Rochelle&const_search_last_name=Devault', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/30/2020 22:06:04', 'email': 'jasmine.gonzalez_21@sfuhs.org', 'name': 'Black Student Union (BSU)', 'description': "We welcome any and all members of the UHS community who identify as being a part of the African diaspora (e.g. black, African American, black-biracial, etc.). Come out for a guaranteed good time so you're ready to hang with everyone in person when it's safe to have irl cookouts :)", 'leaders': 'Jasmine Gonzalez, Anna Elgin, Alyanna Hughes', 'sponsor': 'Alexandra Simmons', 'meeting_time': 'Wednesday Clubs/Affinity', 'image': 'https://drive.google.com/uc?export=view&id=1gWtAqOvic-aiMzAP31hLzExfnENj6Yue', 'index': 5, 'id': 'black-student-union-(bsu)', 'leader_array': ['Jasmine Gonzalez', 'Anna Elgin', 'Alyanna Hughes'], 'leader_info': [{'name': 'Jasmine Gonzalez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jasmine&const_search_last_name=Gonzalez', 'is_not_last': True}, {'name': 'Anna Elgin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Anna&const_search_last_name=Elgin', 'is_not_last': True, 'is_not_first': True}, {'name': 'Alyanna Hughes', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alyanna&const_search_last_name=Hughes', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Alexandra Simmons'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, {'timestamp': '8/30/2020 22:43:36', 'email': 'jasmine.gonzalez_21@sfuhs.org', 'name': 'Financial Aid and Socio-Economic Status Club (FASES)', 'description': "FASES is a space for members of the UHS community to discuss wealth, financial aid, and the local + societal implications of both. Sometimes we'll be an affinity space for students on financial aid, and sometimes our meetings will be open to all!", 'leaders': 'Jasmine Gonzalez, Frank Wercinski, Chloe Richmond, Gaby Garcia, Drew Phillips ', 'sponsor': 'Nate Lundy, Jenny Schneider', 'meeting_time': 'Thursday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1u3Xm3qeYvmgPNB67hhgJA5C7BedKkHL-', 'index': 6, 'id': 'financial-aid-and-socio-economic-status-club-(fases)', 'leader_array': ['Jasmine Gonzalez', 'Frank Wercinski', 'Chloe Richmond', 'Gaby Garcia', 'Drew Phillips '], 'leader_info': [{'name': 'Jasmine Gonzalez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jasmine&const_search_last_name=Gonzalez', 'is_not_last': True}, {'name': 'Frank Wercinski', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Frank&const_search_last_name=Wercinski', 'is_not_last': True, 'is_not_first': True}, {'name': 'Chloe Richmond', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Chloe&const_search_last_name=Richmond', 'is_not_last': True, 'is_not_first': True}, {'name': 'Gaby Garcia', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Gaby&const_search_last_name=Garcia', 'is_not_last': True, 'is_not_first': True}, {'name': 'Drew Phillips ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Drew&const_search_last_name=Phillips', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy', 'Jenny Schneider'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': True}, {'name': 'Jenny Schneider', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jenny&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}], 'is_affinity_group': True}, {'timestamp': '8/19/2020 9:28:49', 'email': 'isabella.hochschi_21@sfuhs.org', 'name': 'Baking Club', 'description': "With the rise of quarantine banana bread, sourdough starters, and all sorts of pandemic baking, we thought it would be the perfect time to bring back Baking Club in a virtual environment. We'll be playing music and/or screen sharing the Great British Baking Show while we bake and chat from our own kitchens and everyone is invited to join! Each meeting, we'll all bake a recipe that we voted on the previous meeting, but you can bake whatever you want as well (it's also okay just to log on to hang out and watch other people bake!) This club is open to all students and faculty, no matter your baking skill level! (p.s. our header photo is from the Club Fair last year! Fingers crossed that we'll bring treats to more in-person meetings if we get the chance to go back on campus soon)", 'leaders': 'Isabella Hochschild, Mirabelle Brettkelly', 'sponsor': 'Jessica Osorio', 'meeting_time': 'Tuesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1SDHm11___kNChZi_a5a_1xSWObn5He2h', 'index': 7, 'id': 'baking-club', 'leader_array': ['Isabella Hochschild', 'Mirabelle Brettkelly'], 'leader_info': [{'name': 'Isabella Hochschild', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Isabella&const_search_last_name=Hochschild', 'is_not_last': True}, {'name': 'Mirabelle Brettkelly', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mirabelle&const_search_last_name=Brettkelly', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jessica Osorio'], 'sponsor_info': [{'name': 'Jessica Osorio', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jessica&const_search_last_name=Osorio', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/12/2020 10:02:44', 'name': 'Board Game Club', 'description': 'A club for playing board games, especially but not limited to Secret Hitler (and now with online alternatives!)', 'leaders': 'Pierce Hoenigman', 'sponsor': 'Sandeep Bhuta', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1VxSCyWj6MufV1GDXmgG5wlRjv6UhNxpi', 'email': '', 'index': 0, 'id': 'board-game-club', 'leader_array': ['Pierce Hoenigman'], 'leader_info': [{'name': 'Pierce Hoenigman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Pierce&const_search_last_name=Hoenigman', 'is_not_last': True}], 'sponsor_array': ['Sandeep Bhuta'], 'sponsor_info': [{'name': 'Sandeep Bhuta', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sandeep&const_search_last_name=Bhuta', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/12/2020 10:38:12', 'name': "SWEAR (Students for Women's Equality and Rights)", 'description': 'SWEAR (Students for Women’s Equality and Rights) is a space on campus created to discuss all things pertaining to self-identifying women/people who identify with the female experience, including current events, mental health, sex, and other various topics. We believe intersectionality is vital to any conversation about the female experience and we strive for our meetings to be welcoming to people from all backgrounds and experiences. We believe amplifying the voices of women of color at UHS is essential to our community. We host both closed and open meetings as well as events like the Mental Health Workshop and the SWEAR Sleepover.', 'leaders': 'Elizabeth Evers, Sarah Walcott, Sara Tagol, Lindsay Eiseman,, Katherine Holden', 'sponsor': 'Jessica Osorio, Corinne Limbach', 'meeting_time': 'Friday lunch', 'image': '', 'email': '', 'index': 1, 'id': "swear-(students-for-women's-equality-and-rights)", 'leader_array': ['Elizabeth Evers', 'Sarah Walcott', 'Sara Tagol', 'Lindsay Eiseman,', 'Katherine Holden'], 'leader_info': [{'name': 'Elizabeth Evers', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Evers', 'is_not_last': True}, {'name': 'Sarah Walcott', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Walcott', 'is_not_last': True, 'is_not_first': True}, {'name': 'Sara Tagol', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sara&const_search_last_name=Tagol', 'is_not_last': True, 'is_not_first': True}, {'name': 'Lindsay Eiseman,', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lindsay&const_search_last_name=Eiseman,', 'is_not_last': True, 'is_not_first': True}, {'name': 'Katherine Holden', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Katherine&const_search_last_name=Holden', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jessica Osorio', 'Corinne Limbach'], 'sponsor_info': [{'name': 'Jessica Osorio', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jessica&const_search_last_name=Osorio', 'is_not_last': True}, {'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': False, 'is_not_first': True}]}, {'timestamp': '8/12/2020 12:02:26', 'name': 'Student Council', 'description': 'Student council is a faculty-supported leadership group dedicated toward teaching students leadership skills while simultaneously assisting the school with a number of tasks. Elected students organize spirit events and interface with faculty regularly to advocate for their constituents.', 'leaders': 'David Wignall', 'sponsor': 'Alexandra Simmons', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1AP-Epdfzp_H4SZGc4BUKmF7tudGxK9ap', 'email': '', 'index': 3, 'id': 'student-council', 'leader_array': ['David Wignall'], 'leader_info': [{'name': 'David Wignall', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=David&const_search_last_name=Wignall', 'is_not_last': True}], 'sponsor_array': ['Alexandra Simmons'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/12/2020 12:23:34', 'name': 'MENA ', 'description': 'MENA stands for Middle Eastern North African and is an affinity space for all people who identify with the term. We mainly have closed meetings available only to those who identify as MENA to discuss topics that relate to our community.', 'leaders': 'Sara Tagol, Darius Yamini ', 'sponsor': 'Dr. Ahmed ', 'meeting_time': 'Wednesday clubs/affinity', 'image': '', 'email': '', 'index': 4, 'id': 'mena-', 'leader_array': ['Sara Tagol', 'Darius Yamini '], 'leader_info': [{'name': 'Sara Tagol', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sara&const_search_last_name=Tagol', 'is_not_last': True}, {'name': 'Darius Yamini ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Darius&const_search_last_name=Yamini', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Dr. Ahmed '], 'sponsor_info': [{'name': 'Dr. Ahmed ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Dr.&const_search_last_name=Ahmed', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/12/2020 13:28:14', 'name': "The Devils' Advocate", 'description': "The Devils' Advocate is the student-run school newspaper, reporting on multiple categories, including current events, sports, arts, and more, of UHS and the world at-large. We believe that journalism has the power to make each reader’s life richer and fosters the vibrance of the UHS community. In pursuit of the truth and honoring journalistic integrity, the DA welcomes and encourages all voices to be represented in our paper. ", 'leaders': 'Jeanette Nguyen, Evan Carlo-Fowler, Zach Beischer', 'sponsor': "Ryan O'Donnell", 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1gjGWsrLkSdFSrdFoye1qMQ45b2EbZ1-U', 'email': '', 'index': 6, 'id': "the-devils'-advocate", 'leader_array': ['Jeanette Nguyen', 'Evan Carlo-Fowler', 'Zach Beischer'], 'leader_info': [{'name': 'Jeanette Nguyen', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jeanette&const_search_last_name=Nguyen', 'is_not_last': True}, {'name': 'Evan Carlo-Fowler', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Evan&const_search_last_name=Carlo-Fowler', 'is_not_last': True, 'is_not_first': True}, {'name': 'Zach Beischer', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Zach&const_search_last_name=Beischer', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ["Ryan O'Donnell"], 'sponsor_info': [{'name': "Ryan O'Donnell", 'link': "https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ryan&const_search_last_name=O'Donnell", 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/12/2020 15:58:18', 'name': 'Rock History and Appreciation Club', 'description': "Not an affinity space.  It's a club for people to listen to, learn about, and enjoy rock music.", 'leaders': 'Maggie Carlson', 'sponsor': 'Sandeep Bhuta', 'meeting_time': 'Wednesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=17xBTZFUg-Qhg8vDSlV3zR-9Dv9Xq2wjQ', 'email': '', 'index': 7, 'id': 'rock-history-and-appreciation-club', 'leader_array': ['Maggie Carlson'], 'leader_info': [{'name': 'Maggie Carlson', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Maggie&const_search_last_name=Carlson', 'is_not_last': True}], 'sponsor_array': ['Sandeep Bhuta'], 'sponsor_info': [{'name': 'Sandeep Bhuta', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sandeep&const_search_last_name=Bhuta', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/12/2020 17:12:43', 'name': 'AAPI', 'description': "AAPI or Asian American/Pacific Islander is UHS's Asian affinity space. AAPI provides a safe space for AAPI students and faculty in the UHS community to  connect with one another and share their experiences. It is closed to those who identify as Asian, Asian American, and Pacific Islander, though some meetings will be open to all who have an interest in learning more about Asian culture. Meetings include discussions about heavier topics (ex. mental health, covid-inflicted racism, normalized cultural appropriation) as well as more light-hearted activities (ex. potlucks, movie screenings, field trips) to foster learning opportunities.", 'leaders': 'Jeanette Nguyen, Mason Villegas, Sarah Cheung', 'sponsor': 'Pierre Carmona, Joanne Sugiyama', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1SuaKY2cFu8qcFiYjDpjXy-rQrFUEoqOZ', 'email': '', 'index': 8, 'id': 'aapi', 'leader_array': ['Jeanette Nguyen', 'Mason Villegas', 'Sarah Cheung'], 'leader_info': [{'name': 'Jeanette Nguyen', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jeanette&const_search_last_name=Nguyen', 'is_not_last': True}, {'name': 'Mason Villegas', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mason&const_search_last_name=Villegas', 'is_not_last': True, 'is_not_first': True}, {'name': 'Sarah Cheung', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Cheung', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Pierre Carmona', 'Joanne Sugiyama'], 'sponsor_info': [{'name': 'Pierre Carmona', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Pierre&const_search_last_name=Carmona', 'is_not_last': True}, {'name': 'Joanne Sugiyama', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Joanne&const_search_last_name=Sugiyama', 'is_not_last': False, 'is_not_first': True}]}, {'timestamp': '8/13/2020 10:43:44', 'name': 'Red Cross Club', 'description': 'This is a club for anyone interested in community service and public health. Due to online school, we will be meeting over zoom to discuss COVID-19, public health issues, as well as discussing drives and other activities for the future. We want to provide a space for students interested in helping their community as well as being knowledgeable about public health inequality. ', 'leaders': 'Sydney Srivastava, Jane Shvartsman', 'sponsor': 'Corinne Limbach', 'meeting_time': 'Monday lunch', 'image': '', 'email': '', 'index': 9, 'id': 'red-cross-club', 'leader_array': ['Sydney Srivastava', 'Jane Shvartsman'], 'leader_info': [{'name': 'Sydney Srivastava', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sydney&const_search_last_name=Srivastava', 'is_not_last': True}, {'name': 'Jane Shvartsman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jane&const_search_last_name=Shvartsman', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Corinne Limbach'], 'sponsor_info': [{'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/13/2020 19:39:52', 'name': 'Men of Color Group', 'description': 'This is an affinity group for men of color to talk about issues or attitudes that have been perpetuated in our respective communities.', 'leaders': 'Kai Martell, Luqmaan Shaikh', 'sponsor': 'Nate Lundy', 'meeting_time': 'Friday lunch', 'image': '', 'email': '', 'index': 10, 'id': 'men-of-color-group', 'leader_array': ['Kai Martell', 'Luqmaan Shaikh'], 'leader_info': [{'name': 'Kai Martell', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Kai&const_search_last_name=Martell', 'is_not_last': True}, {'name': 'Luqmaan Shaikh', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Luqmaan&const_search_last_name=Shaikh', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/14/2020 15:43:03', 'name': 'Dungeons and Dragons Club', 'description': 'A club for people to play Dungeons and Dragons.', 'leaders': 'Ella Barrett, Victoria Mann, Madeline Boyle', 'sponsor': 'Albert Boyle', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1CWJ-jp_qMol2H009SzD9pIqKlGv705Qt', 'email': '', 'index': 11, 'id': 'dungeons-and-dragons-club', 'leader_array': ['Ella Barrett', 'Victoria Mann', 'Madeline Boyle'], 'leader_info': [{'name': 'Ella Barrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ella&const_search_last_name=Barrett', 'is_not_last': True}, {'name': 'Victoria Mann', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Victoria&const_search_last_name=Mann', 'is_not_last': True, 'is_not_first': True}, {'name': 'Madeline Boyle', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Madeline&const_search_last_name=Boyle', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Albert Boyle'], 'sponsor_info': [{'name': 'Albert Boyle', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Albert&const_search_last_name=Boyle', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/14/2020 17:39:26', 'name': 'Riot ', 'description': "We are a Women of Color club/affinity space. We work to make all WOC at UHS feel comfortable in this community and to provide a space for the discussion of many, many related issues!  Although we are a closed affinity space, we frequently hold open meetings, or meetings in collaboration with other clubs like SWEAR, Men's group, Spectra, and more. ", 'leaders': 'Sami Lee, Maya Patel', 'sponsor': 'Alexandra Simmons, Tilda Kapuya (uncertain)', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1fk0NpBGB_oc4tfxS-lZ00EUqtrt-yKF5', 'email': '', 'index': 12, 'id': 'riot-', 'leader_array': ['Sami Lee', 'Maya Patel'], 'leader_info': [{'name': 'Sami Lee', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sami&const_search_last_name=Lee', 'is_not_last': True}, {'name': 'Maya Patel', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Maya&const_search_last_name=Patel', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Alexandra Simmons', 'Tilda Kapuya (uncertain)'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': True}, {'name': 'Tilda Kapuya (uncertain)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Tilda&const_search_last_name=Kapuya', 'is_not_last': False, 'is_not_first': True}]}, {'timestamp': '8/15/2020 16:32:30', 'name': 'Understanding Whiteness', 'description': 'Understanding Whiteness is a discussion space for students who identify as white. The space will be used to talk about and further understand whiteness and how that plays a role in our classrooms, clubs and other UHS spaces. We will focus on whiteness at UHS, in the Bay Area and in the world at large, and how we see whiteness appear in current events. This is a white affinity because we want to create a sustained space for the white members of the UHS community to talk about race. We will be working in partnership with the adult Understanding Whiteness group for some meetings, and hopefully with other affinity spaces as well. ', 'leaders': "Chloe Richmond ('21), Emmy Etlin ('21)", 'sponsor': 'Jen Kent', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=180Oon8EWDpXqOyGpv55HtYLs1V56-RIn', 'email': '', 'index': 13, 'id': 'understanding-whiteness', 'leader_array': ["Chloe Richmond ('21)", "Emmy Etlin ('21)"], 'leader_info': [{'name': "Chloe Richmond ('21)", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Chloe&const_search_last_name=Richmond', 'is_not_last': True}, {'name': "Emmy Etlin ('21)", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emmy&const_search_last_name=Etlin', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jen Kent'], 'sponsor_info': [{'name': 'Jen Kent', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jen&const_search_last_name=Kent', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/16/2020 10:20:56', 'name': 'Yearbook', 'description': "Yearbook is a club focused on capturing the moments shared by the UHS community. This will be an open space to all who want to participate and learn/apply aspects of graphic design and photography! Despite the fact that we may not have the chance to be together for a while, we still want to create an aspect of our school that lets all of us participate with one another. We can't wait to see what comes up!", 'leaders': "Lauren Teotico '21, Pierce Hoenigman '21, Janavi Padala '21, Janine Navalta '22", 'sponsor': 'Elizabeth Faris', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1vVu2mj2nsjr33PrC2naYaE6ET7NwApu9', 'email': '', 'index': 14, 'id': 'yearbook', 'leader_array': ["Lauren Teotico '21", "Pierce Hoenigman '21", "Janavi Padala '21", "Janine Navalta '22"], 'leader_info': [{'name': "Lauren Teotico '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lauren&const_search_last_name=Teotico', 'is_not_last': True}, {'name': "Pierce Hoenigman '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Pierce&const_search_last_name=Hoenigman', 'is_not_last': True, 'is_not_first': True}, {'name': "Janavi Padala '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Janavi&const_search_last_name=Padala', 'is_not_last': True, 'is_not_first': True}, {'name': "Janine Navalta '22", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Janine&const_search_last_name=Navalta', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Elizabeth Faris'], 'sponsor_info': [{'name': 'Elizabeth Faris', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Faris', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/16/2020 17:51:25', 'name': 'Spectra', 'description': 'Spectra will serve as an affinity safe space space for LGBT+ students and faculty. In addition to providing an affinity space, we will hold open meetings and hold discussions to educate the broader UHS community about the issues our community faces.', 'leaders': 'Nico Brubaker, Ariane Vidal, Hannah Urisman', 'sponsor': 'Andrew Galatas', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=143xdpESH3A_Q6ZAKBN5BWszq2H7PQ9mm', 'email': '', 'index': 15, 'id': 'spectra', 'leader_array': ['Nico Brubaker', 'Ariane Vidal', 'Hannah Urisman'], 'leader_info': [{'name': 'Nico Brubaker', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nico&const_search_last_name=Brubaker', 'is_not_last': True}, {'name': 'Ariane Vidal', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=Vidal', 'is_not_last': True, 'is_not_first': True}, {'name': 'Hannah Urisman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hannah&const_search_last_name=Urisman', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Andrew Galatas'], 'sponsor_info': [{'name': 'Andrew Galatas', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Andrew&const_search_last_name=Galatas', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/17/2020 11:08:53', 'name': 'Family Matters Affinity Group', 'description': 'Part of the UHS mission statement: "Together we work to build and sustain a community of diverse backgrounds, perspectives, and talents." We will create a safe space for people with diverse family structures (e.g. adopted, trans-racially adopted, single parent, divorced parents, blended households, etc.) to share experiences and support each other and enlarge our visibility in the UHS community. Our goal is to acknowledge our family differences and make them more visible in the community;  when we can see each other more clearly, our community becomes stronger.\n', 'leaders': 'Alex Perry, Lucas Perry', 'sponsor': 'Eric Johnson', 'meeting_time': 'Wednesday clubs/affinity', 'image': '', 'email': '', 'index': 19, 'id': 'family-matters-affinity-group', 'leader_array': ['Alex Perry', 'Lucas Perry'], 'leader_info': [{'name': 'Alex Perry', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alex&const_search_last_name=Perry', 'is_not_last': True}, {'name': 'Lucas Perry', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lucas&const_search_last_name=Perry', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Eric Johnson'], 'sponsor_info': [{'name': 'Eric Johnson', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Eric&const_search_last_name=Johnson', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/17/2020 11:35:19', 'name': 'Body Positive Club', 'description': 'This club is focused on spreading body positivity and love in the UHS community and beyond. Throughout the year we will cover topics ranging from eating disorders to social media to the culture around bodies at UHS. The meetings are always open to everyone. ', 'leaders': 'Elizabeth Evers, Robbie Grisso, Athena Nooney', 'sponsor': 'Corinne Limbach', 'meeting_time': 'Thursday lunch', 'image': '', 'email': '', 'index': 20, 'id': 'body-positive-club', 'leader_array': ['Elizabeth Evers', 'Robbie Grisso', 'Athena Nooney'], 'leader_info': [{'name': 'Elizabeth Evers', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Evers', 'is_not_last': True}, {'name': 'Robbie Grisso', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Robbie&const_search_last_name=Grisso', 'is_not_last': True, 'is_not_first': True}, {'name': 'Athena Nooney', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Athena&const_search_last_name=Nooney', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Corinne Limbach'], 'sponsor_info': [{'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/17/2020 16:41:02', 'name': 'Jewish Club', 'description': 'Jewish Club welcomes all members of the UHS community to discuss different aspects of the Jewish identity. Together, we will celebrate holidays, discuss controversies in the Jewish community and exchange stories of different Jewish experiences. In the past, some of our most successful meetings have been about Jews and sports, Israel and Palestine, and Jewish comedy. We encourage you to come to our meetings, whether you identify as Jewish, Jew-ish or neither!', 'leaders': 'Emmy Etlin (‘21), Eve Andersen (‘21), Noah Mays-Smith (‘22), Jacob Neplokh (‘23)', 'sponsor': 'Carol Coles', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1dT7fV3YwhOCkmAwWK7cDspJG8giKp2nN', 'email': '', 'index': 21, 'id': 'jewish-club', 'leader_array': ['Emmy Etlin (‘21)', 'Eve Andersen (‘21)', 'Noah Mays-Smith (‘22)', 'Jacob Neplokh (‘23)'], 'leader_info': [{'name': 'Emmy Etlin (‘21)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emmy&const_search_last_name=Etlin', 'is_not_last': True}, {'name': 'Eve Andersen (‘21)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Eve&const_search_last_name=Andersen', 'is_not_last': True, 'is_not_first': True}, {'name': 'Noah Mays-Smith (‘22)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Noah&const_search_last_name=Mays-Smith', 'is_not_last': True, 'is_not_first': True}, {'name': 'Jacob Neplokh (‘23)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jacob&const_search_last_name=Neplokh', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Carol Coles'], 'sponsor_info': [{'name': 'Carol Coles', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Carol&const_search_last_name=Coles', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/17/2020 19:13:08', 'name': 'Interfaith', 'description': 'Interfaith is a club for students and faculty to have open conversations about faith and spirituality. With UHS being a secular school, we recognize that it may be difficult to find safe spaces to discuss faith; therefore, we hope to provide such a space with our club. We would also like to emphasize that we are not an affinity group; anyone is welcome at our meetings, regardless of their religious affiliation or lack thereof. ', 'leaders': 'Ariane Vidal, Erica Cooper, Clarissa Dann', 'sponsor': 'Kate Garrett', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1ttXHVyJTOQ7wBtLrMUYHu1imjdGnWV3a', 'email': '', 'index': 22, 'id': 'interfaith', 'leader_array': ['Ariane Vidal', 'Erica Cooper', 'Clarissa Dann'], 'leader_info': [{'name': 'Ariane Vidal', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=Vidal', 'is_not_last': True}, {'name': 'Erica Cooper', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Erica&const_search_last_name=Cooper', 'is_not_last': True, 'is_not_first': True}, {'name': 'Clarissa Dann', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Clarissa&const_search_last_name=Dann', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Kate Garrett'], 'sponsor_info': [{'name': 'Kate Garrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Kate&const_search_last_name=Garrett', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/18/2020 8:45:13', 'name': 'Book Club', 'description': "For our club, we plan to read a book and discuss it and possibly discuss movies too. It will take a while to read the book or watch the movie so we won't meet consecutively.  \n\nWe invite everyone to come out. ", 'leaders': 'Jack Clancy', 'sponsor': 'Hayley Beale ', 'meeting_time': 'TBD', 'image': '', 'email': '', 'index': 23, 'id': 'book-club', 'leader_array': ['Jack Clancy'], 'leader_info': [{'name': 'Jack Clancy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jack&const_search_last_name=Clancy', 'is_not_last': True}], 'sponsor_array': ['Hayley Beale '], 'sponsor_info': [{'name': 'Hayley Beale ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hayley&const_search_last_name=Beale', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/19/2020 0:40:28', 'name': 'Financial Aid and Socio-Economic Status  (FASES)', 'description': 'FASES is a club focused on addressing and tackling issues of socio-economic status and wealth within our community and beyond. We hold both affinity meetings for students on financial aid and open meetings for all to attend.', 'leaders': 'Jasmine Gonzalez, Frank Wercinski, Chloe Richmond, Drew Phillips, Gaby Garcia', 'sponsor': 'Nate Lundy, Jenny Schneider', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1LzLOB0I_eCVo1O6cBKd03arznTpnXwff', 'email': '', 'index': 25, 'id': 'financial-aid-and-socio-economic-status--(fases)', 'leader_array': ['Jasmine Gonzalez', 'Frank Wercinski', 'Chloe Richmond', 'Drew Phillips', 'Gaby Garcia'], 'leader_info': [{'name': 'Jasmine Gonzalez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jasmine&const_search_last_name=Gonzalez', 'is_not_last': True}, {'name': 'Frank Wercinski', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Frank&const_search_last_name=Wercinski', 'is_not_last': True, 'is_not_first': True}, {'name': 'Chloe Richmond', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Chloe&const_search_last_name=Richmond', 'is_not_last': True, 'is_not_first': True}, {'name': 'Drew Phillips', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Drew&const_search_last_name=Phillips', 'is_not_last': True, 'is_not_first': True}, {'name': 'Gaby Garcia', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Gaby&const_search_last_name=Garcia', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy', 'Jenny Schneider'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': True}, {'name': 'Jenny Schneider', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jenny&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}]}, {'timestamp': '8/19/2020 11:09:47', 'name': 'BioMed club', 'description': "BioMed club is focusing on topics such as vaccine development, clinical trials, and health inequalities. We aim to have speakers every other month covering different topics and meetings in between speakers to debrief and learn about our next speaker. There's no need to come to every meeting; if you see a topic that interests you feel free to drop in!", 'leaders': 'Lucy Falzone, Meryl Sampson', 'sponsor': 'Emma Hartmann', 'meeting_time': 'Tuesday lunch', 'image': '', 'email': '', 'index': 27, 'id': 'biomed-club', 'leader_array': ['Lucy Falzone', 'Meryl Sampson'], 'leader_info': [{'name': 'Lucy Falzone', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lucy&const_search_last_name=Falzone', 'is_not_last': True}, {'name': 'Meryl Sampson', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Meryl&const_search_last_name=Sampson', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Emma Hartmann'], 'sponsor_info': [{'name': 'Emma Hartmann', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emma&const_search_last_name=Hartmann', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/19/2020 12:21:28', 'name': 'UNICEF Club', 'description': 'We are focused on fundraising, advocacy/raising awareness, community building, and volunteering locally. This is a club open to everyone and we would love new faces! ', 'leaders': 'Mirabel Haskin Fernald, Katie Crawford', 'sponsor': 'undecided- we will email Alexandra when we know. ', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1wyrKwmQ5qOBkhg59tobzl-5pL0wYR6BM', 'email': '', 'index': 28, 'id': 'unicef-club', 'leader_array': ['Mirabel Haskin Fernald', 'Katie Crawford'], 'leader_info': [{'name': 'Mirabel Haskin Fernald', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mirabel&const_search_last_name=Haskin', 'is_not_last': True}, {'name': 'Katie Crawford', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Katie&const_search_last_name=Crawford', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['undecided- we will email Alexandra when we know. '], 'sponsor_info': [{'name': 'undecided- we will email Alexandra when we know. ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=undecided-&const_search_last_name=we', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/19/2020 13:43:08', 'name': 'Science Olympiad', 'description': 'A chill club to explore scientific topics not formally taught by UHS and a chance to pursue other scientific interests with your peers in a semi-competitive or fun and experimental environment. ', 'leaders': 'Christian Canete, Sarah Cheung, Ella Barrett', 'sponsor': 'Luke Probst, Ozzie Nevarez', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1biN1bF3j2qp61vNp1uCHLBlWNJNE2ShF', 'email': '', 'index': 29, 'id': 'science-olympiad', 'leader_array': ['Christian Canete', 'Sarah Cheung', 'Ella Barrett'], 'leader_info': [{'name': 'Christian Canete', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Christian&const_search_last_name=Canete', 'is_not_last': True}, {'name': 'Sarah Cheung', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Cheung', 'is_not_last': True, 'is_not_first': True}, {'name': 'Ella Barrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ella&const_search_last_name=Barrett', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Luke Probst', 'Ozzie Nevarez'], 'sponsor_info': [{'name': 'Luke Probst', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Luke&const_search_last_name=Probst', 'is_not_last': True}, {'name': 'Ozzie Nevarez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ozzie&const_search_last_name=Nevarez', 'is_not_last': False, 'is_not_first': True}]}, {'timestamp': '8/21/2020 9:34:15', 'name': "Men's Group", 'description': "Men's Group strives to be a space for men to examine, critique, and reflect on issues of masculinity, as well as a safe space for men to be open and vulnerable. We will have some meetings, closed to self-indentified males. ", 'leaders': 'Owen Myers (2021), Drew Phillips (2021), Frank Wercinski (2021), Luqmaan Shaikh (2021)', 'sponsor': 'Marcus Caimi', 'meeting_time': 'Tuesday lunch', 'image': '', 'email': '', 'index': 30, 'id': "men's-group", 'leader_array': ['Owen Myers (2021)', 'Drew Phillips (2021)', 'Frank Wercinski (2021)', 'Luqmaan Shaikh (2021)'], 'leader_info': [{'name': 'Owen Myers (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Owen&const_search_last_name=Myers', 'is_not_last': True}, {'name': 'Drew Phillips (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Drew&const_search_last_name=Phillips', 'is_not_last': True, 'is_not_first': True}, {'name': 'Frank Wercinski (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Frank&const_search_last_name=Wercinski', 'is_not_last': True, 'is_not_first': True}, {'name': 'Luqmaan Shaikh (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Luqmaan&const_search_last_name=Shaikh', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Marcus Caimi'], 'sponsor_info': [{'name': 'Marcus Caimi', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Marcus&const_search_last_name=Caimi', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 12:26:01', 'name': 'Disney Club', 'description': "We plan on doing screenings of your favorite Disney and Pixar movies! We are always open to suggestions so if you have a childhood fav you'd like us to screen, let us know. Anyone who still feels like a child at heart is encouraged to come :) ", 'leaders': 'Katie Hartel, Sara Tagol', 'sponsor': 'Elizabeth Schaffernoth', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1X800rNe-dESui73xF6zMMm9WShH6Q2kx', 'email': '', 'index': 31, 'id': 'disney-club', 'leader_array': ['Katie Hartel', 'Sara Tagol'], 'leader_info': [{'name': 'Katie Hartel', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Katie&const_search_last_name=Hartel', 'is_not_last': True}, {'name': 'Sara Tagol', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sara&const_search_last_name=Tagol', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Elizabeth Schaffernoth'], 'sponsor_info': [{'name': 'Elizabeth Schaffernoth', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Schaffernoth', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 13:00:15', 'name': 'Satonics', 'description': 'This club is UHS’s a cappella group and is open to anyone who is accepted via an informal audition. We make music entirely with our voices and sing a variety of music, from pop songs to jazz arrangements, and perform at concerts and competitions. We will be holding auditions through Zoom next Friday (29th) and Saturday (30th), with more information to sign up in an email. We especially encourage underclassmen and those with lower voices to audition! Until further notice from the high school a cappella competition we participate in (Varsity Vocals ICHSA), our group will perform for school concerts through pre-recorded songs.', 'leaders': 'Sarah Cheung, Matthew Gin,, Madelyn Ocker', 'sponsor': 'Joel Chapman', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1r4zT6QBHRw4yNHs8Q_rkRac9gAjFByUu', 'email': '', 'index': 32, 'id': 'satonics', 'leader_array': ['Sarah Cheung', 'Matthew Gin,', 'Madelyn Ocker'], 'leader_info': [{'name': 'Sarah Cheung', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Cheung', 'is_not_last': True}, {'name': 'Matthew Gin,', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Matthew&const_search_last_name=Gin,', 'is_not_last': True, 'is_not_first': True}, {'name': 'Madelyn Ocker', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Madelyn&const_search_last_name=Ocker', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Joel Chapman'], 'sponsor_info': [{'name': 'Joel Chapman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Joel&const_search_last_name=Chapman', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 14:14:48', 'name': 'Multiracial Club', 'description': 'An affinity space for students and faculty that self-identify as biracial or multiracial. ', 'leaders': "Arianna Schwartz ’22, Phia Black ’23, Owen Myers ’21, Amelie Scheil '21, Lauren Schneider '21", 'sponsor': 'Nate Lundy', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1iRw4xM3-Ss7EvGAItqS2jeVYPSppBvdv', 'email': '', 'index': 33, 'id': 'multiracial-club', 'leader_array': ['Arianna Schwartz ’22', 'Phia Black ’23', 'Owen Myers ’21', "Amelie Scheil '21", "Lauren Schneider '21"], 'leader_info': [{'name': 'Arianna Schwartz ’22', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Arianna&const_search_last_name=Schwartz', 'is_not_last': True}, {'name': 'Phia Black ’23', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Phia&const_search_last_name=Black', 'is_not_last': True, 'is_not_first': True}, {'name': 'Owen Myers ’21', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Owen&const_search_last_name=Myers', 'is_not_last': True, 'is_not_first': True}, {'name': "Amelie Scheil '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Amelie&const_search_last_name=Scheil', 'is_not_last': True, 'is_not_first': True}, {'name': "Lauren Schneider '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lauren&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 14:27:02', 'name': 'Artivism Club', 'description': 'The purpose of Artivism club is to explore the intersection of art and activism, through art projects, fundraisers, and club meetings. We plan to collaborate with clubs such as BSU, Riot, and SWEAR in order to explore art as a vehicle for social justice. Previous projects include a mural for Summerbridge (featured in the hallway of Upper campus), poster-making sessions, and lunch workshops on color theory/design principles. Our meetings are open to everyone, regardless of identity or prior artistic experience! ', 'leaders': 'Amelie Scheil, Jiho Lee', 'sponsor': 'Jenifer Kent', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1UgyFO_nPxNFkkr_EXDUL6gY6fxzD9rwv', 'email': '', 'index': 34, 'id': 'artivism-club', 'leader_array': ['Amelie Scheil', 'Jiho Lee'], 'leader_info': [{'name': 'Amelie Scheil', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Amelie&const_search_last_name=Scheil', 'is_not_last': True}, {'name': 'Jiho Lee', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jiho&const_search_last_name=Lee', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jenifer Kent'], 'sponsor_info': [{'name': 'Jenifer Kent', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jenifer&const_search_last_name=Kent', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 14:37:40', 'name': 'Girls Who Code', 'description': "Girls Who Code is a national non-profit organization working to close the gender gap in technology. Our club educates, equips, and inspires girls with the computing skills they'll need to pursue 21st-century opportunities.", 'leaders': "Amelie Scheil '21, Isabella Hochschild '21, Alicia Lopez-Guerra '22", 'sponsor': 'Leah Dorazio', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1ilPU8lENicf97gsFnfbO56i5T9cqV57J', 'email': 'amelie.scheil_21@sfuhs.org', 'index': 35, 'id': 'girls-who-code', 'leader_array': ["Amelie Scheil '21", "Isabella Hochschild '21", "Alicia Lopez-Guerra '22"], 'leader_info': [{'name': "Amelie Scheil '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Amelie&const_search_last_name=Scheil', 'is_not_last': True}, {'name': "Isabella Hochschild '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Isabella&const_search_last_name=Hochschild', 'is_not_last': True, 'is_not_first': True}, {'name': "Alicia Lopez-Guerra '22", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alicia&const_search_last_name=Lopez-Guerra', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Leah Dorazio'], 'sponsor_info': [{'name': 'Leah Dorazio', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Leah&const_search_last_name=Dorazio', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 15:27:11', 'name': 'Hapa (half white half asian affinity group)', 'description': 'Hapa is a term used to describe a person who is half asian and half white. This affinity group, with closed meetings, will delve into the complexity that arises with a dual identity. ', 'leaders': 'Anna Neumann-Loreck, Lauren Schneider', 'sponsor': 'Andrew Galatas ', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1Nv-_3OZIR3FI1Z4P0BGK_CRtBghmwvRt', 'email': 'lauren.schneider_21@sfuhs.org', 'index': 37, 'id': 'hapa-(half-white-half-asian-affinity-group)', 'leader_array': ['Anna Neumann-Loreck', 'Lauren Schneider'], 'leader_info': [{'name': 'Anna Neumann-Loreck', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Anna&const_search_last_name=Neumann-Loreck', 'is_not_last': True}, {'name': 'Lauren Schneider', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lauren&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Andrew Galatas '], 'sponsor_info': [{'name': 'Andrew Galatas ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Andrew&const_search_last_name=Galatas', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 16:02:38', 'name': 'Avatar: The Last Airbender Club', 'description': 'Our club welcomes fans of the Avatar universe, including Avatar: The Last Airbender and Legend of Korra. I think we can all agree that it is the best show ever written, so we decided to make a club to appreciate its brilliance. We will watch episodes, discuss opinions and themes, take fun "which bender am I" quizzes and appreciate the show and its excellence.', 'leaders': 'Ariane Vidal, Hannah Urisman', 'sponsor': 'Adrian Acu', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1M4wtD2PLLN4TN94RMQRujwIsQ9SGFh_V', 'email': 'hannah.urisman_22@sfuhs.org', 'index': 38, 'id': 'avatar:-the-last-airbender-club', 'leader_array': ['Ariane Vidal', 'Hannah Urisman'], 'leader_info': [{'name': 'Ariane Vidal', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=Vidal', 'is_not_last': True}, {'name': 'Hannah Urisman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hannah&const_search_last_name=Urisman', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Adrian Acu'], 'sponsor_info': [{'name': 'Adrian Acu', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Adrian&const_search_last_name=Acu', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 16:58:57', 'name': 'Conservative Club', 'description': "UHS Conservative Club is a club dedicated to promoting substantive discussion of political ideas. We believe that when 80% of liberal students feel confident sharing their political views, but 80% of conservative students do not, real debate can never be achieved. To join, you don't need to hold any particular viewpoints on any issue, and you don't even need to be conservative (in fact, we welcome and value differing perspectives). All you need to believe is that UHS, and the United States as a whole, will be a better place if we allow open and honest debate and exchange of ideas, and that echo chambers aren't good for anyone. Our goal is to provide a forum for conservative thought that is mainstream in the United States, but not often represented at UHS.\n\nWe will meet every few weeks to discuss current events, the political climate on campus and in the country, or host a guest speaker.", 'leaders': 'Dan Huguenin, Tyler Sisitsky', 'sponsor': 'Kate Garrett', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1ZnMS1INYZDiydg5lmq5WPDAvAQpedMIi', 'email': 'dan.huguenin_21@sfuhs.org', 'index': 39, 'id': 'conservative-club', 'leader_array': ['Dan Huguenin', 'Tyler Sisitsky'], 'leader_info': [{'name': 'Dan Huguenin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Dan&const_search_last_name=Huguenin', 'is_not_last': True}, {'name': 'Tyler Sisitsky', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Tyler&const_search_last_name=Sisitsky', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Kate Garrett'], 'sponsor_info': [{'name': 'Kate Garrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Kate&const_search_last_name=Garrett', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/21/2020 17:17:45', 'name': 'White Folks Committed to Anti-Racism Affinity Space', 'description': '“I can’t build externally what I haven’t built internally.”\nDr. Cornel West\n \n \nThis is an invitation for all folks who identify as white and are striving toward an identity of anti-racist. This is a space to gather and process the complexity of what it means to be white identifying human beings at this time with a focus on building a competent and firm foundation of anti-racism. This is a supportive and safe space. We will make mistakes. We will have all the best intentions and still have a negative impact. This is a space to learn and grow together, that our intentions may align with our actions, that we may shift to being influential as opposed to impactful. We will bring all our humanness to the table and hold space for all of it.\n ', 'leaders': "(we want but don't have yet!)", 'sponsor': 'Corinne Limbach, Lindsay Repko, Lisa Carroll', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1LnaXI2SXVKV7XrUJj68h3vSKzChiIsow', 'email': 'lisa.carroll@sfuhs.org', 'index': 40, 'id': 'white-folks-committed-to-anti-racism-affinity-space', 'leader_array': ["(we want but don't have yet!)"], 'leader_info': [{'name': "(we want but don't have yet!)", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=(we&const_search_last_name=want', 'is_not_last': True}], 'sponsor_array': ['Corinne Limbach', 'Lindsay Repko', 'Lisa Carroll'], 'sponsor_info': [{'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': True}, {'name': 'Lindsay Repko', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lindsay&const_search_last_name=Repko', 'is_not_last': True, 'is_not_first': True}, {'name': 'Lisa Carroll', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lisa&const_search_last_name=Carroll', 'is_not_last': False, 'is_not_first': True}]}, {'timestamp': '8/21/2020 17:27:13', 'name': 'Mental Health Coalition', 'description': 'Mental Health Advocacy', 'leaders': 'TBD: currently in process', 'sponsor': 'Lindsay Repko (may add others)', 'meeting_time': 'Tuesday lunch', 'image': '', 'email': 'lindsay.repko@sfuhs.org', 'index': 41, 'id': 'mental-health-coalition', 'leader_array': ['TBD: currently in process'], 'leader_info': [{'name': 'TBD: currently in process', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=TBD:&const_search_last_name=currently', 'is_not_last': True}], 'sponsor_array': ['Lindsay Repko (may add others)'], 'sponsor_info': [{'name': 'Lindsay Repko (may add others)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lindsay&const_search_last_name=Repko', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/22/2020 17:44:33', 'name': 'HIstory of History of History of History of Surf Club Club Club Club Club', 'description': 'This club will tell the historic odyssey of surf club at UHS. It will then delve deeper into topics of surf history and culture. From there, we will approach a variety of modern issues such as global warming, environmental preservation and sustainability, and more.', 'leaders': 'Ren Zanze (President), Mica (President)  ', 'sponsor': 'Scott Laughlin', 'meeting_time': 'Friday lunch', 'image': '', 'email': 'ren.zanze_21@sfuhs.org', 'index': 42, 'id': 'history-of-history-of-history-of-history-of-surf-club-club-club-club-club', 'leader_array': ['Ren Zanze (President)', 'Mica (President)  '], 'leader_info': [{'name': 'Ren Zanze (President)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ren&const_search_last_name=Zanze', 'is_not_last': True}, {'name': 'Mica (President)  ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mica&const_search_last_name=(President)', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Scott Laughlin'], 'sponsor_info': [{'name': 'Scott Laughlin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Scott&const_search_last_name=Laughlin', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/22/2020 21:18:27', 'name': "Women's Health Club", 'description': 'The mission of our club is to spread awareness about how common sexual assault/rape is in our society and educate students through stories, guest speakers, social media, documentaries, and other sources. We hope to become advocates for change by working with organizations in San Francisco as well as providing a safe space for UHS students to learn and talk about these issues. This club will have a few closed meetings but will mostly be open for everyone.', 'leaders': 'Ria Dhillon, Malia House', 'sponsor': 'Barbara Holler ', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1e74BJbPfHCyirNbM4MExRl3h_7QralGf', 'email': 'malia.house_22@sfuhs.org', 'index': 43, 'id': "women's-health-club", 'leader_array': ['Ria Dhillon', 'Malia House'], 'leader_info': [{'name': 'Ria Dhillon', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ria&const_search_last_name=Dhillon', 'is_not_last': True}, {'name': 'Malia House', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Malia&const_search_last_name=House', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Barbara Holler '], 'sponsor_info': [{'name': 'Barbara Holler ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Barbara&const_search_last_name=Holler', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/25/2020 13:09:08', 'name': 'The Radio Broadcast Club', 'description': 'In this club we will listen to old radio theater broadcasts as well as rewrite them or recreate them! As a form of online drama!', 'leaders': 'Harper Clementz (10th) , Ariane (11th)', 'sponsor': 'Ryan O’Donnell ', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1NRLA2QMsogjPDLYodEcZylLaSaCA6CnQ', 'email': 'harper.clementz_23@sfuhs.org', 'index': 44, 'id': 'the-radio-broadcast-club', 'leader_array': ['Harper Clementz (10th) ', 'Ariane (11th)'], 'leader_info': [{'name': 'Harper Clementz (10th) ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Harper&const_search_last_name=Clementz', 'is_not_last': True}, {'name': 'Ariane (11th)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=(11th)', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Ryan O’Donnell '], 'sponsor_info': [{'name': 'Ryan O’Donnell ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ryan&const_search_last_name=O’Donnell', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/25/2020 14:49:21', 'name': 'UHS Business Club', 'description': 'Selling short; econometrics; balance sheets...what does this all mean? The UHS Business Club provides opportunities for its members to learn about the inner workings of the business world. Through activities such as case studies, ethical debates, and projects, we will introduce our club members to careers in the business sector, current events in the finance field, and experimentation with basic business transactions. With introductions to management, marketing and investing games, get ready for some fun dives into the business world. We are open to all who would like to join!', 'leaders': 'Mericel Tao, Caroline Hall-Sherr', 'sponsor': 'David Roth', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1KLk4U3iXsTpiP4IfoYO1QuLHydSTBmPi', 'email': 'mericel.tao_22@sfuhs.org', 'index': 45, 'id': 'uhs-business-club', 'leader_array': ['Mericel Tao', 'Caroline Hall-Sherr'], 'leader_info': [{'name': 'Mericel Tao', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mericel&const_search_last_name=Tao', 'is_not_last': True}, {'name': 'Caroline Hall-Sherr', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Caroline&const_search_last_name=Hall-Sherr', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['David Roth'], 'sponsor_info': [{'name': 'David Roth', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=David&const_search_last_name=Roth', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/25/2020 15:04:25', 'name': 'UHS SWENext Club', 'description': 'From bridges to spaceships, computers to cars, engineers are the force behind many of the objects we interact with. The Society of Women Engineers (SWE) seeks to increase the representation of women in the engineering field and revamp the dynamics of the engineering workforce. Our UHS SWENext Club combines group activities, discussions about current events in engineering, and lessons about engineering to expand on SWE’s mission of empowering women engineers. Most of the activity and learning based meetings will be open to non-male identifying students, but meetings discussing current events will be open to all!', 'leaders': 'Danielle Cuthbert, Mericel Tao', 'sponsor': 'Megan Storti', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=121_Q-W2qgbuep_Bl5Rms8v8Uh2DHuze2', 'email': 'danielle.cuthbert_22@sfuhs.org', 'index': 46, 'id': 'uhs-swenext-club', 'leader_array': ['Danielle Cuthbert', 'Mericel Tao'], 'leader_info': [{'name': 'Danielle Cuthbert', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Danielle&const_search_last_name=Cuthbert', 'is_not_last': True}, {'name': 'Mericel Tao', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mericel&const_search_last_name=Tao', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Megan Storti'], 'sponsor_info': [{'name': 'Megan Storti', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Megan&const_search_last_name=Storti', 'is_not_last': False, 'is_not_first': False}]}, {'timestamp': '8/27/2020 12:37:45', 'name': 'Investment Club', 'description': 'This is a club open to all students with an interest in investing and the financial world. No experience is required, we’ll learn together how to track a portfolio and research stocks. The club will have various speakers with years of experience in finance and will be an interactive space for students to learn more about investing.', 'leaders': 'Owen Flanagan', 'sponsor': 'Michael Novak (UHS Chief Financial Operations Officer)', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1gzLIHou05Ff8ukISzaEUHX3q6aEHHPCF', 'email': 'owen.flanagan_21@sfuhs.org', 'index': 47, 'id': 'investment-club', 'leader_array': ['Owen Flanagan'], 'leader_info': [{'name': 'Owen Flanagan', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Owen&const_search_last_name=Flanagan', 'is_not_last': True}], 'sponsor_array': ['Michael Novak (UHS Chief Financial Operations Officer)'], 'sponsor_info': [{'name': 'Michael Novak (UHS Chief Financial Operations Officer)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Michael&const_search_last_name=Novak', 'is_not_last': False, 'is_not_first': False}]}]);
            let shuffled_club_data = shuffleArray(club_data);
            var club_dict = {'Model United Nations': {'timestamp': '8/28/2020 10:37:32', 'email': 'emilia.fowler_21@sfuhs.org', 'name': 'Model United Nations', 'description': "Model UN is a club dedicated to teaching students about international affairs through a UN simulation that takes place in competitive conferences. We use meetings to educate and prepare for conferences, which we attend several times throughout the year. As one of only two clubs with overnight trips, delegates have plenty of opportunities to make friends and lifelong enemies. From ordering six pints of ice cream to the hotel at 1 AM, to aggressively debating the delegation of The Seychelles, to awkwardly greeting the delegation of Italy dressed in full Roman armor, Model UN is an experience you won't forget.", 'leaders': 'Emilia Fowler, Jeanette Nguyen, Dan Huguenin', 'sponsor': 'Rochelle Devault', 'meeting_time': 'Wednesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1bZonWqkSHVC1gGGKLwwDkG6Y2tBxYUJE', 'index': 0, 'id': 'model-united-nations', 'leader_array': ['Emilia Fowler', 'Jeanette Nguyen', 'Dan Huguenin'], 'leader_info': [{'name': 'Emilia Fowler', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emilia&const_search_last_name=Fowler', 'is_not_last': True}, {'name': 'Jeanette Nguyen', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jeanette&const_search_last_name=Nguyen', 'is_not_last': True, 'is_not_first': True}, {'name': 'Dan Huguenin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Dan&const_search_last_name=Huguenin', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Rochelle Devault'], 'sponsor_info': [{'name': 'Rochelle Devault', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Rochelle&const_search_last_name=Devault', 'is_not_last': False, 'is_not_first': False}]}, 'International Club': {'timestamp': '8/28/2020 10:45:05', 'email': 'mirabelle.brettke_21@sfuhs.org', 'name': 'International Club', 'description': 'International club will be a space for people who have citizenship in countries outside of the U.S., are from a country outside of the U.S., or have parents from a country outside of the U.S. to talk about what its like to hold membership in two places that could possibly be thousands of miles apart. ', 'leaders': 'Mirabelle Brettkelly, Isabella Hochschild', 'sponsor': 'Roselyne Pilaar', 'meeting_time': 'Tuesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1YQ-7OVMQZsHQK9FPbBIpSUABdVgNrkwt', 'index': 1, 'id': 'international-club', 'leader_array': ['Mirabelle Brettkelly', 'Isabella Hochschild'], 'leader_info': [{'name': 'Mirabelle Brettkelly', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mirabelle&const_search_last_name=Brettkelly', 'is_not_last': True}, {'name': 'Isabella Hochschild', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Isabella&const_search_last_name=Hochschild', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Roselyne Pilaar'], 'sponsor_info': [{'name': 'Roselyne Pilaar', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Roselyne&const_search_last_name=Pilaar', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, 'Riot': {'timestamp': '8/28/2020 10:48:31', 'email': 'maya.patel_21@sfuhs.org', 'name': 'Riot', 'description': "We are a women of color club/affinity space! We work to make sure all WOC at UHS feel comfortable in this community and provide a space for the discussion of many related issues. Although we are an affinity space, we frequently hold open meetings or meetings in collaboration with other clubs like SWEAR, Men's Group, Spectra, and more. ", 'leaders': 'Maya Patel, Samantha Lee', 'sponsor': 'Alexandra Simmons', 'meeting_time': 'Wednesday Clubs/Affinity', 'image': 'https://drive.google.com/uc?export=view&id=14K3Y3heQscDppBd-oPr92d-q-N-nF-kN', 'index': 2, 'id': 'riot', 'leader_array': ['Maya Patel', 'Samantha Lee'], 'leader_info': [{'name': 'Maya Patel', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Maya&const_search_last_name=Patel', 'is_not_last': True}, {'name': 'Samantha Lee', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Samantha&const_search_last_name=Lee', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Alexandra Simmons'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, 'LatinX United': {'timestamp': '8/28/2020 11:38:43', 'email': 'evancarlo.fowler_21@sfuhs.org', 'name': 'LatinX United', 'description': 'LatinX United is an affinity club for members of the UHS community who identify as LatinX. We host weekly meetings to discuss current events, connect as a community, and act as resources for each other. We also organize and host fundraisers for causes that affect LatinX people in the Bay Area and around the world.', 'leaders': 'Evan-Carlo Fowler, Mica Clark-Herrera, and Brandly Mazariegos', 'sponsor': 'Jessica Osorio ', 'meeting_time': 'Tuesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1w9hu5LswmVIxBiScZ01WnV6pEbXvqIt9', 'index': 3, 'id': 'latinx-united', 'leader_array': ['Evan-Carlo Fowler', 'Mica Clark-Herrera', 'and Brandly Mazariegos'], 'leader_info': [{'name': 'Evan-Carlo Fowler', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Evan-Carlo&const_search_last_name=Fowler', 'is_not_last': True}, {'name': 'Mica Clark-Herrera', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mica&const_search_last_name=Clark-Herrera', 'is_not_last': True, 'is_not_first': True}, {'name': 'Brandly Mazariegos', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=and&const_search_last_name=Brandly', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jessica Osorio '], 'sponsor_info': [{'name': 'Jessica Osorio ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jessica&const_search_last_name=Osorio', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, 'Sunrise Movement- UHS Hub': {'timestamp': '8/28/2020 19:08:29', 'email': 'alicia.lopezguerr_22@sfuhs.org', 'name': 'Sunrise Movement- UHS Hub', 'description': "This is a high school hub of the larger Sunrise Movement which is a non-profit working to raise awareness of and pass the Green New Deal. If enacted, the Green New Deal would force the US to become more active in fighting climate change as well as produce many sustainable jobs. \n\nWe plan to host a space through which UHS students can take part in the political fight against climate change and take part in the Sunrise Movement. We will be discussing our thoughts on the Green New Deal, ideas we have, and current events related to the Sunrise Movement and the Green New Deal. If you are passionate about climate change and the Green New Deal as well as are interested in getting politically involved but don't necessarily know how, join use, and we can work together to hopefully one day get the Green New Deal passed. ", 'leaders': 'Alicia Lopez-Guerra, Hannah Urisman, Annabelle Brauer', 'sponsor': 'Rochelle Devault ', 'meeting_time': 'Thursday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1oMZqQG5Dxi1xmW7QsYrcDbhYAjL3pB_R', 'index': 4, 'id': 'sunrise-movement--uhs-hub', 'leader_array': ['Alicia Lopez-Guerra', 'Hannah Urisman', 'Annabelle Brauer'], 'leader_info': [{'name': 'Alicia Lopez-Guerra', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alicia&const_search_last_name=Lopez-Guerra', 'is_not_last': True}, {'name': 'Hannah Urisman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hannah&const_search_last_name=Urisman', 'is_not_last': True, 'is_not_first': True}, {'name': 'Annabelle Brauer', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Annabelle&const_search_last_name=Brauer', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Rochelle Devault '], 'sponsor_info': [{'name': 'Rochelle Devault ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Rochelle&const_search_last_name=Devault', 'is_not_last': False, 'is_not_first': False}]}, 'Black Student Union (BSU)': {'timestamp': '8/30/2020 22:06:04', 'email': 'jasmine.gonzalez_21@sfuhs.org', 'name': 'Black Student Union (BSU)', 'description': "We welcome any and all members of the UHS community who identify as being a part of the African diaspora (e.g. black, African American, black-biracial, etc.). Come out for a guaranteed good time so you're ready to hang with everyone in person when it's safe to have irl cookouts :)", 'leaders': 'Jasmine Gonzalez, Anna Elgin, Alyanna Hughes', 'sponsor': 'Alexandra Simmons', 'meeting_time': 'Wednesday Clubs/Affinity', 'image': 'https://drive.google.com/uc?export=view&id=1gWtAqOvic-aiMzAP31hLzExfnENj6Yue', 'index': 5, 'id': 'black-student-union-(bsu)', 'leader_array': ['Jasmine Gonzalez', 'Anna Elgin', 'Alyanna Hughes'], 'leader_info': [{'name': 'Jasmine Gonzalez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jasmine&const_search_last_name=Gonzalez', 'is_not_last': True}, {'name': 'Anna Elgin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Anna&const_search_last_name=Elgin', 'is_not_last': True, 'is_not_first': True}, {'name': 'Alyanna Hughes', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alyanna&const_search_last_name=Hughes', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Alexandra Simmons'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': False, 'is_not_first': False}], 'is_affinity_group': True}, 'Financial Aid and Socio-Economic Status Club (FASES)': {'timestamp': '8/30/2020 22:43:36', 'email': 'jasmine.gonzalez_21@sfuhs.org', 'name': 'Financial Aid and Socio-Economic Status Club (FASES)', 'description': "FASES is a space for members of the UHS community to discuss wealth, financial aid, and the local + societal implications of both. Sometimes we'll be an affinity space for students on financial aid, and sometimes our meetings will be open to all!", 'leaders': 'Jasmine Gonzalez, Frank Wercinski, Chloe Richmond, Gaby Garcia, Drew Phillips ', 'sponsor': 'Nate Lundy, Jenny Schneider', 'meeting_time': 'Thursday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1u3Xm3qeYvmgPNB67hhgJA5C7BedKkHL-', 'index': 6, 'id': 'financial-aid-and-socio-economic-status-club-(fases)', 'leader_array': ['Jasmine Gonzalez', 'Frank Wercinski', 'Chloe Richmond', 'Gaby Garcia', 'Drew Phillips '], 'leader_info': [{'name': 'Jasmine Gonzalez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jasmine&const_search_last_name=Gonzalez', 'is_not_last': True}, {'name': 'Frank Wercinski', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Frank&const_search_last_name=Wercinski', 'is_not_last': True, 'is_not_first': True}, {'name': 'Chloe Richmond', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Chloe&const_search_last_name=Richmond', 'is_not_last': True, 'is_not_first': True}, {'name': 'Gaby Garcia', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Gaby&const_search_last_name=Garcia', 'is_not_last': True, 'is_not_first': True}, {'name': 'Drew Phillips ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Drew&const_search_last_name=Phillips', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy', 'Jenny Schneider'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': True}, {'name': 'Jenny Schneider', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jenny&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}], 'is_affinity_group': True}, 'Baking Club': {'timestamp': '8/19/2020 9:28:49', 'email': 'isabella.hochschi_21@sfuhs.org', 'name': 'Baking Club', 'description': "With the rise of quarantine banana bread, sourdough starters, and all sorts of pandemic baking, we thought it would be the perfect time to bring back Baking Club in a virtual environment. We'll be playing music and/or screen sharing the Great British Baking Show while we bake and chat from our own kitchens and everyone is invited to join! Each meeting, we'll all bake a recipe that we voted on the previous meeting, but you can bake whatever you want as well (it's also okay just to log on to hang out and watch other people bake!) This club is open to all students and faculty, no matter your baking skill level! (p.s. our header photo is from the Club Fair last year! Fingers crossed that we'll bring treats to more in-person meetings if we get the chance to go back on campus soon)", 'leaders': 'Isabella Hochschild, Mirabelle Brettkelly', 'sponsor': 'Jessica Osorio', 'meeting_time': 'Tuesday Lunch', 'image': 'https://drive.google.com/uc?export=view&id=1SDHm11___kNChZi_a5a_1xSWObn5He2h', 'index': 7, 'id': 'baking-club', 'leader_array': ['Isabella Hochschild', 'Mirabelle Brettkelly'], 'leader_info': [{'name': 'Isabella Hochschild', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Isabella&const_search_last_name=Hochschild', 'is_not_last': True}, {'name': 'Mirabelle Brettkelly', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mirabelle&const_search_last_name=Brettkelly', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jessica Osorio'], 'sponsor_info': [{'name': 'Jessica Osorio', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jessica&const_search_last_name=Osorio', 'is_not_last': False, 'is_not_first': False}]}, 'Board Game Club': {'timestamp': '8/12/2020 10:02:44', 'name': 'Board Game Club', 'description': 'A club for playing board games, especially but not limited to Secret Hitler (and now with online alternatives!)', 'leaders': 'Pierce Hoenigman', 'sponsor': 'Sandeep Bhuta', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1VxSCyWj6MufV1GDXmgG5wlRjv6UhNxpi', 'email': '', 'index': 0, 'id': 'board-game-club', 'leader_array': ['Pierce Hoenigman'], 'leader_info': [{'name': 'Pierce Hoenigman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Pierce&const_search_last_name=Hoenigman', 'is_not_last': True}], 'sponsor_array': ['Sandeep Bhuta'], 'sponsor_info': [{'name': 'Sandeep Bhuta', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sandeep&const_search_last_name=Bhuta', 'is_not_last': False, 'is_not_first': False}]}, "SWEAR (Students for Women's Equality and Rights)": {'timestamp': '8/12/2020 10:38:12', 'name': "SWEAR (Students for Women's Equality and Rights)", 'description': 'SWEAR (Students for Women’s Equality and Rights) is a space on campus created to discuss all things pertaining to self-identifying women/people who identify with the female experience, including current events, mental health, sex, and other various topics. We believe intersectionality is vital to any conversation about the female experience and we strive for our meetings to be welcoming to people from all backgrounds and experiences. We believe amplifying the voices of women of color at UHS is essential to our community. We host both closed and open meetings as well as events like the Mental Health Workshop and the SWEAR Sleepover.', 'leaders': 'Elizabeth Evers, Sarah Walcott, Sara Tagol, Lindsay Eiseman,, Katherine Holden', 'sponsor': 'Jessica Osorio, Corinne Limbach', 'meeting_time': 'Friday lunch', 'image': '', 'email': '', 'index': 1, 'id': "swear-(students-for-women's-equality-and-rights)", 'leader_array': ['Elizabeth Evers', 'Sarah Walcott', 'Sara Tagol', 'Lindsay Eiseman,', 'Katherine Holden'], 'leader_info': [{'name': 'Elizabeth Evers', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Evers', 'is_not_last': True}, {'name': 'Sarah Walcott', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Walcott', 'is_not_last': True, 'is_not_first': True}, {'name': 'Sara Tagol', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sara&const_search_last_name=Tagol', 'is_not_last': True, 'is_not_first': True}, {'name': 'Lindsay Eiseman,', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lindsay&const_search_last_name=Eiseman,', 'is_not_last': True, 'is_not_first': True}, {'name': 'Katherine Holden', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Katherine&const_search_last_name=Holden', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jessica Osorio', 'Corinne Limbach'], 'sponsor_info': [{'name': 'Jessica Osorio', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jessica&const_search_last_name=Osorio', 'is_not_last': True}, {'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': False, 'is_not_first': True}]}, 'Student Council': {'timestamp': '8/12/2020 12:02:26', 'name': 'Student Council', 'description': 'Student council is a faculty-supported leadership group dedicated toward teaching students leadership skills while simultaneously assisting the school with a number of tasks. Elected students organize spirit events and interface with faculty regularly to advocate for their constituents.', 'leaders': 'David Wignall', 'sponsor': 'Alexandra Simmons', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1AP-Epdfzp_H4SZGc4BUKmF7tudGxK9ap', 'email': '', 'index': 3, 'id': 'student-council', 'leader_array': ['David Wignall'], 'leader_info': [{'name': 'David Wignall', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=David&const_search_last_name=Wignall', 'is_not_last': True}], 'sponsor_array': ['Alexandra Simmons'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': False, 'is_not_first': False}]}, 'MENA ': {'timestamp': '8/12/2020 12:23:34', 'name': 'MENA ', 'description': 'MENA stands for Middle Eastern North African and is an affinity space for all people who identify with the term. We mainly have closed meetings available only to those who identify as MENA to discuss topics that relate to our community.', 'leaders': 'Sara Tagol, Darius Yamini ', 'sponsor': 'Dr. Ahmed ', 'meeting_time': 'Wednesday clubs/affinity', 'image': '', 'email': '', 'index': 4, 'id': 'mena-', 'leader_array': ['Sara Tagol', 'Darius Yamini '], 'leader_info': [{'name': 'Sara Tagol', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sara&const_search_last_name=Tagol', 'is_not_last': True}, {'name': 'Darius Yamini ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Darius&const_search_last_name=Yamini', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Dr. Ahmed '], 'sponsor_info': [{'name': 'Dr. Ahmed ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Dr.&const_search_last_name=Ahmed', 'is_not_last': False, 'is_not_first': False}]}, "The Devils' Advocate": {'timestamp': '8/12/2020 13:28:14', 'name': "The Devils' Advocate", 'description': "The Devils' Advocate is the student-run school newspaper, reporting on multiple categories, including current events, sports, arts, and more, of UHS and the world at-large. We believe that journalism has the power to make each reader’s life richer and fosters the vibrance of the UHS community. In pursuit of the truth and honoring journalistic integrity, the DA welcomes and encourages all voices to be represented in our paper. ", 'leaders': 'Jeanette Nguyen, Evan Carlo-Fowler, Zach Beischer', 'sponsor': "Ryan O'Donnell", 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1gjGWsrLkSdFSrdFoye1qMQ45b2EbZ1-U', 'email': '', 'index': 6, 'id': "the-devils'-advocate", 'leader_array': ['Jeanette Nguyen', 'Evan Carlo-Fowler', 'Zach Beischer'], 'leader_info': [{'name': 'Jeanette Nguyen', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jeanette&const_search_last_name=Nguyen', 'is_not_last': True}, {'name': 'Evan Carlo-Fowler', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Evan&const_search_last_name=Carlo-Fowler', 'is_not_last': True, 'is_not_first': True}, {'name': 'Zach Beischer', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Zach&const_search_last_name=Beischer', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ["Ryan O'Donnell"], 'sponsor_info': [{'name': "Ryan O'Donnell", 'link': "https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ryan&const_search_last_name=O'Donnell", 'is_not_last': False, 'is_not_first': False}]}, 'Rock History and Appreciation Club': {'timestamp': '8/12/2020 15:58:18', 'name': 'Rock History and Appreciation Club', 'description': "Not an affinity space.  It's a club for people to listen to, learn about, and enjoy rock music.", 'leaders': 'Maggie Carlson', 'sponsor': 'Sandeep Bhuta', 'meeting_time': 'Wednesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=17xBTZFUg-Qhg8vDSlV3zR-9Dv9Xq2wjQ', 'email': '', 'index': 7, 'id': 'rock-history-and-appreciation-club', 'leader_array': ['Maggie Carlson'], 'leader_info': [{'name': 'Maggie Carlson', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Maggie&const_search_last_name=Carlson', 'is_not_last': True}], 'sponsor_array': ['Sandeep Bhuta'], 'sponsor_info': [{'name': 'Sandeep Bhuta', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sandeep&const_search_last_name=Bhuta', 'is_not_last': False, 'is_not_first': False}]}, 'AAPI': {'timestamp': '8/12/2020 17:12:43', 'name': 'AAPI', 'description': "AAPI or Asian American/Pacific Islander is UHS's Asian affinity space. AAPI provides a safe space for AAPI students and faculty in the UHS community to  connect with one another and share their experiences. It is closed to those who identify as Asian, Asian American, and Pacific Islander, though some meetings will be open to all who have an interest in learning more about Asian culture. Meetings include discussions about heavier topics (ex. mental health, covid-inflicted racism, normalized cultural appropriation) as well as more light-hearted activities (ex. potlucks, movie screenings, field trips) to foster learning opportunities.", 'leaders': 'Jeanette Nguyen, Mason Villegas, Sarah Cheung', 'sponsor': 'Pierre Carmona, Joanne Sugiyama', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1SuaKY2cFu8qcFiYjDpjXy-rQrFUEoqOZ', 'email': '', 'index': 8, 'id': 'aapi', 'leader_array': ['Jeanette Nguyen', 'Mason Villegas', 'Sarah Cheung'], 'leader_info': [{'name': 'Jeanette Nguyen', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jeanette&const_search_last_name=Nguyen', 'is_not_last': True}, {'name': 'Mason Villegas', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mason&const_search_last_name=Villegas', 'is_not_last': True, 'is_not_first': True}, {'name': 'Sarah Cheung', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Cheung', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Pierre Carmona', 'Joanne Sugiyama'], 'sponsor_info': [{'name': 'Pierre Carmona', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Pierre&const_search_last_name=Carmona', 'is_not_last': True}, {'name': 'Joanne Sugiyama', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Joanne&const_search_last_name=Sugiyama', 'is_not_last': False, 'is_not_first': True}]}, 'Red Cross Club': {'timestamp': '8/13/2020 10:43:44', 'name': 'Red Cross Club', 'description': 'This is a club for anyone interested in community service and public health. Due to online school, we will be meeting over zoom to discuss COVID-19, public health issues, as well as discussing drives and other activities for the future. We want to provide a space for students interested in helping their community as well as being knowledgeable about public health inequality. ', 'leaders': 'Sydney Srivastava, Jane Shvartsman', 'sponsor': 'Corinne Limbach', 'meeting_time': 'Monday lunch', 'image': '', 'email': '', 'index': 9, 'id': 'red-cross-club', 'leader_array': ['Sydney Srivastava', 'Jane Shvartsman'], 'leader_info': [{'name': 'Sydney Srivastava', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sydney&const_search_last_name=Srivastava', 'is_not_last': True}, {'name': 'Jane Shvartsman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jane&const_search_last_name=Shvartsman', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Corinne Limbach'], 'sponsor_info': [{'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': False, 'is_not_first': False}]}, 'Men of Color Group': {'timestamp': '8/13/2020 19:39:52', 'name': 'Men of Color Group', 'description': 'This is an affinity group for men of color to talk about issues or attitudes that have been perpetuated in our respective communities.', 'leaders': 'Kai Martell, Luqmaan Shaikh', 'sponsor': 'Nate Lundy', 'meeting_time': 'Friday lunch', 'image': '', 'email': '', 'index': 10, 'id': 'men-of-color-group', 'leader_array': ['Kai Martell', 'Luqmaan Shaikh'], 'leader_info': [{'name': 'Kai Martell', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Kai&const_search_last_name=Martell', 'is_not_last': True}, {'name': 'Luqmaan Shaikh', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Luqmaan&const_search_last_name=Shaikh', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': False, 'is_not_first': False}]}, 'Dungeons and Dragons Club': {'timestamp': '8/14/2020 15:43:03', 'name': 'Dungeons and Dragons Club', 'description': 'A club for people to play Dungeons and Dragons.', 'leaders': 'Ella Barrett, Victoria Mann, Madeline Boyle', 'sponsor': 'Albert Boyle', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1CWJ-jp_qMol2H009SzD9pIqKlGv705Qt', 'email': '', 'index': 11, 'id': 'dungeons-and-dragons-club', 'leader_array': ['Ella Barrett', 'Victoria Mann', 'Madeline Boyle'], 'leader_info': [{'name': 'Ella Barrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ella&const_search_last_name=Barrett', 'is_not_last': True}, {'name': 'Victoria Mann', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Victoria&const_search_last_name=Mann', 'is_not_last': True, 'is_not_first': True}, {'name': 'Madeline Boyle', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Madeline&const_search_last_name=Boyle', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Albert Boyle'], 'sponsor_info': [{'name': 'Albert Boyle', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Albert&const_search_last_name=Boyle', 'is_not_last': False, 'is_not_first': False}]}, 'Riot ': {'timestamp': '8/14/2020 17:39:26', 'name': 'Riot ', 'description': "We are a Women of Color club/affinity space. We work to make all WOC at UHS feel comfortable in this community and to provide a space for the discussion of many, many related issues!  Although we are a closed affinity space, we frequently hold open meetings, or meetings in collaboration with other clubs like SWEAR, Men's group, Spectra, and more. ", 'leaders': 'Sami Lee, Maya Patel', 'sponsor': 'Alexandra Simmons, Tilda Kapuya (uncertain)', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1fk0NpBGB_oc4tfxS-lZ00EUqtrt-yKF5', 'email': '', 'index': 12, 'id': 'riot-', 'leader_array': ['Sami Lee', 'Maya Patel'], 'leader_info': [{'name': 'Sami Lee', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sami&const_search_last_name=Lee', 'is_not_last': True}, {'name': 'Maya Patel', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Maya&const_search_last_name=Patel', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Alexandra Simmons', 'Tilda Kapuya (uncertain)'], 'sponsor_info': [{'name': 'Alexandra Simmons', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alexandra&const_search_last_name=Simmons', 'is_not_last': True}, {'name': 'Tilda Kapuya (uncertain)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Tilda&const_search_last_name=Kapuya', 'is_not_last': False, 'is_not_first': True}]}, 'Understanding Whiteness': {'timestamp': '8/15/2020 16:32:30', 'name': 'Understanding Whiteness', 'description': 'Understanding Whiteness is a discussion space for students who identify as white. The space will be used to talk about and further understand whiteness and how that plays a role in our classrooms, clubs and other UHS spaces. We will focus on whiteness at UHS, in the Bay Area and in the world at large, and how we see whiteness appear in current events. This is a white affinity because we want to create a sustained space for the white members of the UHS community to talk about race. We will be working in partnership with the adult Understanding Whiteness group for some meetings, and hopefully with other affinity spaces as well. ', 'leaders': "Chloe Richmond ('21), Emmy Etlin ('21)", 'sponsor': 'Jen Kent', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=180Oon8EWDpXqOyGpv55HtYLs1V56-RIn', 'email': '', 'index': 13, 'id': 'understanding-whiteness', 'leader_array': ["Chloe Richmond ('21)", "Emmy Etlin ('21)"], 'leader_info': [{'name': "Chloe Richmond ('21)", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Chloe&const_search_last_name=Richmond', 'is_not_last': True}, {'name': "Emmy Etlin ('21)", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emmy&const_search_last_name=Etlin', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jen Kent'], 'sponsor_info': [{'name': 'Jen Kent', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jen&const_search_last_name=Kent', 'is_not_last': False, 'is_not_first': False}]}, 'Yearbook': {'timestamp': '8/16/2020 10:20:56', 'name': 'Yearbook', 'description': "Yearbook is a club focused on capturing the moments shared by the UHS community. This will be an open space to all who want to participate and learn/apply aspects of graphic design and photography! Despite the fact that we may not have the chance to be together for a while, we still want to create an aspect of our school that lets all of us participate with one another. We can't wait to see what comes up!", 'leaders': "Lauren Teotico '21, Pierce Hoenigman '21, Janavi Padala '21, Janine Navalta '22", 'sponsor': 'Elizabeth Faris', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1vVu2mj2nsjr33PrC2naYaE6ET7NwApu9', 'email': '', 'index': 14, 'id': 'yearbook', 'leader_array': ["Lauren Teotico '21", "Pierce Hoenigman '21", "Janavi Padala '21", "Janine Navalta '22"], 'leader_info': [{'name': "Lauren Teotico '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lauren&const_search_last_name=Teotico', 'is_not_last': True}, {'name': "Pierce Hoenigman '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Pierce&const_search_last_name=Hoenigman', 'is_not_last': True, 'is_not_first': True}, {'name': "Janavi Padala '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Janavi&const_search_last_name=Padala', 'is_not_last': True, 'is_not_first': True}, {'name': "Janine Navalta '22", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Janine&const_search_last_name=Navalta', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Elizabeth Faris'], 'sponsor_info': [{'name': 'Elizabeth Faris', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Faris', 'is_not_last': False, 'is_not_first': False}]}, 'Spectra': {'timestamp': '8/16/2020 17:51:25', 'name': 'Spectra', 'description': 'Spectra will serve as an affinity safe space space for LGBT+ students and faculty. In addition to providing an affinity space, we will hold open meetings and hold discussions to educate the broader UHS community about the issues our community faces.', 'leaders': 'Nico Brubaker, Ariane Vidal, Hannah Urisman', 'sponsor': 'Andrew Galatas', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=143xdpESH3A_Q6ZAKBN5BWszq2H7PQ9mm', 'email': '', 'index': 15, 'id': 'spectra', 'leader_array': ['Nico Brubaker', 'Ariane Vidal', 'Hannah Urisman'], 'leader_info': [{'name': 'Nico Brubaker', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nico&const_search_last_name=Brubaker', 'is_not_last': True}, {'name': 'Ariane Vidal', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=Vidal', 'is_not_last': True, 'is_not_first': True}, {'name': 'Hannah Urisman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hannah&const_search_last_name=Urisman', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Andrew Galatas'], 'sponsor_info': [{'name': 'Andrew Galatas', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Andrew&const_search_last_name=Galatas', 'is_not_last': False, 'is_not_first': False}]}, 'Family Matters Affinity Group': {'timestamp': '8/17/2020 11:08:53', 'name': 'Family Matters Affinity Group', 'description': 'Part of the UHS mission statement: "Together we work to build and sustain a community of diverse backgrounds, perspectives, and talents." We will create a safe space for people with diverse family structures (e.g. adopted, trans-racially adopted, single parent, divorced parents, blended households, etc.) to share experiences and support each other and enlarge our visibility in the UHS community. Our goal is to acknowledge our family differences and make them more visible in the community;  when we can see each other more clearly, our community becomes stronger.\n', 'leaders': 'Alex Perry, Lucas Perry', 'sponsor': 'Eric Johnson', 'meeting_time': 'Wednesday clubs/affinity', 'image': '', 'email': '', 'index': 19, 'id': 'family-matters-affinity-group', 'leader_array': ['Alex Perry', 'Lucas Perry'], 'leader_info': [{'name': 'Alex Perry', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alex&const_search_last_name=Perry', 'is_not_last': True}, {'name': 'Lucas Perry', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lucas&const_search_last_name=Perry', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Eric Johnson'], 'sponsor_info': [{'name': 'Eric Johnson', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Eric&const_search_last_name=Johnson', 'is_not_last': False, 'is_not_first': False}]}, 'Body Positive Club': {'timestamp': '8/17/2020 11:35:19', 'name': 'Body Positive Club', 'description': 'This club is focused on spreading body positivity and love in the UHS community and beyond. Throughout the year we will cover topics ranging from eating disorders to social media to the culture around bodies at UHS. The meetings are always open to everyone. ', 'leaders': 'Elizabeth Evers, Robbie Grisso, Athena Nooney', 'sponsor': 'Corinne Limbach', 'meeting_time': 'Thursday lunch', 'image': '', 'email': '', 'index': 20, 'id': 'body-positive-club', 'leader_array': ['Elizabeth Evers', 'Robbie Grisso', 'Athena Nooney'], 'leader_info': [{'name': 'Elizabeth Evers', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Evers', 'is_not_last': True}, {'name': 'Robbie Grisso', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Robbie&const_search_last_name=Grisso', 'is_not_last': True, 'is_not_first': True}, {'name': 'Athena Nooney', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Athena&const_search_last_name=Nooney', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Corinne Limbach'], 'sponsor_info': [{'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': False, 'is_not_first': False}]}, 'Jewish Club': {'timestamp': '8/17/2020 16:41:02', 'name': 'Jewish Club', 'description': 'Jewish Club welcomes all members of the UHS community to discuss different aspects of the Jewish identity. Together, we will celebrate holidays, discuss controversies in the Jewish community and exchange stories of different Jewish experiences. In the past, some of our most successful meetings have been about Jews and sports, Israel and Palestine, and Jewish comedy. We encourage you to come to our meetings, whether you identify as Jewish, Jew-ish or neither!', 'leaders': 'Emmy Etlin (‘21), Eve Andersen (‘21), Noah Mays-Smith (‘22), Jacob Neplokh (‘23)', 'sponsor': 'Carol Coles', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1dT7fV3YwhOCkmAwWK7cDspJG8giKp2nN', 'email': '', 'index': 21, 'id': 'jewish-club', 'leader_array': ['Emmy Etlin (‘21)', 'Eve Andersen (‘21)', 'Noah Mays-Smith (‘22)', 'Jacob Neplokh (‘23)'], 'leader_info': [{'name': 'Emmy Etlin (‘21)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emmy&const_search_last_name=Etlin', 'is_not_last': True}, {'name': 'Eve Andersen (‘21)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Eve&const_search_last_name=Andersen', 'is_not_last': True, 'is_not_first': True}, {'name': 'Noah Mays-Smith (‘22)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Noah&const_search_last_name=Mays-Smith', 'is_not_last': True, 'is_not_first': True}, {'name': 'Jacob Neplokh (‘23)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jacob&const_search_last_name=Neplokh', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Carol Coles'], 'sponsor_info': [{'name': 'Carol Coles', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Carol&const_search_last_name=Coles', 'is_not_last': False, 'is_not_first': False}]}, 'Interfaith': {'timestamp': '8/17/2020 19:13:08', 'name': 'Interfaith', 'description': 'Interfaith is a club for students and faculty to have open conversations about faith and spirituality. With UHS being a secular school, we recognize that it may be difficult to find safe spaces to discuss faith; therefore, we hope to provide such a space with our club. We would also like to emphasize that we are not an affinity group; anyone is welcome at our meetings, regardless of their religious affiliation or lack thereof. ', 'leaders': 'Ariane Vidal, Erica Cooper, Clarissa Dann', 'sponsor': 'Kate Garrett', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1ttXHVyJTOQ7wBtLrMUYHu1imjdGnWV3a', 'email': '', 'index': 22, 'id': 'interfaith', 'leader_array': ['Ariane Vidal', 'Erica Cooper', 'Clarissa Dann'], 'leader_info': [{'name': 'Ariane Vidal', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=Vidal', 'is_not_last': True}, {'name': 'Erica Cooper', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Erica&const_search_last_name=Cooper', 'is_not_last': True, 'is_not_first': True}, {'name': 'Clarissa Dann', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Clarissa&const_search_last_name=Dann', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Kate Garrett'], 'sponsor_info': [{'name': 'Kate Garrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Kate&const_search_last_name=Garrett', 'is_not_last': False, 'is_not_first': False}]}, 'Book Club': {'timestamp': '8/18/2020 8:45:13', 'name': 'Book Club', 'description': "For our club, we plan to read a book and discuss it and possibly discuss movies too. It will take a while to read the book or watch the movie so we won't meet consecutively.  \n\nWe invite everyone to come out. ", 'leaders': 'Jack Clancy', 'sponsor': 'Hayley Beale ', 'meeting_time': 'TBD', 'image': '', 'email': '', 'index': 23, 'id': 'book-club', 'leader_array': ['Jack Clancy'], 'leader_info': [{'name': 'Jack Clancy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jack&const_search_last_name=Clancy', 'is_not_last': True}], 'sponsor_array': ['Hayley Beale '], 'sponsor_info': [{'name': 'Hayley Beale ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hayley&const_search_last_name=Beale', 'is_not_last': False, 'is_not_first': False}]}, 'Financial Aid and Socio-Economic Status  (FASES)': {'timestamp': '8/19/2020 0:40:28', 'name': 'Financial Aid and Socio-Economic Status  (FASES)', 'description': 'FASES is a club focused on addressing and tackling issues of socio-economic status and wealth within our community and beyond. We hold both affinity meetings for students on financial aid and open meetings for all to attend.', 'leaders': 'Jasmine Gonzalez, Frank Wercinski, Chloe Richmond, Drew Phillips, Gaby Garcia', 'sponsor': 'Nate Lundy, Jenny Schneider', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1LzLOB0I_eCVo1O6cBKd03arznTpnXwff', 'email': '', 'index': 25, 'id': 'financial-aid-and-socio-economic-status--(fases)', 'leader_array': ['Jasmine Gonzalez', 'Frank Wercinski', 'Chloe Richmond', 'Drew Phillips', 'Gaby Garcia'], 'leader_info': [{'name': 'Jasmine Gonzalez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jasmine&const_search_last_name=Gonzalez', 'is_not_last': True}, {'name': 'Frank Wercinski', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Frank&const_search_last_name=Wercinski', 'is_not_last': True, 'is_not_first': True}, {'name': 'Chloe Richmond', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Chloe&const_search_last_name=Richmond', 'is_not_last': True, 'is_not_first': True}, {'name': 'Drew Phillips', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Drew&const_search_last_name=Phillips', 'is_not_last': True, 'is_not_first': True}, {'name': 'Gaby Garcia', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Gaby&const_search_last_name=Garcia', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy', 'Jenny Schneider'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': True}, {'name': 'Jenny Schneider', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jenny&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}]}, 'BioMed club': {'timestamp': '8/19/2020 11:09:47', 'name': 'BioMed club', 'description': "BioMed club is focusing on topics such as vaccine development, clinical trials, and health inequalities. We aim to have speakers every other month covering different topics and meetings in between speakers to debrief and learn about our next speaker. There's no need to come to every meeting; if you see a topic that interests you feel free to drop in!", 'leaders': 'Lucy Falzone, Meryl Sampson', 'sponsor': 'Emma Hartmann', 'meeting_time': 'Tuesday lunch', 'image': '', 'email': '', 'index': 27, 'id': 'biomed-club', 'leader_array': ['Lucy Falzone', 'Meryl Sampson'], 'leader_info': [{'name': 'Lucy Falzone', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lucy&const_search_last_name=Falzone', 'is_not_last': True}, {'name': 'Meryl Sampson', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Meryl&const_search_last_name=Sampson', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Emma Hartmann'], 'sponsor_info': [{'name': 'Emma Hartmann', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Emma&const_search_last_name=Hartmann', 'is_not_last': False, 'is_not_first': False}]}, 'UNICEF Club': {'timestamp': '8/19/2020 12:21:28', 'name': 'UNICEF Club', 'description': 'We are focused on fundraising, advocacy/raising awareness, community building, and volunteering locally. This is a club open to everyone and we would love new faces! ', 'leaders': 'Mirabel Haskin Fernald, Katie Crawford', 'sponsor': 'undecided- we will email Alexandra when we know. ', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1wyrKwmQ5qOBkhg59tobzl-5pL0wYR6BM', 'email': '', 'index': 28, 'id': 'unicef-club', 'leader_array': ['Mirabel Haskin Fernald', 'Katie Crawford'], 'leader_info': [{'name': 'Mirabel Haskin Fernald', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mirabel&const_search_last_name=Haskin', 'is_not_last': True}, {'name': 'Katie Crawford', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Katie&const_search_last_name=Crawford', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['undecided- we will email Alexandra when we know. '], 'sponsor_info': [{'name': 'undecided- we will email Alexandra when we know. ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=undecided-&const_search_last_name=we', 'is_not_last': False, 'is_not_first': False}]}, 'Science Olympiad': {'timestamp': '8/19/2020 13:43:08', 'name': 'Science Olympiad', 'description': 'A chill club to explore scientific topics not formally taught by UHS and a chance to pursue other scientific interests with your peers in a semi-competitive or fun and experimental environment. ', 'leaders': 'Christian Canete, Sarah Cheung, Ella Barrett', 'sponsor': 'Luke Probst, Ozzie Nevarez', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1biN1bF3j2qp61vNp1uCHLBlWNJNE2ShF', 'email': '', 'index': 29, 'id': 'science-olympiad', 'leader_array': ['Christian Canete', 'Sarah Cheung', 'Ella Barrett'], 'leader_info': [{'name': 'Christian Canete', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Christian&const_search_last_name=Canete', 'is_not_last': True}, {'name': 'Sarah Cheung', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Cheung', 'is_not_last': True, 'is_not_first': True}, {'name': 'Ella Barrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ella&const_search_last_name=Barrett', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Luke Probst', 'Ozzie Nevarez'], 'sponsor_info': [{'name': 'Luke Probst', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Luke&const_search_last_name=Probst', 'is_not_last': True}, {'name': 'Ozzie Nevarez', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ozzie&const_search_last_name=Nevarez', 'is_not_last': False, 'is_not_first': True}]}, "Men's Group": {'timestamp': '8/21/2020 9:34:15', 'name': "Men's Group", 'description': "Men's Group strives to be a space for men to examine, critique, and reflect on issues of masculinity, as well as a safe space for men to be open and vulnerable. We will have some meetings, closed to self-indentified males. ", 'leaders': 'Owen Myers (2021), Drew Phillips (2021), Frank Wercinski (2021), Luqmaan Shaikh (2021)', 'sponsor': 'Marcus Caimi', 'meeting_time': 'Tuesday lunch', 'image': '', 'email': '', 'index': 30, 'id': "men's-group", 'leader_array': ['Owen Myers (2021)', 'Drew Phillips (2021)', 'Frank Wercinski (2021)', 'Luqmaan Shaikh (2021)'], 'leader_info': [{'name': 'Owen Myers (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Owen&const_search_last_name=Myers', 'is_not_last': True}, {'name': 'Drew Phillips (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Drew&const_search_last_name=Phillips', 'is_not_last': True, 'is_not_first': True}, {'name': 'Frank Wercinski (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Frank&const_search_last_name=Wercinski', 'is_not_last': True, 'is_not_first': True}, {'name': 'Luqmaan Shaikh (2021)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Luqmaan&const_search_last_name=Shaikh', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Marcus Caimi'], 'sponsor_info': [{'name': 'Marcus Caimi', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Marcus&const_search_last_name=Caimi', 'is_not_last': False, 'is_not_first': False}]}, 'Disney Club': {'timestamp': '8/21/2020 12:26:01', 'name': 'Disney Club', 'description': "We plan on doing screenings of your favorite Disney and Pixar movies! We are always open to suggestions so if you have a childhood fav you'd like us to screen, let us know. Anyone who still feels like a child at heart is encouraged to come :) ", 'leaders': 'Katie Hartel, Sara Tagol', 'sponsor': 'Elizabeth Schaffernoth', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1X800rNe-dESui73xF6zMMm9WShH6Q2kx', 'email': '', 'index': 31, 'id': 'disney-club', 'leader_array': ['Katie Hartel', 'Sara Tagol'], 'leader_info': [{'name': 'Katie Hartel', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Katie&const_search_last_name=Hartel', 'is_not_last': True}, {'name': 'Sara Tagol', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sara&const_search_last_name=Tagol', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Elizabeth Schaffernoth'], 'sponsor_info': [{'name': 'Elizabeth Schaffernoth', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Elizabeth&const_search_last_name=Schaffernoth', 'is_not_last': False, 'is_not_first': False}]}, 'Satonics': {'timestamp': '8/21/2020 13:00:15', 'name': 'Satonics', 'description': 'This club is UHS’s a cappella group and is open to anyone who is accepted via an informal audition. We make music entirely with our voices and sing a variety of music, from pop songs to jazz arrangements, and perform at concerts and competitions. We will be holding auditions through Zoom next Friday (29th) and Saturday (30th), with more information to sign up in an email. We especially encourage underclassmen and those with lower voices to audition! Until further notice from the high school a cappella competition we participate in (Varsity Vocals ICHSA), our group will perform for school concerts through pre-recorded songs.', 'leaders': 'Sarah Cheung, Matthew Gin,, Madelyn Ocker', 'sponsor': 'Joel Chapman', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1r4zT6QBHRw4yNHs8Q_rkRac9gAjFByUu', 'email': '', 'index': 32, 'id': 'satonics', 'leader_array': ['Sarah Cheung', 'Matthew Gin,', 'Madelyn Ocker'], 'leader_info': [{'name': 'Sarah Cheung', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Sarah&const_search_last_name=Cheung', 'is_not_last': True}, {'name': 'Matthew Gin,', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Matthew&const_search_last_name=Gin,', 'is_not_last': True, 'is_not_first': True}, {'name': 'Madelyn Ocker', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Madelyn&const_search_last_name=Ocker', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Joel Chapman'], 'sponsor_info': [{'name': 'Joel Chapman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Joel&const_search_last_name=Chapman', 'is_not_last': False, 'is_not_first': False}]}, 'Multiracial Club': {'timestamp': '8/21/2020 14:14:48', 'name': 'Multiracial Club', 'description': 'An affinity space for students and faculty that self-identify as biracial or multiracial. ', 'leaders': "Arianna Schwartz ’22, Phia Black ’23, Owen Myers ’21, Amelie Scheil '21, Lauren Schneider '21", 'sponsor': 'Nate Lundy', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1iRw4xM3-Ss7EvGAItqS2jeVYPSppBvdv', 'email': '', 'index': 33, 'id': 'multiracial-club', 'leader_array': ['Arianna Schwartz ’22', 'Phia Black ’23', 'Owen Myers ’21', "Amelie Scheil '21", "Lauren Schneider '21"], 'leader_info': [{'name': 'Arianna Schwartz ’22', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Arianna&const_search_last_name=Schwartz', 'is_not_last': True}, {'name': 'Phia Black ’23', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Phia&const_search_last_name=Black', 'is_not_last': True, 'is_not_first': True}, {'name': 'Owen Myers ’21', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Owen&const_search_last_name=Myers', 'is_not_last': True, 'is_not_first': True}, {'name': "Amelie Scheil '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Amelie&const_search_last_name=Scheil', 'is_not_last': True, 'is_not_first': True}, {'name': "Lauren Schneider '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lauren&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Nate Lundy'], 'sponsor_info': [{'name': 'Nate Lundy', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Nate&const_search_last_name=Lundy', 'is_not_last': False, 'is_not_first': False}]}, 'Artivism Club': {'timestamp': '8/21/2020 14:27:02', 'name': 'Artivism Club', 'description': 'The purpose of Artivism club is to explore the intersection of art and activism, through art projects, fundraisers, and club meetings. We plan to collaborate with clubs such as BSU, Riot, and SWEAR in order to explore art as a vehicle for social justice. Previous projects include a mural for Summerbridge (featured in the hallway of Upper campus), poster-making sessions, and lunch workshops on color theory/design principles. Our meetings are open to everyone, regardless of identity or prior artistic experience! ', 'leaders': 'Amelie Scheil, Jiho Lee', 'sponsor': 'Jenifer Kent', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1UgyFO_nPxNFkkr_EXDUL6gY6fxzD9rwv', 'email': '', 'index': 34, 'id': 'artivism-club', 'leader_array': ['Amelie Scheil', 'Jiho Lee'], 'leader_info': [{'name': 'Amelie Scheil', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Amelie&const_search_last_name=Scheil', 'is_not_last': True}, {'name': 'Jiho Lee', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jiho&const_search_last_name=Lee', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Jenifer Kent'], 'sponsor_info': [{'name': 'Jenifer Kent', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Jenifer&const_search_last_name=Kent', 'is_not_last': False, 'is_not_first': False}]}, 'Girls Who Code': {'timestamp': '8/21/2020 14:37:40', 'name': 'Girls Who Code', 'description': "Girls Who Code is a national non-profit organization working to close the gender gap in technology. Our club educates, equips, and inspires girls with the computing skills they'll need to pursue 21st-century opportunities.", 'leaders': "Amelie Scheil '21, Isabella Hochschild '21, Alicia Lopez-Guerra '22", 'sponsor': 'Leah Dorazio', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1ilPU8lENicf97gsFnfbO56i5T9cqV57J', 'email': 'amelie.scheil_21@sfuhs.org', 'index': 35, 'id': 'girls-who-code', 'leader_array': ["Amelie Scheil '21", "Isabella Hochschild '21", "Alicia Lopez-Guerra '22"], 'leader_info': [{'name': "Amelie Scheil '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Amelie&const_search_last_name=Scheil', 'is_not_last': True}, {'name': "Isabella Hochschild '21", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Isabella&const_search_last_name=Hochschild', 'is_not_last': True, 'is_not_first': True}, {'name': "Alicia Lopez-Guerra '22", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Alicia&const_search_last_name=Lopez-Guerra', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Leah Dorazio'], 'sponsor_info': [{'name': 'Leah Dorazio', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Leah&const_search_last_name=Dorazio', 'is_not_last': False, 'is_not_first': False}]}, 'Hapa (half white half asian affinity group)': {'timestamp': '8/21/2020 15:27:11', 'name': 'Hapa (half white half asian affinity group)', 'description': 'Hapa is a term used to describe a person who is half asian and half white. This affinity group, with closed meetings, will delve into the complexity that arises with a dual identity. ', 'leaders': 'Anna Neumann-Loreck, Lauren Schneider', 'sponsor': 'Andrew Galatas ', 'meeting_time': 'Thursday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1Nv-_3OZIR3FI1Z4P0BGK_CRtBghmwvRt', 'email': 'lauren.schneider_21@sfuhs.org', 'index': 37, 'id': 'hapa-(half-white-half-asian-affinity-group)', 'leader_array': ['Anna Neumann-Loreck', 'Lauren Schneider'], 'leader_info': [{'name': 'Anna Neumann-Loreck', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Anna&const_search_last_name=Neumann-Loreck', 'is_not_last': True}, {'name': 'Lauren Schneider', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lauren&const_search_last_name=Schneider', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Andrew Galatas '], 'sponsor_info': [{'name': 'Andrew Galatas ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Andrew&const_search_last_name=Galatas', 'is_not_last': False, 'is_not_first': False}]}, 'Avatar: The Last Airbender Club': {'timestamp': '8/21/2020 16:02:38', 'name': 'Avatar: The Last Airbender Club', 'description': 'Our club welcomes fans of the Avatar universe, including Avatar: The Last Airbender and Legend of Korra. I think we can all agree that it is the best show ever written, so we decided to make a club to appreciate its brilliance. We will watch episodes, discuss opinions and themes, take fun "which bender am I" quizzes and appreciate the show and its excellence.', 'leaders': 'Ariane Vidal, Hannah Urisman', 'sponsor': 'Adrian Acu', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1M4wtD2PLLN4TN94RMQRujwIsQ9SGFh_V', 'email': 'hannah.urisman_22@sfuhs.org', 'index': 38, 'id': 'avatar:-the-last-airbender-club', 'leader_array': ['Ariane Vidal', 'Hannah Urisman'], 'leader_info': [{'name': 'Ariane Vidal', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=Vidal', 'is_not_last': True}, {'name': 'Hannah Urisman', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Hannah&const_search_last_name=Urisman', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Adrian Acu'], 'sponsor_info': [{'name': 'Adrian Acu', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Adrian&const_search_last_name=Acu', 'is_not_last': False, 'is_not_first': False}]}, 'Conservative Club': {'timestamp': '8/21/2020 16:58:57', 'name': 'Conservative Club', 'description': "UHS Conservative Club is a club dedicated to promoting substantive discussion of political ideas. We believe that when 80% of liberal students feel confident sharing their political views, but 80% of conservative students do not, real debate can never be achieved. To join, you don't need to hold any particular viewpoints on any issue, and you don't even need to be conservative (in fact, we welcome and value differing perspectives). All you need to believe is that UHS, and the United States as a whole, will be a better place if we allow open and honest debate and exchange of ideas, and that echo chambers aren't good for anyone. Our goal is to provide a forum for conservative thought that is mainstream in the United States, but not often represented at UHS.\n\nWe will meet every few weeks to discuss current events, the political climate on campus and in the country, or host a guest speaker.", 'leaders': 'Dan Huguenin, Tyler Sisitsky', 'sponsor': 'Kate Garrett', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1ZnMS1INYZDiydg5lmq5WPDAvAQpedMIi', 'email': 'dan.huguenin_21@sfuhs.org', 'index': 39, 'id': 'conservative-club', 'leader_array': ['Dan Huguenin', 'Tyler Sisitsky'], 'leader_info': [{'name': 'Dan Huguenin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Dan&const_search_last_name=Huguenin', 'is_not_last': True}, {'name': 'Tyler Sisitsky', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Tyler&const_search_last_name=Sisitsky', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Kate Garrett'], 'sponsor_info': [{'name': 'Kate Garrett', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Kate&const_search_last_name=Garrett', 'is_not_last': False, 'is_not_first': False}]}, 'White Folks Committed to Anti-Racism Affinity Space': {'timestamp': '8/21/2020 17:17:45', 'name': 'White Folks Committed to Anti-Racism Affinity Space', 'description': '“I can’t build externally what I haven’t built internally.”\nDr. Cornel West\n \n \nThis is an invitation for all folks who identify as white and are striving toward an identity of anti-racist. This is a space to gather and process the complexity of what it means to be white identifying human beings at this time with a focus on building a competent and firm foundation of anti-racism. This is a supportive and safe space. We will make mistakes. We will have all the best intentions and still have a negative impact. This is a space to learn and grow together, that our intentions may align with our actions, that we may shift to being influential as opposed to impactful. We will bring all our humanness to the table and hold space for all of it.\n ', 'leaders': "(we want but don't have yet!)", 'sponsor': 'Corinne Limbach, Lindsay Repko, Lisa Carroll', 'meeting_time': 'Tuesday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1LnaXI2SXVKV7XrUJj68h3vSKzChiIsow', 'email': 'lisa.carroll@sfuhs.org', 'index': 40, 'id': 'white-folks-committed-to-anti-racism-affinity-space', 'leader_array': ["(we want but don't have yet!)"], 'leader_info': [{'name': "(we want but don't have yet!)", 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=(we&const_search_last_name=want', 'is_not_last': True}], 'sponsor_array': ['Corinne Limbach', 'Lindsay Repko', 'Lisa Carroll'], 'sponsor_info': [{'name': 'Corinne Limbach', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Corinne&const_search_last_name=Limbach', 'is_not_last': True}, {'name': 'Lindsay Repko', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lindsay&const_search_last_name=Repko', 'is_not_last': True, 'is_not_first': True}, {'name': 'Lisa Carroll', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lisa&const_search_last_name=Carroll', 'is_not_last': False, 'is_not_first': True}]}, 'Mental Health Coalition': {'timestamp': '8/21/2020 17:27:13', 'name': 'Mental Health Coalition', 'description': 'Mental Health Advocacy', 'leaders': 'TBD: currently in process', 'sponsor': 'Lindsay Repko (may add others)', 'meeting_time': 'Tuesday lunch', 'image': '', 'email': 'lindsay.repko@sfuhs.org', 'index': 41, 'id': 'mental-health-coalition', 'leader_array': ['TBD: currently in process'], 'leader_info': [{'name': 'TBD: currently in process', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=TBD:&const_search_last_name=currently', 'is_not_last': True}], 'sponsor_array': ['Lindsay Repko (may add others)'], 'sponsor_info': [{'name': 'Lindsay Repko (may add others)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Lindsay&const_search_last_name=Repko', 'is_not_last': False, 'is_not_first': False}]}, 'HIstory of History of History of History of Surf Club Club Club Club Club': {'timestamp': '8/22/2020 17:44:33', 'name': 'HIstory of History of History of History of Surf Club Club Club Club Club', 'description': 'This club will tell the historic odyssey of surf club at UHS. It will then delve deeper into topics of surf history and culture. From there, we will approach a variety of modern issues such as global warming, environmental preservation and sustainability, and more.', 'leaders': 'Ren Zanze (President), Mica (President)  ', 'sponsor': 'Scott Laughlin', 'meeting_time': 'Friday lunch', 'image': '', 'email': 'ren.zanze_21@sfuhs.org', 'index': 42, 'id': 'history-of-history-of-history-of-history-of-surf-club-club-club-club-club', 'leader_array': ['Ren Zanze (President)', 'Mica (President)  '], 'leader_info': [{'name': 'Ren Zanze (President)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ren&const_search_last_name=Zanze', 'is_not_last': True}, {'name': 'Mica (President)  ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mica&const_search_last_name=(President)', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Scott Laughlin'], 'sponsor_info': [{'name': 'Scott Laughlin', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Scott&const_search_last_name=Laughlin', 'is_not_last': False, 'is_not_first': False}]}, "Women's Health Club": {'timestamp': '8/22/2020 21:18:27', 'name': "Women's Health Club", 'description': 'The mission of our club is to spread awareness about how common sexual assault/rape is in our society and educate students through stories, guest speakers, social media, documentaries, and other sources. We hope to become advocates for change by working with organizations in San Francisco as well as providing a safe space for UHS students to learn and talk about these issues. This club will have a few closed meetings but will mostly be open for everyone.', 'leaders': 'Ria Dhillon, Malia House', 'sponsor': 'Barbara Holler ', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1e74BJbPfHCyirNbM4MExRl3h_7QralGf', 'email': 'malia.house_22@sfuhs.org', 'index': 43, 'id': "women's-health-club", 'leader_array': ['Ria Dhillon', 'Malia House'], 'leader_info': [{'name': 'Ria Dhillon', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ria&const_search_last_name=Dhillon', 'is_not_last': True}, {'name': 'Malia House', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Malia&const_search_last_name=House', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Barbara Holler '], 'sponsor_info': [{'name': 'Barbara Holler ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Barbara&const_search_last_name=Holler', 'is_not_last': False, 'is_not_first': False}]}, 'The Radio Broadcast Club': {'timestamp': '8/25/2020 13:09:08', 'name': 'The Radio Broadcast Club', 'description': 'In this club we will listen to old radio theater broadcasts as well as rewrite them or recreate them! As a form of online drama!', 'leaders': 'Harper Clementz (10th) , Ariane (11th)', 'sponsor': 'Ryan O’Donnell ', 'meeting_time': 'Friday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1NRLA2QMsogjPDLYodEcZylLaSaCA6CnQ', 'email': 'harper.clementz_23@sfuhs.org', 'index': 44, 'id': 'the-radio-broadcast-club', 'leader_array': ['Harper Clementz (10th) ', 'Ariane (11th)'], 'leader_info': [{'name': 'Harper Clementz (10th) ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Harper&const_search_last_name=Clementz', 'is_not_last': True}, {'name': 'Ariane (11th)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ariane&const_search_last_name=(11th)', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Ryan O’Donnell '], 'sponsor_info': [{'name': 'Ryan O’Donnell ', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Ryan&const_search_last_name=O’Donnell', 'is_not_last': False, 'is_not_first': False}]}, 'UHS Business Club': {'timestamp': '8/25/2020 14:49:21', 'name': 'UHS Business Club', 'description': 'Selling short; econometrics; balance sheets...what does this all mean? The UHS Business Club provides opportunities for its members to learn about the inner workings of the business world. Through activities such as case studies, ethical debates, and projects, we will introduce our club members to careers in the business sector, current events in the finance field, and experimentation with basic business transactions. With introductions to management, marketing and investing games, get ready for some fun dives into the business world. We are open to all who would like to join!', 'leaders': 'Mericel Tao, Caroline Hall-Sherr', 'sponsor': 'David Roth', 'meeting_time': 'Monday lunch', 'image': 'https://drive.google.com/uc?export=view&id=1KLk4U3iXsTpiP4IfoYO1QuLHydSTBmPi', 'email': 'mericel.tao_22@sfuhs.org', 'index': 45, 'id': 'uhs-business-club', 'leader_array': ['Mericel Tao', 'Caroline Hall-Sherr'], 'leader_info': [{'name': 'Mericel Tao', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mericel&const_search_last_name=Tao', 'is_not_last': True}, {'name': 'Caroline Hall-Sherr', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Caroline&const_search_last_name=Hall-Sherr', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['David Roth'], 'sponsor_info': [{'name': 'David Roth', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=David&const_search_last_name=Roth', 'is_not_last': False, 'is_not_first': False}]}, 'UHS SWENext Club': {'timestamp': '8/25/2020 15:04:25', 'name': 'UHS SWENext Club', 'description': 'From bridges to spaceships, computers to cars, engineers are the force behind many of the objects we interact with. The Society of Women Engineers (SWE) seeks to increase the representation of women in the engineering field and revamp the dynamics of the engineering workforce. Our UHS SWENext Club combines group activities, discussions about current events in engineering, and lessons about engineering to expand on SWE’s mission of empowering women engineers. Most of the activity and learning based meetings will be open to non-male identifying students, but meetings discussing current events will be open to all!', 'leaders': 'Danielle Cuthbert, Mericel Tao', 'sponsor': 'Megan Storti', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=121_Q-W2qgbuep_Bl5Rms8v8Uh2DHuze2', 'email': 'danielle.cuthbert_22@sfuhs.org', 'index': 46, 'id': 'uhs-swenext-club', 'leader_array': ['Danielle Cuthbert', 'Mericel Tao'], 'leader_info': [{'name': 'Danielle Cuthbert', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Danielle&const_search_last_name=Cuthbert', 'is_not_last': True}, {'name': 'Mericel Tao', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Mericel&const_search_last_name=Tao', 'is_not_last': False, 'is_not_first': True}], 'sponsor_array': ['Megan Storti'], 'sponsor_info': [{'name': 'Megan Storti', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Megan&const_search_last_name=Storti', 'is_not_last': False, 'is_not_first': False}]}, 'Investment Club': {'timestamp': '8/27/2020 12:37:45', 'name': 'Investment Club', 'description': 'This is a club open to all students with an interest in investing and the financial world. No experience is required, we’ll learn together how to track a portfolio and research stocks. The club will have various speakers with years of experience in finance and will be an interactive space for students to learn more about investing.', 'leaders': 'Owen Flanagan', 'sponsor': 'Michael Novak (UHS Chief Financial Operations Officer)', 'meeting_time': 'Wednesday clubs/affinity', 'image': 'https://drive.google.com/uc?export=view&id=1gzLIHou05Ff8ukISzaEUHX3q6aEHHPCF', 'email': 'owen.flanagan_21@sfuhs.org', 'index': 47, 'id': 'investment-club', 'leader_array': ['Owen Flanagan'], 'leader_info': [{'name': 'Owen Flanagan', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Owen&const_search_last_name=Flanagan', 'is_not_last': True}], 'sponsor_array': ['Michael Novak (UHS Chief Financial Operations Officer)'], 'sponsor_info': [{'name': 'Michael Novak (UHS Chief Financial Operations Officer)', 'link': 'https://www.sfuhs.org/student/community-directory?utf8=%E2%9C%93&const_search_role_ids=6%2C2%2C1&const_search_first_name=Michael&const_search_last_name=Novak', 'is_not_last': False, 'is_not_first': False}]}};
            $('#search').keyup(function(){
                console.log("searching for "+$(this).val())
                search_text($(this).val());
            });
            $('#show-affinity-groups').click(function(){
                $('#cards').show();
                $('#search-div').show();
                $('.card').hide();
                $('#carousel').hide();
                $('.specific-club').hide();
                $('.card-columns .affinity-group').each(function(){
                    $(this).show()
                });
                $('.nav-link').each(function(){
                    $(this).removeClass("active")
                });
                $(this).addClass("active");
            });
            $('#show-clubs').click(function(){
                $('#cards').show();
                $('#search-div').show();
                $('.card').hide();
                $('#carousel').hide();
                $('.specific-club').hide();
                $('.card-columns .club').each(function(){
                    $(this).show()
                });
                $('.nav-link').each(function(){
                    $(this).removeClass("active")
                });
                $(this).addClass("active");
            });
            $('#show-all').click(function(){
                $('#cards').show();
                $('#search-div').show();
                $('.card').show();
                $('#carousel').hide();
                $('.specific-club').hide();
                $('.nav-link').each(function(){
                    $(this).removeClass("active")
                });
                $(this).addClass("active");
            });
            $('#show-carousel').click(function(){
                $('#cards').hide();
                $('#search-div').hide();
                $('.specific-club').hide();
                $('.nav-link').each(function(){
                    $(this).removeClass("active")
                });
                $(this).addClass("active");
                $('#carousel').show();
            });
            $('.specific-club-link').click(function() {
                $('#carousel').hide();
                // $('#cards').show();
                // $('.card').hide();
                $('.nav-link').each(function(){
                     $(this).removeClass("active")
                });
                // console.log("searching for "+$(this).text())
                // search_text($(this).text());
                $('#'+$(this).attr("id").split("-link")[0]).show();
            })
        });
    function search_text(value){
        $('.card-columns .card').each(function(){
            var found = 'false';
            $(this).find('.card-body .card-title').each(function(){
                if($(this).text().toLowerCase().indexOf(value.toLowerCase()) >= 0)
                {
                    found = 'true';
                }
            });
            if(found == 'true'){
                $(this).show()
            }
            else {
                $(this).hide();
            }
        });
    };
    function shuffleArray(array) {
        let shuffled = array.map((a) => ({sort: Math.random(), value: a})).sort((a, b) => a.sort - b.sort).map((a) => a.value)
        return shuffled;
    };
</script>
</body>

</html>