%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PEAXAI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Efficiency Analysis Using Explainable Artificial Intelligence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Benchmarking 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-deaR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastshap 
BuildRequires:    R-CRAN-iml 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-rminer 
BuildRequires:    R-stats 
Requires:         R-CRAN-Benchmarking 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-deaR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastshap 
Requires:         R-CRAN-iml 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-rminer 
Requires:         R-stats 

%description
Provides a probabilistic framework that integrates Data Envelopment
Analysis (DEA) (Banker et al., 1984) <doi:10.1287/mnsc.30.9.1078> with
machine learning classifiers (Kuhn, 2008) <doi:10.18637/jss.v028.i05> to
estimate both the (in)efficiency status and the probability of efficiency
for decision-making units. The approach trains predictive models on
DEA-derived efficiency labels (Charnes et al., 1985)
<doi:10.1016/0304-4076(85)90133-2>, enabling explainable artificial
intelligence (XAI) workflows with global and local interpretability tools,
including permutation importance (Molnar et al., 2018)
<doi:10.21105/joss.00786>, Shapley value explanations (Strumbelj &
Kononenko, 2014) <doi:10.1007/s10115-013-0679-x>, and sensitivity analysis
(Cortez, 2011) <https://CRAN.R-project.org/package=rminer>. The framework
also supports probability-threshold peer selection and counterfactual
improvement recommendations for benchmarking and policy evaluation. The
probabilistic efficiency framework is detailed in González-Moyano et al.
(2025) "Probability-based Technical Efficiency Analysis through Machine
Learning", in review for publication.

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
