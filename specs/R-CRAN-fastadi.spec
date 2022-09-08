%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastadi
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Self-Tuning Data Adaptive Matrix Imputation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-LRMF3 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ellipsis 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-LRMF3 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ellipsis 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-logger 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RSpectra 

%description
Implements the AdaptiveImpute matrix completion algorithm of 'Intelligent
Initialization and Adaptive Thresholding for Iterative Matrix Completion',
<https://amstat.tandfonline.com/doi/abs/10.1080/10618600.2018.1518238>.
AdaptiveImpute is useful for embedding sparsely observed matrices, often
out performs competing matrix completion algorithms, and self-tunes its
hyperparameter, making usage easy.

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
