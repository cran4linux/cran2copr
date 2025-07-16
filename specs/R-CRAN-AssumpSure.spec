%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AssumpSure
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' Application for Statistical Test Assumption Checking and Guidance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shinyscreenshot 
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-compositions 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-correlation 
BuildRequires:    R-CRAN-MVN 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-modelbased 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-see 
BuildRequires:    R-CRAN-bestNormalize 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-sjPlot 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shinyscreenshot 
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-compositions 
Requires:         R-CRAN-car 
Requires:         R-CRAN-correlation 
Requires:         R-CRAN-MVN 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-modelbased 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-see 
Requires:         R-CRAN-bestNormalize 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-sjPlot 

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
