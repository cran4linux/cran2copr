%global __brp_check_rpaths %{nil}
%global packname  PSweight
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Propensity Score Weighting for Causal Inference with Observational Studies and Randomized Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-SuperLearner 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-SuperLearner 

%description
Supports propensity score weighting analysis of observational studies and
randomized trials. Enables the estimation and inference of average causal
effects with binary and multiple treatments using overlap weights (ATO),
inverse probability of treatment weights (ATE), average treatment effect
among the treated weights (ATT), matching weights (ATM) and entropy
weights (ATEN), with and without propensity score trimming. These weights
are members of the family of balancing weights introduced in Li, Morgan
and Zaslavsky (2018) <doi:10.1080/01621459.2016.1260466> and Li and Li
(2019) <doi:10.1214/19-AOAS1282>.

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
