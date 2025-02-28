%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MomTrunc
%global packver   6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Moments of Folded and Doubly Truncated Multivariate Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-tlrmvnmvt >= 1.1.0
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-tlrmvnmvt >= 1.1.0
Requires:         R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-hypergeo 

%description
It computes arbitrary products moments (mean vector and
variance-covariance matrix), for some double truncated (and folded)
multivariate distributions. These distributions belong to the family of
selection elliptical distributions, which includes well known skewed
distributions as the unified skew-t distribution (SUT) and its particular
cases as the extended skew-t (EST), skew-t (ST) and the symmetric
student-t (T) distribution. Analogous normal cases unified skew-normal
(SUN), extended skew-normal (ESN), skew-normal (SN), and symmetric normal
(N) are also included. Density, probabilities and random deviates are also
offered for these members.

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
