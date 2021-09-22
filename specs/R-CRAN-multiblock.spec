%global __brp_check_rpaths %{nil}
%global packname  multiblock
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiblock Data Fusion in Statistics and Machine Learning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-geigen 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-MFAg 
BuildRequires:    R-CRAN-mixlm 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-plsVarSel 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-r.jive 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RegularizedSCA 
BuildRequires:    R-CRAN-RGCCA 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-SSBtools 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-car 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-geigen 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-MFAg 
Requires:         R-CRAN-mixlm 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-plsVarSel 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-r.jive 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RegularizedSCA 
Requires:         R-CRAN-RGCCA 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-SSBtools 

%description
Functions and datasets to support Smilde, Næs and Liland (2021, ISBN:
978-1-119-60096-1) "Multiblock Data Fusion in Statistics and Machine
Learning - Applications in the Natural and Life Sciences". This implements
and imports a large collection of methods for multiblock data analysis
with common interfaces, result- and plotting functions, several real data
sets and six vignettes covering a range different applications.

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
