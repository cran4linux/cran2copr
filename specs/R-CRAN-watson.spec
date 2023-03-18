%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  watson
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting and Simulating Mixtures of Watson Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Tinflex >= 1.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Tinflex >= 1.8
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Tools for fitting and simulating mixtures of Watson distributions. The
random sampling scheme of the package offers two sampling algorithms that
are based of the results of Sablica, Hornik and Leydold (2022)
<https://research.wu.ac.at/en/publications/random-sampling-from-the-watson-distribution>.
What is more, the package offers a smart tool to combine these two
methods, and based on the selected parameters, it approximates the
relative sampling speed for both methods and picks the faster one. In
addition, the package offers a fitting function for the mixtures of Watson
distribution, that uses the expectation-maximization (EM) algorithm.
Special features are the possibility to use multiple variants of the
E-step and M-step, sparse matrices for the data representation and state
of the art methods for numerical evaluation of needed special functions
using the results of Sablica and Hornik (2022)
<https://www.ams.org/journals/mcom/2022-91-334/S0025-5718-2021-03690-X/>.

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
