%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  underdisp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics and Models for Underdispersed Count Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-VGAM 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Tools for detecting and modeling underdispersion in count data
(conditional variance below the conditional mean), a phenomenon overlooked
by the Poisson and negative binomial defaults. Provides a screening
diagnostic that benchmarks at-risk dispersion against a zero-truncated
Poisson; the continuous parameter binomial (CPB) regression and its
zero-truncated variant, with an interpretable observation-specific bound
and high-dimensional fixed-effects support; validated bootstrap (for
coefficients) and profile-likelihood (for the dispersion parameter)
inference; and quantities of interest including predicted probabilities
and the implied ceiling. The likelihood is implemented in C++ for speed.

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
