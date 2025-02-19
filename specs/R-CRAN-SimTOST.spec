%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimTOST
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Estimation for Bio-Equivalence Trials Through Simulation

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.13
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.13
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-matrixcalc 
Requires:         R-parallel 

%description
Sample size estimation for bio-equivalence trials is supported through a
simulation-based approach that extends the Two One-Sided Tests (TOST)
procedure. The methodology provides flexibility in hypothesis testing,
accommodates multiple treatment comparisons, and accounts for correlated
endpoints. Users can model complex trial scenarios, including parallel and
crossover designs, intra-subject variability, and different equivalence
margins. Monte Carlo simulations enable accurate estimation of power and
type I error rates, ensuring well-calibrated study designs. The
statistical framework builds on established methods for equivalence
testing and multiple hypothesis testing in bio-equivalence studies, as
described in Schuirmann (1987) <doi:10.1007/BF01068419>, Mielke et al.
(2018) <doi:10.1080/19466315.2017.1371071>, Shieh (2022)
<doi:10.1371/journal.pone.0269128>, and Sozu et al. (2015)
<doi:10.1007/978-3-319-22005-5>. Comprehensive documentation and vignettes
guide users through implementation and interpretation of results.

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
