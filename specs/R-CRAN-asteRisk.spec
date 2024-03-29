%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  asteRisk
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Satellite Position

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-nanotime 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-onion 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-nanotime 
Requires:         R-stats 
Requires:         R-CRAN-onion 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-utils 

%description
Provides basic functionalities to calculate the position of satellites
given a known state vector. The package includes implementations of the
SGP4 and SDP4 simplified perturbation models to propagate orbital state
vectors, as well as utilities to read TLE files and convert coordinates
between different frames of reference. Several of the functionalities of
the package (including the high-precision numerical orbit propagator)
require the coefficients and data included in the 'asteRiskData' package,
available in a 'drat' repository. To install this data package, run
'install.packages("asteRiskData",
repos="https://rafael-ayala.github.io/drat/")'. Felix R. Hoots, Ronald L.
Roehrich and T.S. Kelso (1988)
<https://celestrak.org/NORAD/documentation/spacetrk.pdf>. David Vallado,
Paul Crawford, Richard Hujsak and T.S. Kelso (2012)
<doi:10.2514/6.2006-6753>. Felix R. Hoots, Paul W. Schumacher Jr. and
Robert A. Glover (2014) <doi:10.2514/1.9161>.

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
