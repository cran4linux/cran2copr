%global __brp_check_rpaths %{nil}
%global packname  CIMTx
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference for Multiple Treatments with a Binary Outcome

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-twang 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Matching 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-WeightIt 
BuildRequires:    R-CRAN-tmle 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-twang 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Matching 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-WeightIt 
Requires:         R-CRAN-tmle 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-metR 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Different methods to conduct causal inference for multiple treatments with
a binary outcome, including regression adjustment, vector matching,
Bayesian additive regression trees, targeted maximum likelihood and
inverse probability of treatment weighting using different generalized
propensity score models such as multinomial logistic regression,
generalized boosted models and super learner. For more details, see the
paper by Hu et al. <doi:10.1177/0962280220921909>.

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
