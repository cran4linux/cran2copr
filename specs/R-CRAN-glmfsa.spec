%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmfsa
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection with Annealing for Sparse Generalized Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Fits sparse generalized linear models under an exact cardinality
constraint using Feature Selection with Annealing (FSA), the method of
Barbu, She, Ding and Gramajo (2017) <doi:10.1109/TPAMI.2016.2544315>.
Rather than inducing sparsity through an L1 (lasso-type) penalty, FSA
alternates a gradient step on the loss with a step that removes the
lowest-magnitude coefficients according to an annealing schedule, so the
user specifies the number of variables directly and the surviving
coefficients carry no shrinkage bias. The working design matrix physically
shrinks as iterations proceed, which makes the cost of a fit fall over
time and the method well suited to problems with very many features.
Gaussian, binomial, Poisson, multinomial, multi-response Gaussian and Cox
proportional hazards families are supported, with robust Lorenz and
smoothed support vector machine (SVM) losses available for classification
with noisy labels. Dense and sparse design matrices are both handled, and
the interface mirrors that of the 'glmnet' package.

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
