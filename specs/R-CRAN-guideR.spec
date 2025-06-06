%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  guideR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Statistical Functions Used in 'guide-R'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-pak 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-pak 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-srvyr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 

%description
Companion package for the manual 'guide-R : Guide pour l’analyse de
données d’enquêtes avec R' available at
<https://larmarange.github.io/guide-R/>. 'guideR' implements miscellaneous
functions introduced in 'guide-R' to facilitate statistical analysis and
manipulation of survey data.

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
