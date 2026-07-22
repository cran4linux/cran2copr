%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tbnb
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Threshold-Based and Iterative Threshold-Based Naive Bayes Classifier

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda >= 3.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-quanteda >= 3.0
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Implements the Threshold-Based Naive Bayes (Tb-NB) classifier and its
iterative refinement (iTb-NB) for binary sentiment / text classification
problems. The classifier computes a continuous log-likelihood ratio score
per document and uses a data-driven decision threshold estimated via
K-fold cross-validation on a user-selected criterion (accuracy, F1 score,
Matthews correlation coefficient, balanced error, etc.). An optional
iterative refinement procedure locally re-estimates the threshold in
regions of class overlap using either Gaussian kernel density estimation
or a Central Limit Theorem bootstrap approximation. The package exposes an
idiomatic R formula + data.frame interface together with a
'quanteda'-based text preprocessing pipeline, supports user-supplied
document-feature matrices, and includes an optional word-embedding
extension that augments the Bag-of-Words with K nearest semantic
neighbours of each token. The package additionally implements the p-value
extension proposed by Romano (2025) for both document- and feature-level
interpretability via tbnb_pvalues(). Methods are described in Romano,
Contu, Mola, Conversano (2024) <doi:10.1007/s11634-023-00536-8>, Romano,
Zammarchi, Conversano (2024) <doi:10.1007/s10260-023-00721-1>, and Romano
(2025) <doi:10.1007/978-3-031-96736-8_41>.

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
