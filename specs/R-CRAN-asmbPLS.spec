%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  asmbPLS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predicting and Classifying Patient Phenotypes with Multi-Omics Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-stats 

%description
Adaptive Sparse Multi-block Partial Least Square, a supervised algorithm,
is an extension of the Sparse Multi-block Partial Least Square, which
allows different quantiles to be used in different blocks of different
partial least square components to decide the proportion of features to be
retained. The best combinations of quantiles can be chosen from a set of
user-defined quantiles combinations by cross-validation. By doing this, it
enables us to do the feature selection for different blocks, and the
selected features can then be further used to predict the outcome. For
example, in biomedical applications, clinical covariates plus different
types of omics data such as microbiome, metabolome, mRNA data, methylation
data, copy number variation data might be predictive for patients outcome
such as survival time or response to therapy. Different types of data
could be put in different blocks and along with survival time to fit the
model. The fitted model can then be used to predict the survival for the
new samples with the corresponding clinical covariates and omics data. In
addition, Adaptive Sparse Multi-block Partial Least Square Discriminant
Analysis is also included, which extends Adaptive Sparse Multi-block
Partial Least Square for classifying the categorical outcome.

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
