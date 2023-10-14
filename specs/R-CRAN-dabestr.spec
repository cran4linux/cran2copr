%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dabestr
%global packver   2023.9.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2023.9.12
Release:          1%{?dist}%{?buildtag}
Summary:          Data Analysis using Bootstrap-Coupled Estimation

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggbeeswarm 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-brunnermunzel 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggbeeswarm 
Requires:         R-CRAN-effsize 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggsci 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-brunnermunzel 
Requires:         R-methods 

%description
Data Analysis using Bootstrap-Coupled ESTimation. Estimation statistics is
a simple framework that avoids the pitfalls of significance testing. It
uses familiar statistical concepts: means, mean differences, and error
bars. More importantly, it focuses on the effect size of one's
experiment/intervention, as opposed to a false dichotomy engendered by P
values. An estimation plot has two key features: 1. It presents all
datapoints as a swarmplot, which orders each point to display the
underlying distribution. 2. It presents the effect size as a bootstrap 95%%
confidence interval on a separate but aligned axes. Estimation plots are
introduced in Ho et al., Nature Methods 2019, 1548-7105.
<doi:10.1038/s41592-019-0470-3>. The free-to-view PDF is located at
<https://www.nature.com/articles/s41592-019-0470-3.epdf?author_access_token=Euy6APITxsYA3huBKOFBvNRgN0jAjWel9jnR3ZoTv0Pr6zJiJ3AA5aH4989gOJS_dajtNr1Wt17D0fh-t4GFcvqwMYN03qb8C33na_UrCUcGrt-Z0J9aPL6TPSbOxIC-pbHWKUDo2XsUOr3hQmlRew%%3D%%3D>.

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
