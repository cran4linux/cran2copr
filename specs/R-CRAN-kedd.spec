%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kedd
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Estimator and Bandwidth Selection for Density and Its Derivatives

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-tools 
Requires:         R-utils 

%description
Kernel estimation of a univariate probability density and of its
derivatives of any order r, with data-driven bandwidth selection. Provides
the kernel estimator of the derivative of order r, the kernels, their
derivatives and convolutions, and eight bandwidth selectors: the
asymptotic MISE rule (AMISE), and unbiased (UCV), biased (BCV1, BCV2),
complete (CCV), modified (MCV), trimmed (TCV), smoothed (SCV) and
maximum-likelihood (MLCV) cross-validation. Supports ten named kernels
(Gaussian, Epanechnikov, uniform, triangular, biweight, triweight,
tricube, cosine, Silverman, logistic) and the power family Pow(s,t),
c(1-|x|^s)^t on [-1,1]. Results are S4 objects with 'ggplot2' graphics;
the O(n^2) criteria are computed in C++ ('Rcpp') with 'OpenMP'
parallelism. Includes five example samples from Marron and Wand (1992)
normal mixtures, a vignette and demos. Companion to Guidoum (2020)
<doi:10.48550/arXiv.2012.06102>.

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
