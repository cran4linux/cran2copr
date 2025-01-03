%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CRE
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Discovery and Inference of Heterogeneous Treatment Effects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-RRF 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-bartCause 
BuildRequires:    R-CRAN-stabs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-arules 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-randomForest 
Requires:         R-methods 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-RRF 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-bartCause 
Requires:         R-CRAN-stabs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-arules 

%description
Provides a new method for interpretable heterogeneous treatment effects
characterization in terms of decision rules via an extensive exploration
of heterogeneity patterns by an ensemble-of-trees approach, enforcing high
stability in the discovery. It relies on a two-stage pseudo-outcome
regression, and it is supported by theoretical convergence guarantees.
Bargagli-Stoffi, F. J., Cadei, R., Lee, K., & Dominici, F. (2023) Causal
rule ensemble: Interpretable Discovery and Inference of Heterogeneous
Treatment Effects. arXiv preprint <doi:10.48550/arXiv.2009.09036>.

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
