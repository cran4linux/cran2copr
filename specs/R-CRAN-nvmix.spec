%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nvmix
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normal Variance Mixtures

License:          GPL (>= 3) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-qrng 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pracma 

%description
Functions for working with (grouped) multivariate normal variance mixture
distributions (evaluation of distribution functions and densities, random
number generation and parameter estimation), including Student's t
distribution for non-integer degrees-of-freedom as well as the grouped t
distribution and copula with multiple degrees-of-freedom parameters. See
<doi:10.18637/jss.v102.i02> for a high-level description of select
functionality.

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
