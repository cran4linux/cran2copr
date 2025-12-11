%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qrmtools
%global packver   0.0-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Quantitative Risk Management

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-quantmod 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rugarch 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ADGofTest 
Requires:         R-graphics 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-quantmod 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-rugarch 
Requires:         R-utils 
Requires:         R-CRAN-ADGofTest 

%description
Functions and data sets for reproducing selected results from the book
"Quantitative Risk Management: Concepts, Techniques and Tools".
Furthermore, new developments and auxiliary functions for Quantitative
Risk Management practice.

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
