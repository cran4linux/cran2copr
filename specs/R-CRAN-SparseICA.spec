%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SparseICA
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Independent Component Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-MASS >= 7.3.58
BuildRequires:    R-parallel >= 4.1
BuildRequires:    R-CRAN-irlba >= 2.3.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-clue >= 0.3
BuildRequires:    R-CRAN-ciftiTools >= 0.16
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.58
Requires:         R-parallel >= 4.1
Requires:         R-CRAN-irlba >= 2.3.5
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-clue >= 0.3
Requires:         R-CRAN-ciftiTools >= 0.16

%description
Provides an implementation of the Sparse ICA method in Wang et al. (2024)
<doi:10.1080/01621459.2024.2370593> for estimating sparse independent
source components of cortical surface functional MRI data, by addressing a
non-smooth, non-convex optimization problem through the relax-and-split
framework. This method effectively balances statistical independence and
sparsity while maintaining computational efficiency.

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
