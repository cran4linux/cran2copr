%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidysdm
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Models with Tidymodels

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-tidymodels 
BuildRequires:    R-CRAN-spatialsample 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-DALEXtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-CRAN-workflows 
BuildRequires:    R-CRAN-workflowsets 
BuildRequires:    R-CRAN-yardstick 
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-tidymodels 
Requires:         R-CRAN-spatialsample 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-DALEXtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maxnet 
Requires:         R-methods 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tune 
Requires:         R-CRAN-workflows 
Requires:         R-CRAN-workflowsets 
Requires:         R-CRAN-yardstick 

%description
Fit species distribution models (SDMs) using the 'tidymodels' framework,
which provides a standardised interface to define models and process their
outputs. 'tidysdm' expands 'tidymodels' by providing methods for spatial
objects, models and metrics specific to SDMs, as well as a number of
specialised functions to process occurrences for contemporary and palaeo
datasets. The full functionalities of the package are described in
Leonardi et al. (2023) <doi:10.1101/2023.07.24.550358>.

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
