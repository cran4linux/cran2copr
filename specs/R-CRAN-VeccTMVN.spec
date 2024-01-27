%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VeccTMVN
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Normal Probabilities using Vecchia Approximation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix >= 1.5.3
BuildRequires:    R-CRAN-truncnorm >= 1.0.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-GpGp >= 0.4.0
BuildRequires:    R-CRAN-GPvecchia 
BuildRequires:    R-CRAN-TruncatedNormal 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix >= 1.5.3
Requires:         R-CRAN-truncnorm >= 1.0.8
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-GpGp >= 0.4.0
Requires:         R-CRAN-GPvecchia 
Requires:         R-CRAN-TruncatedNormal 

%description
Under a different representation of the multivariate normal (MVN)
probability, we can use the Vecchia approximation to sample the integrand
at a linear complexity with respect to n. Additionally, both the SOV
algorithm from Genz (92) and the exponential-tilting method from Botev
(2017) can be adapted to linear complexity. The reference for the method
implemented in this package is Jian Cao and Matthias Katzfuss (2024)
"Linear-Cost Vecchia Approximation of Multivariate Normal Probabilities"
<arXiv:2311.09426>. Two major references for the development of our method
are Alan Genz (1992) "Numerical Computation of Multivariate Normal
Probabilities" <doi:10.1080/10618600.1992.10477010> and Z. I. Botev (2017)
"The Normal Law Under Linear Restrictions: Simulation and Estimation via
Minimax Tilting" <arXiv:1603.04166>.

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
