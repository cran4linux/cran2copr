%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  resemble
%global packver   2.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Memory-Based Learning in Spectral Chemometrics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-magrittr >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-mathjaxr >= 1.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-magrittr >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-mathjaxr >= 1.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 

%description
Functions for dissimilarity analysis and memory-based learning (MBL, a.k.a
local modeling) in complex spectral data sets. Most of these functions are
based on the methods presented in Ramirez-Lopez et al. (2013)
<doi:10.1016/j.geoderma.2012.12.014>.

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
