%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geohabnet
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Cropland Connectivity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.3.7
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-terra >= 1.7.29
BuildRequires:    R-CRAN-geosphere >= 1.5.18
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-igraph >= 1.4.2
BuildRequires:    R-CRAN-beepr >= 1.3
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-easycsv >= 1.0.8
BuildRequires:    R-CRAN-geodata >= 0.5.8
BuildRequires:    R-CRAN-viridisLite >= 0.4.2
BuildRequires:    R-CRAN-rnaturalearth >= 0.3.3
BuildRequires:    R-CRAN-config >= 0.3.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
Requires:         R-CRAN-yaml >= 2.3.7
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-terra >= 1.7.29
Requires:         R-CRAN-geosphere >= 1.5.18
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-igraph >= 1.4.2
Requires:         R-CRAN-beepr >= 1.3
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-easycsv >= 1.0.8
Requires:         R-CRAN-geodata >= 0.5.8
Requires:         R-CRAN-viridisLite >= 0.4.2
Requires:         R-CRAN-rnaturalearth >= 0.3.3
Requires:         R-CRAN-config >= 0.3.1
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tools 

%description
Geographical spatial analysis of cropland connectivity. Allows users to
visualize risk index plots for a given set of crops. The functions are
developed as an extension to analysis from Xing et al (2021)
<doi:10.1093/biosci/biaa067>. The primary function is sean() and is
indicative of how sensitive the risk analysis is to parameters using
kernel models. The Package currently supports crops sourced from Monfreda,
C., N. Ramankutty, and J. A. Foley (2008) <doi:10.1029/2007gb002947>
"Farming the planet: 2. Geographic distribution of crop areas, yields,
physiological types, and net primary production in the year 2000, Global
Biogeochem. Cycles, 22, GB1022" and International Food Policy Research
Institute (2019) <doi:10.7910/DVN/PRFF8V> "Global Spatially-Disaggregated
Crop Production Statistics Data for 2010 Version 2.0, Harvard Dataverse,
V4". This analysis produces 3 maps - mean, variance, and difference for
the crop risk index. It applies distance functions and graph operations on
a network to calculate risk index. There are multiple ways in which
functions can be used - generate final outcome and then the intermediate
outcomes for more sophisticated use cases. Refer to vignettes. sean() will
set some global variables which can be accessed using $ prefix. These
values are propagated to other functions for performing operations such as
distance matrix calculation. parameters.yaml stores the parameters and
values and can be accessed using get_parameters(). Refer it's usage. The
objective of this package is to support risk analysis using cropland
connectivity on 10 parameters - host crops, density threshold, aggregation
and distance method, resolution, geographic extent, link threshold, kernel
models, network metrics and maps. These parameters serves as an input and
are used different phases of analysis workflow.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
