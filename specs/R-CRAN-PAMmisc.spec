%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAMmisc
%global packver   1.11.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.6
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions for Passive Acoustic Analysis

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-PamBinaries 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rerddap 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-rjson 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-PamBinaries 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rerddap 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-hoardr 
Requires:         R-methods 
Requires:         R-CRAN-geosphere 
Requires:         R-tcltk 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-rjson 

%description
A collection of miscellaneous functions for passive acoustics. Much of the
content here is adapted to R from code written by other people. If you
have any ideas of functions to add, please contact Taiki Sakai.

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
