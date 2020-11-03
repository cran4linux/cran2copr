%global packname  samc
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Absorbing Markov Chains

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-raster 

%description
Implements functions for working with absorbing Markov chains. The
implementation is based on the framework described in "Toward a unified
framework for connectivity that disentangles movement and mortality in
space and time" by Fletcher et al. (2019) <doi:10.1111/ele.13333>, which
applies them to spatial ecology. This framework incorporates both
resistance and absorption with spatial absorbing Markov chains (SAMC) to
provide several short-term and long-term predictions for metrics related
to connectivity in landscapes. Despite the ecological context of the
framework, this package can be used in any application of absorbing Markov
chains.

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
