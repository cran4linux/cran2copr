%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zigg
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight Interfaces to the 'Ziggurat' Pseudo Random Number Generator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
The 'Ziggurat' pseudo-random number generator (or PRNG), introduced by
Marsaglia and Tsang (2000, <doi:10.18637/jss.v005.i08>) and further
improved by Leong et al (2005, <doi:10.18637/jss.v012.i07>), offers a
lightweight and very fast PRNG for the normal, exponential, and uniform
distributions. It is provided here in a small zero-dependency package. It
can be used from R as well as from 'C/C++' code in other packages as is
demonstrated by four included sample packages using four distinct methods
to use the PRNG presented here in client package. The implementation is
influenced by our package 'RcppZiggurat' which offers a comparison among
multiple alternative implementations but presented here in a
lighter-weight implementation that is easier to use by other packages. The
PRNGs provided are generally faster than the ones in base R: on our
machine, the relative gains for normal, exponential and uniform are on the
order of 7.4, 5.2 and 4.7 times faster than base R. However, these
generators are of potentially lesser quality and shorter period so if in
doubt use of the base R functions remains the general recommendation.

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
