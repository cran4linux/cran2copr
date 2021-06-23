%global __brp_check_rpaths %{nil}
%global packname  multiverse
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Explorable Multiverse' Data Analysis and Reports

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.3
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.1
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.2
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-collections 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-berryFunctions 
Requires:         R-CRAN-knitr >= 1.3
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.1
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.2
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-collections 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-berryFunctions 

%description
Implement 'multiverse' style analyses (Steegen S., Tuerlinckx F, Gelman
A., Vanpaemal, W., 2016) <doi:10.1177/1745691616658637>, (Dragicevic P.,
Jansen Y., Sarma A., Kay M., Chevalier F., 2019)
<doi:10.1145/3290605.3300295> to show the robustness of statistical
inference. 'Multiverse analysis' is a philosophy of statistical reporting
where paper authors report the outcomes of many different statistical
analyses in order to show how fragile or robust their findings are. The
'multiverse' package (Sarma A., Kale A., Moon M., Taback N., Chevalier F.,
Hullman J., Kay M., 2021) <doi:10.31219/osf.io/yfbwm> allows users to
concisely and flexibly implement 'multiverse-style' analysis, which
involve declaring alternate ways of performing an analysis step, in R and
R Notebooks.

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
