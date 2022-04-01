%global __brp_check_rpaths %{nil}
%global packname  bnlearn
%global packver   4.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Network Structure Learning, Parameter Learning and Inference

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Bayesian network structure learning, parameter learning and inference.
This package implements constraint-based (PC, GS, IAMB, Inter-IAMB,
Fast-IAMB, MMPC, Hiton-PC, HPC), pairwise (ARACNE and Chow-Liu),
score-based (Hill-Climbing and Tabu Search) and hybrid (MMHC, RSMAX2,
H2PC) structure learning algorithms for discrete, Gaussian and conditional
Gaussian networks, along with many score functions and conditional
independence tests. The Naive Bayes and the Tree-Augmented Naive Bayes
(TAN) classifiers are also implemented. Some utility functions (model
comparison and manipulation, random data generation, arc orientation
testing, simple and advanced plots) are included, as well as support for
parameter estimation (maximum likelihood and Bayesian) and inference,
conditional probability queries, cross-validation, bootstrap and model
averaging. Development snapshots with the latest bugfixes are available
from <https://www.bnlearn.com/>.

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
