%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DGP4LCF
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dependent Gaussian Processes for Longitudinal Correlated Factors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-GPFDA 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-factor.switching 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-GPFDA 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-factor.switching 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-pheatmap 
Requires:         R-stats 

%description
Functionalities for analyzing high-dimensional and longitudinal biomarker
data to facilitate precision medicine, using a joint model of Bayesian
sparse factor analysis and dependent Gaussian processes. This paper
illustrates the method in detail: J Cai, RJB Goudie, C Starr, BDM Tom
(2023) <doi:10.48550/arXiv.2307.02781>.

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
