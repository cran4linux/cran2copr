%global __brp_check_rpaths %{nil}
%global packname  cricketr
%global packver   0.0.26
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.26
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Cricketers and Cricket Teams Based on ESPN Cricinfo Statsguru

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-XML 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-httr 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for analyzing performances of cricketers based on stats in ESPN
Cricinfo Statsguru. The toolset can be used for analysis of Tests,ODIs and
Twenty20 matches of both batsmen and bowlers. The package can also be used
to analyze team performances.

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
