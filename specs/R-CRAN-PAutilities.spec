%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAutilities
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Streamline Physical Activity Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-lazyeval >= 0.2
BuildRequires:    R-CRAN-equivalence 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-lazyeval >= 0.2
Requires:         R-CRAN-equivalence 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 

%description
Functions that support a broad range of common tasks in physical activity
research, including but not limited to creation of Bland-Altman plots
(<doi:10.1136/bmj.313.7049.106>), metabolic calculations such as basal
metabolic rate predictions
(<https://europepmc.org/article/med/4044297/reloa>), demographic
calculations such as age-for-body-mass-index percentile
(<https://www.cdc.gov/growthcharts/cdc_charts.htm>), and analysis of bout
detection algorithm performance
(<https://pubmed.ncbi.nlm.nih.gov/34258524/>).

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
