%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesPop
%global packver   11.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          11.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Population Projection

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bayesTFR >= 7.1.0
BuildRequires:    R-CRAN-bayesLife >= 5.0.0
BuildRequires:    R-CRAN-MortCast >= 2.6.1
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-wpp2019 
BuildRequires:    R-CRAN-wpp2012 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rworldmap 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-googleVis 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-bayesTFR >= 7.1.0
Requires:         R-CRAN-bayesLife >= 5.0.0
Requires:         R-CRAN-MortCast >= 2.6.1
Requires:         R-parallel 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-wpp2019 
Requires:         R-CRAN-wpp2012 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rworldmap 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-googleVis 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 

%description
Generating population projections for all countries of the world using
several probabilistic components, such as total fertility rate and life
expectancy (Raftery et al., 2012 <doi:10.1073/pnas.1211452109>).

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
