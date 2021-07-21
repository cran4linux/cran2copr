%global __brp_check_rpaths %{nil}
%global packname  recometrics
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation Metrics for Implicit-Feedback Recommender Systems

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix >= 1.3.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-CRAN-MatrixExtra 
BuildRequires:    R-CRAN-float 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.3.4
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-MatrixExtra 
Requires:         R-CRAN-float 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-methods 

%description
Calculates evaluation metrics for implicit-feedback recommender systems
that are based on low-rank matrix factorization models, given the fitted
model matrices and data, thus allowing to compare models from a variety of
libraries. Metrics include P@K (precision-at-k, for top-K
recommendations), R@K (recall at k), AP@K (average precision at k), NDCG@K
(normalized discounted cumulative gain at k), Hit@K (from which the 'Hit
Rate' is calculated), RR@K (reciprocal rank at k, from which the 'MRR' or
'mean reciprocal rank' is calculated), ROC-AUC (area under the
receiver-operating characteristic curve), and PR-AUC (area under the
precision-recall curve). These are calculated on a per-user basis
according to the ranking of items induced by the model, using efficient
multi-threaded routines. Also provides functions for creating train-test
splits for model fitting and evaluation.

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
