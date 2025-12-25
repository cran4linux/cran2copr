%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tlrmvnmvt
%global packver   1.1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Low-Rank Methods for MVN and MVT Probabilities

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-methods >= 4.2.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.5.0
Requires:         R-methods >= 4.2.0
Requires:         R-CRAN-Rcpp >= 1.0.8

%description
Implementation of the classic Genz algorithm and a novel tile-low-rank
algorithm for computing relatively high-dimensional multivariate normal
(MVN) and Student-t (MVT) probabilities. References used for this package:
Foley, James, Andries van Dam, Steven Feiner, and John Hughes. "Computer
Graphics: Principle and Practice". Addison-Wesley Publishing Company.
Reading, Massachusetts (1987, ISBN:0-201-84840-6 1); Genz, A., "Numerical
computation of multivariate normal probabilities," Journal of
Computational and Graphical Statistics, 1, 141-149 (1992)
<doi:10.1080/10618600.1992.10477010>; Cao, J., Genton, M. G., Keyes, D.
E., & Turkiyyah, G. M. "Exploiting Low Rank Covariance Structures for
Computing High-Dimensional Normal and Student- t Probabilities,"
Statistics and Computing, 31.1, 1-16 (2021)
<doi:10.1007/s11222-020-09978-y>; Cao, J., Genton, M. G., Keyes, D. E., &
Turkiyyah, G. M. "tlrmvnmvt: Computing High-Dimensional Multivariate
Normal and Student-t Probabilities with Low-Rank Methods in R," Journal of
Statistical Software, 101.4, 1-25 (2022) <doi:10.18637/jss.v101.i04>.

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
