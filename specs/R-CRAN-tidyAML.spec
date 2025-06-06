%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyAML
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Machine Learning with 'tidymodels'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tune >= 1.3.0
BuildRequires:    R-CRAN-workflows >= 1.1.2
BuildRequires:    R-CRAN-rsample >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.5
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-workflowsets 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tune >= 1.3.0
Requires:         R-CRAN-workflows >= 1.1.2
Requires:         R-CRAN-rsample >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.5
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-workflowsets 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 

%description
The goal of this package will be to provide a simple interface for
automatic machine learning that fits the 'tidymodels' framework. The
intention is to work for regression and classification problems with a
simple verb framework.

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
