%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  remote
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Empirical Orthogonal Teleconnections in R

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Empirical orthogonal teleconnections in R. 'remote' is short for
'R(-based) EMpirical Orthogonal TEleconnections'. It implements a
collection of functions to facilitate empirical orthogonal teleconnection
analysis. Empirical Orthogonal Teleconnections (EOTs) denote a regression
based approach to decompose spatio-temporal fields into a set of
independent orthogonal patterns. They are quite similar to Empirical
Orthogonal Functions (EOFs) with EOTs producing less abstract results. In
contrast to EOFs, which are orthogonal in both space and time, EOT
analysis produces patterns that are orthogonal in either space or time.

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
