%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easysurv
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simplify Survival Data Analysis and Model Fitting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggsurvfit >= 1.2.0
BuildRequires:    R-CRAN-bshazard 
BuildRequires:    R-CRAN-censored 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-flexsurvcure 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggsurvfit >= 1.2.0
Requires:         R-CRAN-bshazard 
Requires:         R-CRAN-censored 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-flexsurvcure 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-usethis 
Requires:         R-utils 

%description
Inspect survival data, plot Kaplan-Meier curves, assess the proportional
hazards assumption, fit parametric survival models, predict and plot
survival and hazards, and export the outputs to 'Excel'.  A simple
interface for fitting survival models using flexsurv::flexsurvreg(),
flexsurv::flexsurvspline(), flexsurvcure::flexsurvcure(), and
survival::survreg().

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
