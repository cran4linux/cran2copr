%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CausalMetaR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Causally Interpretable Meta-Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-SuperLearner 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-SuperLearner 

%description
Provides robust and efficient methods for estimating causal effects in a
target population using a multi-source dataset, including those of
Dahabreh et al. (2019) <doi:10.1111/biom.13716>, Robertson et al. (2021)
<doi:10.48550/arXiv.2104.05905>, and Wang et al. (2024)
<doi:10.48550/arXiv.2402.02684>. The multi-source data can be a collection
of trials, observational studies, or a combination of both, which have the
same data structure (outcome, treatment, and covariates). The target
population can be based on an internal dataset or an external dataset
where only covariate information is available. The causal estimands
available are average treatment effects and subgroup treatment effects.
See Wang et al. (2025) <doi:10.1017/rsm.2025.5> for a detailed guide on
using the package.

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
