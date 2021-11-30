%global __brp_check_rpaths %{nil}
%global packname  CIMTx
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference for Multiple Treatments with a Binary Outcome

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3.16
BuildRequires:    R-CRAN-Matching >= 4.9.11
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-BART >= 2.9
BuildRequires:    R-CRAN-twang >= 2.5
BuildRequires:    R-CRAN-SuperLearner >= 2.0.28
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-mgcv >= 1.8.38
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-tmle >= 1.5.0.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-arm >= 1.2.12
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-doParallel >= 1.0.16
BuildRequires:    R-CRAN-WeightIt >= 0.12.0
BuildRequires:    R-CRAN-metR >= 0.11.0
BuildRequires:    R-stats 
Requires:         R-CRAN-nnet >= 7.3.16
Requires:         R-CRAN-Matching >= 4.9.11
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-BART >= 2.9
Requires:         R-CRAN-twang >= 2.5
Requires:         R-CRAN-SuperLearner >= 2.0.28
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-mgcv >= 1.8.38
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-tmle >= 1.5.0.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-arm >= 1.2.12
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-doParallel >= 1.0.16
Requires:         R-CRAN-WeightIt >= 0.12.0
Requires:         R-CRAN-metR >= 0.11.0
Requires:         R-stats 

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
