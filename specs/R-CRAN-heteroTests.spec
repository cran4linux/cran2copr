%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heteroTests
%global packver   0.11.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.2
Release:          1%{?dist}%{?buildtag}
Summary:          Heteroscedasticity Diagnostics for Linear Models

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-SuppDists 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-R6 
Requires:         R-parallel 
Requires:         R-CRAN-SuppDists 

%description
Provides a unified set of heteroscedasticity diagnostics for linear-model
workflows. It implements classical auxiliary-regression tests, including
those of White (1980) <doi:10.2307/1912934>, Breusch and Pagan (1979)
<doi:10.2307/1911963>, Koenker (1981) <doi:10.1016/0304-4076(81)90062-2>,
Goldfeld and Quandt (1965) <doi:10.1080/01621459.1965.10480811> and Harvey
(1976) <doi:10.2307/1913974>; the score test of Cook and Weisberg (1983)
<doi:10.1093/biomet/70.1.1>; the ARCH test of Engle (1982)
<doi:10.2307/1912773>; and group-wise tests of equal variance, including
those of Bartlett (1937) <doi:10.1098/rspa.1937.0109>, Brown and Forsythe
(1974) <doi:10.1080/01621459.1974.10482955> and Hartley (1950)
<doi:10.2307/2332383>. Resampling and scalable variants, simulation
utilities, diagnostic visualisation and remediation helpers share a
consistent interface designed for reproducible statistical workflows and
integration with common modelling tools.

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
