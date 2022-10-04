%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROI.plugin.qpoases
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'qpOASES' Plugin for the 'R' Optimization Infrastructure

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ROI >= 0.2.5
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-ROI >= 0.2.5
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-methods 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-checkmate 

%description
Enhances the 'R' Optimization Infrastructure ('ROI') package with the
quadratic solver 'qpOASES'. More information about 'qpOASES' can be found
at <https://github.com/coin-or/qpOASES>.

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
