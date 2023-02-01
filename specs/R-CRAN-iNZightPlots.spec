%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iNZightPlots
%global packver   2.15.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.15.1
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Tools for Exploring Data with 'iNZight'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-iNZightMR >= 2.2.7
BuildRequires:    R-CRAN-iNZightTools >= 1.9
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dichromat 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-expss 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-s20x 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-utils 
Requires:         R-CRAN-iNZightMR >= 2.2.7
Requires:         R-CRAN-iNZightTools >= 1.9
Requires:         R-CRAN-boot 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dichromat 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-expss 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-s20x 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-units 
Requires:         R-CRAN-survey 
Requires:         R-utils 

%description
Simple plotting function(s) for exploratory data analysis with flexible
options allowing for easy plot customisation. The goal is to make it easy
for beginners to start exploring a dataset through simple R function
calls, as well as provide a similar interface to summary statistics and
inference information. Includes functionality to generate interactive
HTML-driven graphs. Used by 'iNZight', a graphical user interface
providing easy exploration and visualisation of data for students of
statistics, available in both desktop and online versions.

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
