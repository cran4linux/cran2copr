%global __brp_check_rpaths %{nil}
%global packname  iNZightPlots
%global packver   2.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Graphical Tools for Exploring Data with 'iNZight'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-iNZightMR >= 2.2.5
BuildRequires:    R-CRAN-iNZightTools >= 1.9
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-s20x 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-dichromat 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-iNZightMR >= 2.2.5
Requires:         R-CRAN-iNZightTools >= 1.9
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-s20x 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-dichromat 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 

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
