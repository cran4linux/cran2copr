%global __brp_check_rpaths %{nil}
%global packname  cuda.ml
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface for the RAPIDS cuML Suite of Libraries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.6
BuildRequires:    R-CRAN-rlang >= 0.1.4
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-parsnip 
Requires:         R-CRAN-Rcpp >= 1.0.6
Requires:         R-CRAN-rlang >= 0.1.4
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-parsnip 

%description
R interface for RAPIDS cuML (<https://github.com/rapidsai/cuml>), a suite
of GPU-accelerated machine learning libraries powered by CUDA
(<https://en.wikipedia.org/wiki/CUDA>).

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
