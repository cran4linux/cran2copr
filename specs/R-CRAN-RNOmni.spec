%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RNOmni
%global packver   1.0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Rank Normal Transformation Omnibus Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Inverse normal transformation (INT) based genetic association testing.
These tests are recommend for continuous traits with non-normally
distributed residuals. INT-based tests robustly control the type I error
in settings where standard linear regression does not, as when the
residual distribution exhibits excess skew or kurtosis. Moreover,
INT-based tests outperform standard linear regression in terms of power.
These tests may be classified into two types. In direct INT (D-INT), the
phenotype is itself transformed. In indirect INT (I-INT), phenotypic
residuals are transformed. The omnibus test (O-INT) adaptively combines
D-INT and I-INT into a single robust and statistically powerful approach.
See McCaw ZR, Lane JM, Saxena R, Redline S, Lin X. "Operating
characteristics of the rank-based inverse normal transformation for
quantitative trait analysis in genome-wide association studies"
<doi:10.1111/biom.13214>.

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
