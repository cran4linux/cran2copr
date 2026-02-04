%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vismi
%global packver   0.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Visual Diagnostics for Multiple Imputation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-mixgb >= 2.2.3
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-trelliscopejs 
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-mixgb >= 2.2.3
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-trelliscopejs 

%description
A comprehensive suite of static and interactive visual diagnostics for
assessing the quality of multiply-imputed data obtained from packages such
as 'mixgb' and 'mice'. The package supports inspection of distributional
characteristics, diagnostics based on masking observed values and
comparing them with re-imputed values, and convergence diagnostics.

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
