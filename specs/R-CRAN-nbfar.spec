%global __brp_check_rpaths %{nil}
%global packname  nbfar
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Negative Binomial Factor Regression Models ('nbfar')

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rrpack 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-mpath 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rrpack 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-mpath 

%description
We developed a negative binomial factor regression model to estimate
structured (sparse) associations between a feature matrix X and
overdispersed count data Y.  With 'nbfar', microbiome count data Y can be
used, for example, to associate host or environmental covariates with
microbial abundances. Currently, two models are available: a) Negative
Binomial reduced rank regression (NB-RRR), b) Negative Binomial co-sparse
factor regression (NB-FAR). Please refer the manuscript 'Mishra, A. K., &
Müller, C. L. (2021). Negative Binomial factor regression with application
to microbiome data analysis. bioRxiv.' for more details.

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
