%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stacks
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Model Stacking

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-parsnip >= 1.2.0
BuildRequires:    R-CRAN-rsample >= 1.2.0
BuildRequires:    R-CRAN-tune >= 1.2.0
BuildRequires:    R-CRAN-workflows >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-recipes >= 1.0.10
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.6.1
BuildRequires:    R-CRAN-butcher >= 0.1.3
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-parsnip >= 1.2.0
Requires:         R-CRAN-rsample >= 1.2.0
Requires:         R-CRAN-tune >= 1.2.0
Requires:         R-CRAN-workflows >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-recipes >= 1.0.10
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.6.1
Requires:         R-CRAN-butcher >= 0.1.3
Requires:         R-CRAN-cli 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glue 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Model stacking is an ensemble technique that involves training a model to
combine the outputs of many diverse statistical models, and has been shown
to improve predictive performance in a variety of settings. 'stacks'
implements a grammar for 'tidymodels'-aligned model stacking.

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
