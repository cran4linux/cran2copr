%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAIHDA
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Analysis of Individual Heterogeneity and Discriminatory Accuracy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-lme4 >= 1.1.27
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-lme4 >= 1.1.27
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-stats 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tibble 

%description
Tools for Multilevel Analysis of Individual Heterogeneity and
Discriminatory Accuracy (MAIHDA) for intersectional inequality research.
Methods are described in Merlo (2018)
<doi:10.1016/j.socscimed.2017.12.026> and Evans et al. (2018)
<doi:10.1016/j.socscimed.2017.11.011>. The package creates intersectional
strata, fits multilevel MAIHDA models, estimates variance partition
coefficients, proportional change in variance, stratum effects, and
discriminatory-accuracy summaries, and provides diagnostic and
presentation plots.

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
