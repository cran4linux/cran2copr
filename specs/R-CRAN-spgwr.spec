%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spgwr
%global packver   0.6-37
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.37
Release:          1%{?dist}%{?buildtag}
Summary:          Geographically Weighted Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-spData >= 2.3.1
BuildRequires:    R-CRAN-sp >= 0.8.3
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-spData >= 2.3.1
Requires:         R-CRAN-sp >= 0.8.3
Requires:         R-stats 
Requires:         R-methods 

%description
Functions for computing geographically weighted regressions are provided,
based on work by Chris Brunsdon, Martin Charlton and Stewart Fotheringham.

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
