%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  slideimp
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Numeric Matrices K-NN and PCA Imputation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-mlpack 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEnsmallen 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Fast k-nearest neighbors (K-NN) and principal component analysis (PCA)
imputation algorithms for missing values in high-dimensional numeric
matrices, i.e., epigenetic data. For extremely high-dimensional data with
ordered features, a sliding window approach for K-NN or PCA imputation is
provided.  Additional features include group-wise imputation (e.g., by
chromosome), hyperparameter tuning with repeated cross-validation,
multi-core parallelization, and optional subset imputation. The K-NN
algorithm is described in: Hastie, T., Tibshirani, R., Sherlock, G.,
Eisen, M., Brown, P. and Botstein, D.  (1999) "Imputing Missing Data for
Gene Expression Arrays". The PCA imputation is an optimized version of the
imputePCA() function from the 'missMDA' package described in: Josse, J.
and Husson, F.  (2016) <doi:10.18637/jss.v070.i01> "missMDA: A Package for
Handling Missing Values in Multivariate Data Analysis".

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
