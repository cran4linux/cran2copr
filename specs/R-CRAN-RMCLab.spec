%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMCLab
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lab for Matrix Completion and Imputation of Discrete Rating Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-softImpute 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-softImpute 

%description
Collection of methods for rating matrix completion, which is a statistical
framework for recommender systems. Another relevant application is the
imputation of rating-scale survey data in the social and behavioral
sciences. Note that matrix completion and imputation are synonymous terms
used in different streams of the literature. The main functionality
implements robust matrix completion for discrete rating-scale data with a
low-rank constraint on a latent continuous matrix (Archimbaud, Alfons, and
Wilms (2025) <doi:10.48550/arXiv.2412.20802>). In addition, the package
provides wrapper functions for 'softImpute' (Mazumder, Hastie, and
Tibshirani, 2010, <https://www.jmlr.org/papers/v11/mazumder10a.html>;
Hastie, Mazumder, Lee, Zadeh, 2015,
<https://www.jmlr.org/papers/v16/hastie15a.html>) for easy tuning of the
regularization parameter, as well as benchmark methods such as median
imputation and mode imputation.

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
