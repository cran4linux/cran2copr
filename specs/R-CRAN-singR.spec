%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  singR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Non-Gaussian Component Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-MASS >= 7.3.57
BuildRequires:    R-CRAN-gam >= 1.20.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-clue >= 0.3.61
BuildRequires:    R-CRAN-ICtest >= 0.3.5
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS >= 7.3.57
Requires:         R-CRAN-gam >= 1.20.1
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-clue >= 0.3.61
Requires:         R-CRAN-ICtest >= 0.3.5

%description
Implementation of SING algorithm to extract joint and individual
non-Gaussian components from two datasets. SING uses an objective function
that maximizes the skewness and kurtosis of latent components with a
penalty to enhance the similarity between subject scores. Unlike other
existing methods, SING does not use PCA for dimension reduction, but
rather uses non-Gaussianity, which can improve feature extraction.
Benjamin B.Risk, Irina Gaynanova (2021) <doi:10.1214/21-AOAS1466>.

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
