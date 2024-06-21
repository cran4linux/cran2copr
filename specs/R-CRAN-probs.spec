%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  probs
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Elementary Probability on Finite Sample Spaces

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-reshape 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-reshape 

%description
Performs elementary probability calculations on finite sample spaces,
which may be represented by data frames or lists. This package is meant to
rescue some widely used functions from the archived 'prob' package (see
<https://cran.r-project.org/src/contrib/Archive/prob/>). Functionality
includes setting up sample spaces, counting tools, defining probability
spaces, performing set algebra, calculating probability and conditional
probability, tools for simulation and checking the law of large numbers,
adding random variables, and finding marginal distributions.
Characteristic functions for all base R distributions are included.

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
