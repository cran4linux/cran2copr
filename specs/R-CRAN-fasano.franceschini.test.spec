%global packname  fasano.franceschini.test
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fasano-Franceschini Test: A 2-D Kolmogorov-Smirnov Two-Sample Test

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-methods 

%description
An implementation of the 2-D Kolmogorov-Smirnov (KS) two-sample test as
defined by Fasano and Franceschini (Fasano and Franceschini 1987). The
'fasano.franceschini.test' package provides three improvements over the
current 2-D KS test on the Comprehensive R Archive Network (CRAN): (i) the
Fasano and Franceschini test has been shown to run in O(n^2) versus the
Peacock implementation which runs in O(n^3); (ii) the package implements a
procedure for handling ties in the data; and (iii) the package implements
a parallelized bootstrapping procedure for improved significance testing.
Ultimately, the 'fasano.franceschini.test' package presents a robust
statistical test for analyzing random samples defined in 2-dimensions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
