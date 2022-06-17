%global __brp_check_rpaths %{nil}
%global packname  rrpack
%global packver   0.1-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Reduced-Rank Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 

%description
Multivariate regression methodologies including classical reduced-rank
regression (RRR) studied by Anderson (1951) <doi:10.1214/aoms/1177729580>
and Reinsel and Velu (1998) <doi:10.1007/978-1-4757-2853-8>, reduced-rank
regression via adaptive nuclear norm penalization proposed by Chen et al.
(2013) <doi:10.1093/biomet/ast036> and Mukherjee et al. (2015)
<doi:10.1093/biomet/asx080>, robust reduced-rank regression (R4) proposed
by She and Chen (2017) <doi:10.1093/biomet/asx032>,
generalized/mixed-response reduced-rank regression (mRRR) proposed by Luo
et al. (2018) <doi:10.1016/j.jmva.2018.04.011>, row-sparse reduced-rank
regression (SRRR) proposed by Chen and Huang (2012)
<doi:10.1080/01621459.2012.734178>, reduced-rank regression with a sparse
singular value decomposition (RSSVD) proposed by Chen et al. (2012)
<doi:10.1111/j.1467-9868.2011.01002.x> and sparse and orthogonal factor
regression (SOFAR) proposed by Uematsu et al. (2019)
<doi:10.1109/TIT.2019.2909889>.

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
