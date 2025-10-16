%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dgpsi
%global packver   2.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'dgpsi' for Deep and Linked Gaussian Process Emulations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.26
BuildRequires:    R-CRAN-benchmarkme >= 1.0.8
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-clhs 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-reticulate >= 1.26
Requires:         R-CRAN-benchmarkme >= 1.0.8
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-lhs 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-clhs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-visNetwork 
Requires:         R-parallel 
Requires:         R-CRAN-kableExtra 

%description
Interface to the 'python' package 'dgpsi' for Gaussian process, deep
Gaussian process, and linked deep Gaussian process emulations of computer
models and networks using stochastic imputation (SI). The implementations
follow Ming & Guillas (2021) <doi:10.1137/20M1323771> and Ming,
Williamson, & Guillas (2023) <doi:10.1080/00401706.2022.2124311> and Ming
& Williamson (2023) <doi:10.48550/arXiv.2306.01212>. To get started with
the package, see <https://mingdeyu.github.io/dgpsi-R/>.

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
