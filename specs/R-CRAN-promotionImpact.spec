%global packname  promotionImpact
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis & Measurement of Promotion Effectiveness

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-KernSmooth >= 2.23.15
BuildRequires:    R-CRAN-strucchange >= 1.5.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-lmtest >= 0.9
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-prophet >= 0.6
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-CRAN-ggpubr >= 0.1.8
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-KernSmooth >= 2.23.15
Requires:         R-CRAN-strucchange >= 1.5.1
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-lmtest >= 0.9
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-prophet >= 0.6
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-CRAN-ggpubr >= 0.1.8

%description
Analysis and measurement of promotion effectiveness on a given target
variable (e.g. daily sales). After converting promotion schedule into
dummy or smoothed predictor variables, the package estimates the effects
of these variables controlled for trend/periodicity/structural change
using prophet by Taylor and Letham (2017)
<doi:10.7287/peerj.preprints.3190v2> and some prespecified variables (e.g.
start of a month).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
