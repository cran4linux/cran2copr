%global __brp_check_rpaths %{nil}
%global packname  TTAinterfaceTrendAnalysis
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Trend Analysis Graphical Interface

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-relimp 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-rkt 
BuildRequires:    R-CRAN-stlplus 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-relimp 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-rkt 
Requires:         R-CRAN-stlplus 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-lubridate 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-zoo 
Requires:         R-methods 

%description
This interface was created to develop a standard procedure to analyse
temporal trend in the framework of the OSPAR convention. The analysis
process run through 4 successive steps : 1) manipulate your data, 2)
select the parameters you want to analyse, 3) build your regulated time
series, 4) perform diagnosis and analysis and 5) read the results.
Statistical analysis call other package function such as Kendall tests or
cusum() function.

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
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
