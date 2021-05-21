%global packname  sknifedatar
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Swiss Knife of Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-parsnip >= 0.1.4
BuildRequires:    R-CRAN-tune >= 0.1.3
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-rsample >= 0.0.9
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-modeltime 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-workflowsets 
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-parsnip >= 0.1.4
Requires:         R-CRAN-tune >= 0.1.3
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-rsample >= 0.0.9
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-modeltime 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-workflowsets 

%description
Extension of the 'modeltime' ecosystem. In addition. Allows fitting of
multiple models over multiple time series. It also provides a bridge for
using the 'workflowsets' package with 'modeltime'. It includes some
functionalities for spatial data and visualization.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
