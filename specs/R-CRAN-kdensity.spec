%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kdensity
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Density Estimation with Parametric Starts and Asymmetric Kernels

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-univariateML 
BuildRequires:    R-CRAN-EQL 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-univariateML 
Requires:         R-CRAN-EQL 

%description
Handles univariate non-parametric density estimation with parametric
starts and asymmetric kernels in a simple and flexible way. Kernel density
estimation with parametric starts involves fitting a parametric density to
the data before making a correction with kernel density estimation, see
Hjort & Glad (1995) <doi:10.1214/aos/1176324627>. Asymmetric kernels make
kernel density estimation more efficient on bounded intervals such as (0,
1) and the positive half-line. Supported asymmetric kernels are the gamma
kernel of Chen (2000) <doi:10.1023/A:1004165218295>, the beta kernel of
Chen (1999) <doi:10.1016/S0167-9473(99)00010-9>, and the copula kernel of
Jones & Henderson (2007) <doi:10.1093/biomet/asm068>. User-supplied
kernels, parametric starts, and bandwidths are supported.

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
