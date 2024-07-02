%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  soiltestcorr
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Soil Test Correlation and Calibration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpp 
BuildRequires:    R-CRAN-nlstools 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-nlraa 
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-smatr 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpp 
Requires:         R-CRAN-nlstools 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-nlraa 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-smatr 

%description
A compilation of functions designed to assist users on the correlation
analysis of crop yield and soil test values. Functions to estimate crop
response patterns to soil nutrient availability and critical soil test
values using various approaches such as: 1) the modified arcsine-log
calibration curve (Correndo et al. (2017) <doi:10.1071/CP16444>); 2) the
graphical Cate-Nelson quadrants analysis (Cate & Nelson (1965)), 3) the
statistical Cate-Nelson quadrants analysis (Cate & Nelson (1971)
<doi:10.2136/sssaj1971.03615995003500040048x>), 4) the linear-plateau
regression (Anderson & Nelson (1975) <doi:10.2307/2529422>), 5) the
quadratic-plateau regression (Bullock & Bullock (1994)
<doi:10.2134/agronj1994.00021962008600010033x>), and 6) the
Mitscherlich-type exponential regression (Melsted & Peck (1977)
<doi:10.2134/asaspecpub29.c1>). The package development stemmed from
ongoing work with the Fertilizer Recommendation Support Tool (FRST) and
Feed the Future Innovation Lab for Collaborative Research on Sustainable
Intensification (SIIL) projects.

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
