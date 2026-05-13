%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idealstan
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Measurement with 'Stan'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-svDialogs 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-gghighlight 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidybayes 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ordbetareg 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tibble 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-svDialogs 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-gghighlight 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidybayes 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ordbetareg 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tibble 

%description
Offers item-response theory (IRT) ideal-point measurement modeling for
diverse distributions, missing data, and over-time variation. Full and
approximate Bayesian sampling with 'Stan' (<https://mc-stan.org/>).

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
