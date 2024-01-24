%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phenofit
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Remote Sensing Vegetation Phenology

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zeallot 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-CRAN-zeallot 

%description
The merits of 'TIMESAT' and 'phenopix' are adopted. Besides, a simple and
growing season dividing method and a practical snow elimination method
based on Whittaker were proposed. 7 curve fitting methods and 4 phenology
extraction methods were provided. Parameters boundary are considered for
every curve fitting methods according to their ecological meaning. And
'optimx' is used to select best optimization method for different curve
fitting methods. Reference: Kong, D., (2020). R package: A
state-of-the-art Vegetation Phenology extraction package, phenofit version
0.3.1, <doi:10.5281/zenodo.5150204>; Kong, D., Zhang, Y., Wang, D., Chen,
J., & Gu, X. (2020). Photoperiod Explains the Asynchronization Between
Vegetation Carbon Phenology and Vegetation Greenness Phenology. Journal of
Geophysical Research: Biogeosciences, 125(8), e2020JG005636.
<doi:10.1029/2020JG005636>; Kong, D., Zhang, Y., Gu, X., & Wang, D.
(2019). A robust method for reconstructing global MODIS EVI time series on
the Google Earth Engine. ISPRS Journal of Photogrammetry and Remote
Sensing, 155, 13–24; Zhang, Q., Kong, D., Shi, P., Singh, V.P., Sun, P.,
2018. Vegetation phenology on the Qinghai-Tibetan Plateau and its response
to climate change (1982–2013). Agric. For. Meteorol. 248, 408–417.
<doi:10.1016/j.agrformet.2017.10.026>.

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
