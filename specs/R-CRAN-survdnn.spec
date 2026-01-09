%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survdnn
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Deep Neural Networks for Survival Analysis with R 'torch'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 

%description
Provides deep learning models for right-censored survival data using the
'torch' backend. Supports multiple loss functions, including Cox partial
likelihood, L2-penalized Cox, time-dependent Cox, and accelerated failure
time (AFT) loss. Offers a formula-based interface, built-in support for
cross-validation, hyperparameter tuning, survival curve plotting, and
evaluation metrics such as the C-index, Brier score, and integrated Brier
score. For methodological details, see Kvamme et al. (2019)
<https://www.jmlr.org/papers/v20/18-424.html>.

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
