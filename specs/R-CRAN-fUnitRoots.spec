%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fUnitRoots
%global packver   4021.80
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4021.80
Release:          1%{?dist}%{?buildtag}
Summary:          Rmetrics - Modelling Trends and Unit Roots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-urca 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides four addons for analyzing trends and unit roots in financial time
series: (i) functions for the density and probability of the augmented
Dickey-Fuller Test, (ii) functions for the density and probability of
MacKinnon's unit root test statistics, (iii) reimplementations for the ADF
and MacKinnon Test, and (iv) an 'urca' Unit Root Test Interface for
Pfaff's unit root test suite.

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
