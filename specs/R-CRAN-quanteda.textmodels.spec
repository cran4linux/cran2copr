%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quanteda.textmodels
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          1%{?dist}%{?buildtag}
Summary:          Scaling Models and Classifiers for Textual Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-quanteda >= 4.0.0
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.7.600.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-LiblineaR 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-quanteda >= 4.0.0
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-LiblineaR 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-stringi 

%description
Scaling models and classifiers for sparse matrix objects representing
textual data in the form of a document-feature matrix.  Includes original
implementations of 'Laver', 'Benoit', and Garry's (2003)
<doi:10.1017/S0003055403000698>, 'Wordscores' model, the Perry and
'Benoit' (2017) <doi:10.48550/arXiv.1710.08963> class affinity scaling
model, and the 'Slapin' and 'Proksch' (2008)
<doi:10.1111/j.1540-5907.2008.00338.x> 'wordfish' model, as well as
methods for correspondence analysis, latent semantic analysis, and fast
Naive Bayes and linear 'SVMs' specially designed for sparse textual data.

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
