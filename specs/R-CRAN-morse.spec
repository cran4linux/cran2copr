%global __brp_check_rpaths %{nil}
%global packname  morse
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Tools for Reproduction and Survival Data in Ecotoxicology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rjags >= 4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-rjags >= 4.0
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-coda 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-epitools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 

%description
Tools for ecotoxicologists and regulators dedicated to the mathematical
and statistical modelling of toxicity test data. They use advanced and
innovative methods for a valuable quantitative environmental risk
assessment. See also Delignette-Muller et al. (2017)
<doi:10.1021/acs.est.6b05326>. and Baudrot et al. (2018)
<doi:10.1021/acs.est.7b05464>.

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
