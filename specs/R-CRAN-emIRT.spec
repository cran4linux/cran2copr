%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  emIRT
%global packver   0.0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.15
Release:          1%{?dist}%{?buildtag}
Summary:          EM Algorithms for Estimating Item Response Theory Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-pscl >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-pscl >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.10.6

%description
Various Expectation-Maximization (EM) algorithms are implemented for item
response theory (IRT) models. The package includes IRT models for binary
and ordinal responses, along with dynamic and hierarchical IRT models with
binary responses. The latter two models are fitted using variational EM.
The package also includes variational network and text scaling models.
The algorithms are described in Imai, Lo, and Olmsted (2016)
<DOI:10.1017/S000305541600037X>.

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
