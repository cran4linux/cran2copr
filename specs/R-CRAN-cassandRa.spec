%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cassandRa
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Finds Missing Links and Metric Confidence Intervals in Ecological Bipartite Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-vegan >= 2.5.3
BuildRequires:    R-CRAN-bipartite >= 2.11
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 0.8
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-vegan >= 2.5.3
Requires:         R-CRAN-bipartite >= 2.11
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-tidyr >= 0.8
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Provides methods to deal with under sampling in ecological bipartite
networks from Terry and Lewis (2020) Ecology <doi:10.1002/ecy.3047>
Includes tools to fit a variety of statistical network models and sample
coverage estimators to highlight most likely missing links. Also includes
simple functions to resample from observed networks to generate confidence
intervals for common ecological network metrics.

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
