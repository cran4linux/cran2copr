%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diveMove
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dive Analysis and Calibration

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-uniReg 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-uniReg 

%description
Utilities to represent, visualize, filter, analyse, and summarize
time-depth recorder (TDR) data.  Miscellaneous functions for handling
location data are also provided.

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
