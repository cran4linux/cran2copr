%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mrIML
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Response (Multivariate) Interpretable Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-flashlight 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-MetricsWeighted 
BuildRequires:    R-CRAN-finetune 
BuildRequires:    R-CRAN-hstats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-flashlight 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-MetricsWeighted 
Requires:         R-CRAN-finetune 
Requires:         R-CRAN-hstats 

%description
Builds and interprets multi-response machine learning models using
'tidymodels' syntax. Users can supply a tidy model, and 'mrIML' automates
the process of fitting multiple response models to multivariate data and
applying interpretable machine learning techniques across them. For more
details see Fountain-Jones (2021) <doi:10.1111/1755-0998.13495> and
Fountain-Jones et al. (2024) <doi:10.22541/au.172676147.77148600/v1>.

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
