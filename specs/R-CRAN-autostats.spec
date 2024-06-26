%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autostats
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Auto Stats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggeasy 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jtools 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-framecleaner 
BuildRequires:    R-CRAN-presenter 
BuildRequires:    R-CRAN-yardstick 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-recosystem 
BuildRequires:    R-CRAN-Ckmeans.1d.dp 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggeasy 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jtools 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-framecleaner 
Requires:         R-CRAN-presenter 
Requires:         R-CRAN-yardstick 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-party 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-recosystem 
Requires:         R-CRAN-Ckmeans.1d.dp 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-igraph 

%description
Automatically do statistical exploration. Create formulas using
'tidyselect' syntax, and then determine cross-validated model accuracy and
variable contributions using 'glm' and 'xgboost'. Contains additional
helper functions to create and modify formulas. Has a flagship function to
quickly determine relationships between categorical and continuous
variables in the data set.

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
