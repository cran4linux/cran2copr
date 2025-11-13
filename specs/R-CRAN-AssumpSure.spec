%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AssumpSure
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Application for Statistical Test Assumption Checking and Guidance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.65
BuildRequires:    R-CRAN-nnet >= 7.3.20
BuildRequires:    R-CRAN-MVN >= 6.1
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-car >= 3.1.3
BuildRequires:    R-CRAN-lmerTest >= 3.1.3
BuildRequires:    R-CRAN-sjPlot >= 2.9.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-compositions >= 2.0.8
BuildRequires:    R-CRAN-tidyverse >= 2.0.0
BuildRequires:    R-CRAN-bestNormalize >= 1.9.1
BuildRequires:    R-CRAN-knitr >= 1.50
BuildRequires:    R-CRAN-coin >= 1.4.3
BuildRequires:    R-CRAN-kableExtra >= 1.4.0
BuildRequires:    R-CRAN-patchwork >= 1.3.1
BuildRequires:    R-CRAN-shiny >= 1.11.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-lme4 >= 1.1.37
BuildRequires:    R-CRAN-glmmTMB >= 1.1.11
BuildRequires:    R-CRAN-broom >= 1.0.8
BuildRequires:    R-CRAN-effectsize >= 1.0.1
BuildRequires:    R-CRAN-brglm2 >= 0.9.2
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-correlation >= 0.8.8
BuildRequires:    R-CRAN-rstatix >= 0.7.2
BuildRequires:    R-CRAN-shinyBS >= 0.61.1
BuildRequires:    R-CRAN-ggpubr >= 0.6.1
BuildRequires:    R-CRAN-htmltools >= 0.5.8.1
BuildRequires:    R-CRAN-fontawesome >= 0.5.3
BuildRequires:    R-CRAN-DHARMa >= 0.4.7
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-CRAN-broom.mixed >= 0.2.9.6
BuildRequires:    R-CRAN-performance >= 0.15.0
BuildRequires:    R-CRAN-modelbased >= 0.12.0
BuildRequires:    R-CRAN-see >= 0.11.0
BuildRequires:    R-CRAN-shinyscreenshot 
Requires:         R-CRAN-MASS >= 7.3.65
Requires:         R-CRAN-nnet >= 7.3.20
Requires:         R-CRAN-MVN >= 6.1
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-car >= 3.1.3
Requires:         R-CRAN-lmerTest >= 3.1.3
Requires:         R-CRAN-sjPlot >= 2.9.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-compositions >= 2.0.8
Requires:         R-CRAN-tidyverse >= 2.0.0
Requires:         R-CRAN-bestNormalize >= 1.9.1
Requires:         R-CRAN-knitr >= 1.50
Requires:         R-CRAN-coin >= 1.4.3
Requires:         R-CRAN-kableExtra >= 1.4.0
Requires:         R-CRAN-patchwork >= 1.3.1
Requires:         R-CRAN-shiny >= 1.11.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-lme4 >= 1.1.37
Requires:         R-CRAN-glmmTMB >= 1.1.11
Requires:         R-CRAN-broom >= 1.0.8
Requires:         R-CRAN-effectsize >= 1.0.1
Requires:         R-CRAN-brglm2 >= 0.9.2
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-correlation >= 0.8.8
Requires:         R-CRAN-rstatix >= 0.7.2
Requires:         R-CRAN-shinyBS >= 0.61.1
Requires:         R-CRAN-ggpubr >= 0.6.1
Requires:         R-CRAN-htmltools >= 0.5.8.1
Requires:         R-CRAN-fontawesome >= 0.5.3
Requires:         R-CRAN-DHARMa >= 0.4.7
Requires:         R-CRAN-DT >= 0.33
Requires:         R-CRAN-broom.mixed >= 0.2.9.6
Requires:         R-CRAN-performance >= 0.15.0
Requires:         R-CRAN-modelbased >= 0.12.0
Requires:         R-CRAN-see >= 0.11.0
Requires:         R-CRAN-shinyscreenshot 

%description
A 'shiny' application to assess statistical assumptions and guide users
toward appropriate tests. The app is designed for researchers with minimal
statistical training and provides diagnostics, plots, and test
recommendations for a wide range of analyses. Many statistical assumptions
are implemented using the package 'rstatix' (Kassambara, 2019)
<doi:10.32614/CRAN.package.rstatix> and 'performance' (Lüdecke et al.,
2021) <doi:10.21105/joss.03139>.

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
