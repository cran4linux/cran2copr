%global packname  forestinventory
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design-Based Global and Small-Area Estimations for Multiphase Forest Inventories

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 

%description
Extensive global and small-area estimation procedures for multiphase
forest inventories under the design-based Monte-Carlo approach are
provided. The implementation has been published in the Journal of
Statistical Software (<doi:10.18637/jss.v097.i04>) and includes estimators
for simple and cluster sampling published by Daniel Mandallaz in 2007
(<doi:10.1201/9781584889779>), 2013 (<doi:10.1139/cjfr-2012-0381>,
<doi:10.1139/cjfr-2013-0181>, <doi:10.1139/cjfr-2013-0449>,
<doi:10.3929/ethz-a-009990020>) and 2016 (<doi:10.3929/ethz-a-010579388>).
It provides point estimates, their external- and design-based variances
and confidence intervals, as well as a set of functions to analyze and
visualize the produced estimates. The procedures have also been optimized
for the use of remote sensing data as auxiliary information, as
demonstrated in 2018 by Hill et al. (<doi:10.3390/rs10071052>).

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
