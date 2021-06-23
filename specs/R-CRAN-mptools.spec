%global __brp_check_rpaths %{nil}
%global packname  mptools
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          RAMAS Metapop Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-viridis 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-animation 
Requires:         R-lattice 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-viridis 

%description
'RAMAS Metapop' <https://www.ramas.com/ramas.htm#metapop> is a popular
software package for performing spatially-explicit population viability
analysis. It is primarily GUI-driven, but can benefit from integration
into an R workflow, wherein model results can be subjected to further
analysis. 'RAMAS Metapop' stores metapopulation model parameter settings
and population dynamics simulation results in plain text files (.mp
files). This package facilitates access, summary and visualisation of
'RAMAS Metapop 5' outputs in order to better integrate 'RAMAS' analyses
into an R workflow.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_001.tif
%doc %{rlibdir}/%{packname}/example_002.tif
%doc %{rlibdir}/%{packname}/example_003.tif
%doc %{rlibdir}/%{packname}/example_004.tif
%doc %{rlibdir}/%{packname}/example_005.tif
%doc %{rlibdir}/%{packname}/example_006.tif
%doc %{rlibdir}/%{packname}/example_007.tif
%doc %{rlibdir}/%{packname}/example_008.tif
%doc %{rlibdir}/%{packname}/example_009.tif
%doc %{rlibdir}/%{packname}/example_010.tif
%doc %{rlibdir}/%{packname}/example_011.tif
%doc %{rlibdir}/%{packname}/example_012.tif
%doc %{rlibdir}/%{packname}/example_013.tif
%doc %{rlibdir}/%{packname}/example_014.tif
%doc %{rlibdir}/%{packname}/example_015.tif
%doc %{rlibdir}/%{packname}/example_016.tif
%doc %{rlibdir}/%{packname}/example_017.tif
%doc %{rlibdir}/%{packname}/example_018.tif
%doc %{rlibdir}/%{packname}/example_019.tif
%doc %{rlibdir}/%{packname}/example_020.tif
%doc %{rlibdir}/%{packname}/example_021.tif
%doc %{rlibdir}/%{packname}/example_022.tif
%doc %{rlibdir}/%{packname}/example_023.tif
%doc %{rlibdir}/%{packname}/example_024.tif
%doc %{rlibdir}/%{packname}/example_025.tif
%doc %{rlibdir}/%{packname}/example_026.tif
%doc %{rlibdir}/%{packname}/example_027.tif
%doc %{rlibdir}/%{packname}/example_028.tif
%doc %{rlibdir}/%{packname}/example_029.tif
%doc %{rlibdir}/%{packname}/example_030.tif
%doc %{rlibdir}/%{packname}/example_031.tif
%doc %{rlibdir}/%{packname}/example_032.tif
%doc %{rlibdir}/%{packname}/example_033.tif
%doc %{rlibdir}/%{packname}/example_034.tif
%doc %{rlibdir}/%{packname}/example_035.tif
%doc %{rlibdir}/%{packname}/example_036.tif
%doc %{rlibdir}/%{packname}/example_037.tif
%doc %{rlibdir}/%{packname}/example_038.tif
%doc %{rlibdir}/%{packname}/example_039.tif
%doc %{rlibdir}/%{packname}/example_040.tif
%doc %{rlibdir}/%{packname}/example_041.tif
%doc %{rlibdir}/%{packname}/example_042.tif
%doc %{rlibdir}/%{packname}/example_043.tif
%doc %{rlibdir}/%{packname}/example_044.tif
%doc %{rlibdir}/%{packname}/example_045.tif
%doc %{rlibdir}/%{packname}/example_046.tif
%doc %{rlibdir}/%{packname}/example_047.tif
%doc %{rlibdir}/%{packname}/example_048.tif
%doc %{rlibdir}/%{packname}/example_049.tif
%doc %{rlibdir}/%{packname}/example_050.tif
%doc %{rlibdir}/%{packname}/example_051.tif
%doc %{rlibdir}/%{packname}/example_052.tif
%doc %{rlibdir}/%{packname}/example_053.tif
%doc %{rlibdir}/%{packname}/example_054.tif
%doc %{rlibdir}/%{packname}/example_055.tif
%doc %{rlibdir}/%{packname}/example_056.tif
%doc %{rlibdir}/%{packname}/example_057.tif
%doc %{rlibdir}/%{packname}/example_058.tif
%doc %{rlibdir}/%{packname}/example_059.tif
%doc %{rlibdir}/%{packname}/example_060.tif
%doc %{rlibdir}/%{packname}/example_061.tif
%doc %{rlibdir}/%{packname}/example_062.tif
%doc %{rlibdir}/%{packname}/example_063.tif
%doc %{rlibdir}/%{packname}/example_064.tif
%doc %{rlibdir}/%{packname}/example_065.tif
%doc %{rlibdir}/%{packname}/example_066.tif
%doc %{rlibdir}/%{packname}/example_067.tif
%doc %{rlibdir}/%{packname}/example_068.tif
%doc %{rlibdir}/%{packname}/example_069.tif
%doc %{rlibdir}/%{packname}/example_070.tif
%doc %{rlibdir}/%{packname}/example_071.tif
%doc %{rlibdir}/%{packname}/example_072.tif
%doc %{rlibdir}/%{packname}/example_073.tif
%doc %{rlibdir}/%{packname}/example_074.tif
%doc %{rlibdir}/%{packname}/example_075.tif
%doc %{rlibdir}/%{packname}/example_076.tif
%doc %{rlibdir}/%{packname}/example_077.tif
%doc %{rlibdir}/%{packname}/example_078.tif
%doc %{rlibdir}/%{packname}/example_079.tif
%doc %{rlibdir}/%{packname}/example_080.tif
%doc %{rlibdir}/%{packname}/example_081.tif
%doc %{rlibdir}/%{packname}/example_082.tif
%doc %{rlibdir}/%{packname}/example_083.tif
%doc %{rlibdir}/%{packname}/example_084.tif
%doc %{rlibdir}/%{packname}/example_085.tif
%doc %{rlibdir}/%{packname}/example_086.tif
%doc %{rlibdir}/%{packname}/example_087.tif
%doc %{rlibdir}/%{packname}/example_088.tif
%doc %{rlibdir}/%{packname}/example_089.tif
%doc %{rlibdir}/%{packname}/example_090.tif
%doc %{rlibdir}/%{packname}/example_091.tif
%doc %{rlibdir}/%{packname}/example_092.tif
%doc %{rlibdir}/%{packname}/example_093.tif
%doc %{rlibdir}/%{packname}/example_094.tif
%doc %{rlibdir}/%{packname}/example_095.tif
%doc %{rlibdir}/%{packname}/example_096.tif
%doc %{rlibdir}/%{packname}/example_097.tif
%doc %{rlibdir}/%{packname}/example_098.tif
%doc %{rlibdir}/%{packname}/example_099.tif
%doc %{rlibdir}/%{packname}/example_100.tif
%doc %{rlibdir}/%{packname}/example.mp
%doc %{rlibdir}/%{packname}/example1.kch
%doc %{rlibdir}/%{packname}/example10.kch
%doc %{rlibdir}/%{packname}/example100.kch
%doc %{rlibdir}/%{packname}/example101.kch
%doc %{rlibdir}/%{packname}/example102.kch
%doc %{rlibdir}/%{packname}/example103.kch
%doc %{rlibdir}/%{packname}/example104.kch
%doc %{rlibdir}/%{packname}/example105.kch
%doc %{rlibdir}/%{packname}/example106.kch
%doc %{rlibdir}/%{packname}/example107.kch
%doc %{rlibdir}/%{packname}/example108.kch
%doc %{rlibdir}/%{packname}/example109.kch
%doc %{rlibdir}/%{packname}/example11.kch
%doc %{rlibdir}/%{packname}/example110.kch
%doc %{rlibdir}/%{packname}/example111.kch
%doc %{rlibdir}/%{packname}/example112.kch
%doc %{rlibdir}/%{packname}/example113.kch
%doc %{rlibdir}/%{packname}/example114.kch
%doc %{rlibdir}/%{packname}/example115.kch
%doc %{rlibdir}/%{packname}/example116.kch
%doc %{rlibdir}/%{packname}/example117.kch
%doc %{rlibdir}/%{packname}/example118.kch
%doc %{rlibdir}/%{packname}/example119.kch
%doc %{rlibdir}/%{packname}/example12.kch
%doc %{rlibdir}/%{packname}/example120.kch
%doc %{rlibdir}/%{packname}/example121.kch
%doc %{rlibdir}/%{packname}/example122.kch
%doc %{rlibdir}/%{packname}/example123.kch
%doc %{rlibdir}/%{packname}/example124.kch
%doc %{rlibdir}/%{packname}/example125.kch
%doc %{rlibdir}/%{packname}/example126.kch
%doc %{rlibdir}/%{packname}/example127.kch
%doc %{rlibdir}/%{packname}/example128.kch
%doc %{rlibdir}/%{packname}/example129.kch
%doc %{rlibdir}/%{packname}/example13.kch
%doc %{rlibdir}/%{packname}/example130.kch
%doc %{rlibdir}/%{packname}/example131.kch
%doc %{rlibdir}/%{packname}/example132.kch
%doc %{rlibdir}/%{packname}/example133.kch
%doc %{rlibdir}/%{packname}/example134.kch
%doc %{rlibdir}/%{packname}/example135.kch
%doc %{rlibdir}/%{packname}/example136.kch
%doc %{rlibdir}/%{packname}/example137.kch
%doc %{rlibdir}/%{packname}/example138.kch
%doc %{rlibdir}/%{packname}/example139.kch
%doc %{rlibdir}/%{packname}/example14.kch
%doc %{rlibdir}/%{packname}/example140.kch
%doc %{rlibdir}/%{packname}/example141.kch
%doc %{rlibdir}/%{packname}/example142.kch
%doc %{rlibdir}/%{packname}/example143.kch
%doc %{rlibdir}/%{packname}/example144.kch
%doc %{rlibdir}/%{packname}/example145.kch
%doc %{rlibdir}/%{packname}/example146.kch
%doc %{rlibdir}/%{packname}/example147.kch
%doc %{rlibdir}/%{packname}/example148.kch
%doc %{rlibdir}/%{packname}/example149.kch
%doc %{rlibdir}/%{packname}/example15.kch
%doc %{rlibdir}/%{packname}/example150.kch
%doc %{rlibdir}/%{packname}/example151.kch
%doc %{rlibdir}/%{packname}/example152.kch
%doc %{rlibdir}/%{packname}/example153.kch
%doc %{rlibdir}/%{packname}/example154.kch
%doc %{rlibdir}/%{packname}/example155.kch
%doc %{rlibdir}/%{packname}/example156.kch
%doc %{rlibdir}/%{packname}/example157.kch
%doc %{rlibdir}/%{packname}/example158.kch
%doc %{rlibdir}/%{packname}/example159.kch
%doc %{rlibdir}/%{packname}/example16.kch
%doc %{rlibdir}/%{packname}/example160.kch
%doc %{rlibdir}/%{packname}/example161.kch
%doc %{rlibdir}/%{packname}/example162.kch
%doc %{rlibdir}/%{packname}/example163.kch
%doc %{rlibdir}/%{packname}/example164.kch
%doc %{rlibdir}/%{packname}/example165.kch
%doc %{rlibdir}/%{packname}/example166.kch
%doc %{rlibdir}/%{packname}/example167.kch
%doc %{rlibdir}/%{packname}/example168.kch
%doc %{rlibdir}/%{packname}/example169.kch
%doc %{rlibdir}/%{packname}/example17.kch
%doc %{rlibdir}/%{packname}/example170.kch
%doc %{rlibdir}/%{packname}/example171.kch
%doc %{rlibdir}/%{packname}/example172.kch
%doc %{rlibdir}/%{packname}/example173.kch
%doc %{rlibdir}/%{packname}/example174.kch
%doc %{rlibdir}/%{packname}/example175.kch
%doc %{rlibdir}/%{packname}/example176.kch
%doc %{rlibdir}/%{packname}/example177.kch
%doc %{rlibdir}/%{packname}/example178.kch
%doc %{rlibdir}/%{packname}/example179.kch
%doc %{rlibdir}/%{packname}/example18.kch
%doc %{rlibdir}/%{packname}/example180.kch
%doc %{rlibdir}/%{packname}/example181.kch
%doc %{rlibdir}/%{packname}/example182.kch
%doc %{rlibdir}/%{packname}/example183.kch
%doc %{rlibdir}/%{packname}/example184.kch
%doc %{rlibdir}/%{packname}/example185.kch
%doc %{rlibdir}/%{packname}/example186.kch
%doc %{rlibdir}/%{packname}/example187.kch
%doc %{rlibdir}/%{packname}/example188.kch
%doc %{rlibdir}/%{packname}/example189.kch
%doc %{rlibdir}/%{packname}/example19.kch
%doc %{rlibdir}/%{packname}/example190.kch
%doc %{rlibdir}/%{packname}/example191.kch
%doc %{rlibdir}/%{packname}/example192.kch
%doc %{rlibdir}/%{packname}/example193.kch
%doc %{rlibdir}/%{packname}/example194.kch
%doc %{rlibdir}/%{packname}/example195.kch
%doc %{rlibdir}/%{packname}/example196.kch
%doc %{rlibdir}/%{packname}/example197.kch
%doc %{rlibdir}/%{packname}/example198.kch
%doc %{rlibdir}/%{packname}/example199.kch
%doc %{rlibdir}/%{packname}/example2.kch
%doc %{rlibdir}/%{packname}/example20.kch
%doc %{rlibdir}/%{packname}/example200.kch
%doc %{rlibdir}/%{packname}/example201.kch
%doc %{rlibdir}/%{packname}/example202.kch
%doc %{rlibdir}/%{packname}/example203.kch
%doc %{rlibdir}/%{packname}/example204.kch
%doc %{rlibdir}/%{packname}/example205.kch
%doc %{rlibdir}/%{packname}/example206.kch
%doc %{rlibdir}/%{packname}/example207.kch
%doc %{rlibdir}/%{packname}/example208.kch
%doc %{rlibdir}/%{packname}/example209.kch
%doc %{rlibdir}/%{packname}/example21.kch
%doc %{rlibdir}/%{packname}/example210.kch
%doc %{rlibdir}/%{packname}/example211.kch
%doc %{rlibdir}/%{packname}/example212.kch
%doc %{rlibdir}/%{packname}/example213.kch
%doc %{rlibdir}/%{packname}/example214.kch
%doc %{rlibdir}/%{packname}/example215.kch
%doc %{rlibdir}/%{packname}/example216.kch
%doc %{rlibdir}/%{packname}/example217.kch
%doc %{rlibdir}/%{packname}/example218.kch
%doc %{rlibdir}/%{packname}/example219.kch
%doc %{rlibdir}/%{packname}/example22.kch
%doc %{rlibdir}/%{packname}/example220.kch
%doc %{rlibdir}/%{packname}/example221.kch
%doc %{rlibdir}/%{packname}/example222.kch
%doc %{rlibdir}/%{packname}/example223.kch
%doc %{rlibdir}/%{packname}/example224.kch
%doc %{rlibdir}/%{packname}/example225.kch
%doc %{rlibdir}/%{packname}/example226.kch
%doc %{rlibdir}/%{packname}/example227.kch
%doc %{rlibdir}/%{packname}/example228.kch
%doc %{rlibdir}/%{packname}/example229.kch
%doc %{rlibdir}/%{packname}/example23.kch
%doc %{rlibdir}/%{packname}/example230.kch
%doc %{rlibdir}/%{packname}/example231.kch
%doc %{rlibdir}/%{packname}/example232.kch
%doc %{rlibdir}/%{packname}/example233.kch
%doc %{rlibdir}/%{packname}/example234.kch
%doc %{rlibdir}/%{packname}/example235.kch
%doc %{rlibdir}/%{packname}/example236.kch
%doc %{rlibdir}/%{packname}/example237.kch
%doc %{rlibdir}/%{packname}/example238.kch
%doc %{rlibdir}/%{packname}/example239.kch
%doc %{rlibdir}/%{packname}/example24.kch
%doc %{rlibdir}/%{packname}/example240.kch
%doc %{rlibdir}/%{packname}/example241.kch
%doc %{rlibdir}/%{packname}/example242.kch
%doc %{rlibdir}/%{packname}/example243.kch
%doc %{rlibdir}/%{packname}/example244.kch
%doc %{rlibdir}/%{packname}/example245.kch
%doc %{rlibdir}/%{packname}/example246.kch
%doc %{rlibdir}/%{packname}/example247.kch
%doc %{rlibdir}/%{packname}/example248.kch
%doc %{rlibdir}/%{packname}/example249.kch
%doc %{rlibdir}/%{packname}/example25.kch
%doc %{rlibdir}/%{packname}/example250.kch
%doc %{rlibdir}/%{packname}/example251.kch
%doc %{rlibdir}/%{packname}/example252.kch
%doc %{rlibdir}/%{packname}/example253.kch
%doc %{rlibdir}/%{packname}/example254.kch
%doc %{rlibdir}/%{packname}/example255.kch
%doc %{rlibdir}/%{packname}/example256.kch
%doc %{rlibdir}/%{packname}/example257.kch
%doc %{rlibdir}/%{packname}/example258.kch
%doc %{rlibdir}/%{packname}/example259.kch
%doc %{rlibdir}/%{packname}/example26.kch
%doc %{rlibdir}/%{packname}/example260.kch
%doc %{rlibdir}/%{packname}/example261.kch
%doc %{rlibdir}/%{packname}/example262.kch
%doc %{rlibdir}/%{packname}/example263.kch
%doc %{rlibdir}/%{packname}/example27.kch
%doc %{rlibdir}/%{packname}/example28.kch
%doc %{rlibdir}/%{packname}/example29.kch
%doc %{rlibdir}/%{packname}/example3.kch
%doc %{rlibdir}/%{packname}/example30.kch
%doc %{rlibdir}/%{packname}/example31.kch
%doc %{rlibdir}/%{packname}/example32.kch
%doc %{rlibdir}/%{packname}/example33.kch
%doc %{rlibdir}/%{packname}/example34.kch
%doc %{rlibdir}/%{packname}/example35.kch
%doc %{rlibdir}/%{packname}/example36.kch
%doc %{rlibdir}/%{packname}/example37.kch
%doc %{rlibdir}/%{packname}/example38.kch
%doc %{rlibdir}/%{packname}/example39.kch
%doc %{rlibdir}/%{packname}/example4.kch
%doc %{rlibdir}/%{packname}/example40.kch
%doc %{rlibdir}/%{packname}/example41.kch
%doc %{rlibdir}/%{packname}/example42.kch
%doc %{rlibdir}/%{packname}/example43.kch
%doc %{rlibdir}/%{packname}/example44.kch
%doc %{rlibdir}/%{packname}/example45.kch
%doc %{rlibdir}/%{packname}/example46.kch
%doc %{rlibdir}/%{packname}/example47.kch
%doc %{rlibdir}/%{packname}/example48.kch
%doc %{rlibdir}/%{packname}/example49.kch
%doc %{rlibdir}/%{packname}/example5.kch
%doc %{rlibdir}/%{packname}/example50.kch
%doc %{rlibdir}/%{packname}/example51.kch
%doc %{rlibdir}/%{packname}/example52.kch
%doc %{rlibdir}/%{packname}/example53.kch
%doc %{rlibdir}/%{packname}/example54.kch
%doc %{rlibdir}/%{packname}/example55.kch
%doc %{rlibdir}/%{packname}/example56.kch
%doc %{rlibdir}/%{packname}/example57.kch
%doc %{rlibdir}/%{packname}/example58.kch
%doc %{rlibdir}/%{packname}/example59.kch
%doc %{rlibdir}/%{packname}/example6.kch
%doc %{rlibdir}/%{packname}/example60.kch
%doc %{rlibdir}/%{packname}/example61.kch
%doc %{rlibdir}/%{packname}/example62.kch
%doc %{rlibdir}/%{packname}/example63.kch
%doc %{rlibdir}/%{packname}/example64.kch
%doc %{rlibdir}/%{packname}/example65.kch
%doc %{rlibdir}/%{packname}/example66.kch
%doc %{rlibdir}/%{packname}/example67.kch
%doc %{rlibdir}/%{packname}/example68.kch
%doc %{rlibdir}/%{packname}/example69.kch
%doc %{rlibdir}/%{packname}/example7.kch
%doc %{rlibdir}/%{packname}/example70.kch
%doc %{rlibdir}/%{packname}/example71.kch
%doc %{rlibdir}/%{packname}/example72.kch
%doc %{rlibdir}/%{packname}/example73.kch
%doc %{rlibdir}/%{packname}/example74.kch
%doc %{rlibdir}/%{packname}/example75.kch
%doc %{rlibdir}/%{packname}/example76.kch
%doc %{rlibdir}/%{packname}/example77.kch
%doc %{rlibdir}/%{packname}/example78.kch
%doc %{rlibdir}/%{packname}/example79.kch
%doc %{rlibdir}/%{packname}/example8.kch
%doc %{rlibdir}/%{packname}/example80.kch
%doc %{rlibdir}/%{packname}/example81.kch
%doc %{rlibdir}/%{packname}/example82.kch
%doc %{rlibdir}/%{packname}/example83.kch
%doc %{rlibdir}/%{packname}/example84.kch
%doc %{rlibdir}/%{packname}/example85.kch
%doc %{rlibdir}/%{packname}/example86.kch
%doc %{rlibdir}/%{packname}/example87.kch
%doc %{rlibdir}/%{packname}/example88.kch
%doc %{rlibdir}/%{packname}/example89.kch
%doc %{rlibdir}/%{packname}/example9.kch
%doc %{rlibdir}/%{packname}/example90.kch
%doc %{rlibdir}/%{packname}/example91.kch
%doc %{rlibdir}/%{packname}/example92.kch
%doc %{rlibdir}/%{packname}/example93.kch
%doc %{rlibdir}/%{packname}/example94.kch
%doc %{rlibdir}/%{packname}/example95.kch
%doc %{rlibdir}/%{packname}/example96.kch
%doc %{rlibdir}/%{packname}/example97.kch
%doc %{rlibdir}/%{packname}/example98.kch
%doc %{rlibdir}/%{packname}/example99.kch
%{rlibdir}/%{packname}/INDEX
