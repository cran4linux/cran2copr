%global __brp_check_rpaths %{nil}
%global packname  MachineShop
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Models and Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-rsample >= 0.1.0
BuildRequires:    R-CRAN-dials >= 0.0.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-rsample >= 0.1.0
Requires:         R-CRAN-dials >= 0.0.4
Requires:         R-CRAN-abind 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-party 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Meta-package for statistical and machine learning with a unified interface
for model fitting, prediction, performance assessment, and presentation of
results.  Approaches for model fitting and prediction of numerical,
categorical, or censored time-to-event outcomes include traditional
regression models, regularization methods, tree-based methods, support
vector machines, neural networks, ensembles, data preprocessing,
filtering, and model tuning and selection.  Performance metrics are
provided for model assessment and can be estimated with independent test
sets, split sampling, cross-validation, or bootstrap resampling.  Resample
estimation can be executed in parallel for faster processing and nested in
cases of model tuning and selection.  Modeling results can be summarized
with descriptive statistics; calibration curves; variable importance;
partial dependence plots; confusion matrices; and ROC, lift, and other
performance curves.

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
