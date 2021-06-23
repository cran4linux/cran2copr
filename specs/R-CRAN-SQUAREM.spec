%global __brp_check_rpaths %{nil}
%global packname  SQUAREM
%global packver   2021.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2021.1
Release:          1%{?dist}%{?buildtag}
Summary:          Squared Extrapolation Methods for Accelerating EM-Like Monotone Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch

%description
Algorithms for accelerating the convergence of slow, monotone sequences
from smooth, contraction mapping such as the EM algorithm. It can be used
to accelerate any smooth, linearly convergent acceleration scheme.  A
tutorial style introduction to this package is available in a vignette on
the CRAN download page or, when the package is loaded in an R session,
with vignette("SQUAREM"). Refer to the J Stat Software article:
<doi:10.18637/jss.v092.i07>.

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
