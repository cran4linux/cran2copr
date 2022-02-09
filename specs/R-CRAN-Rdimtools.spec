%global __brp_check_rpaths %{nil}
%global packname  Rdimtools
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Dimension Reduction and Estimation Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-CVXR >= 1.0
BuildRequires:    R-CRAN-maotai >= 0.2.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-RcppDE 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mclustcomp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-CVXR >= 1.0
Requires:         R-CRAN-maotai >= 0.2.4
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-RcppDE 
Requires:         R-CRAN-Rcsdp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RSpectra 
Requires:         R-graphics 
Requires:         R-CRAN-mclustcomp 
Requires:         R-stats 
Requires:         R-utils 

%description
We provide linear and nonlinear dimension reduction techniques. Intrinsic
dimension estimation methods for exploratory analysis are also provided.
For more details on the package, see the paper by You (2020)
<arXiv:2005.11107>.

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
