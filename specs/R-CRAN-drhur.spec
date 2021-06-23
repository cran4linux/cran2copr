%global __brp_check_rpaths %{nil}
%global packname  drhur
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Learning R with Dr. Hu

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-learnr >= 0.10.1
BuildRequires:    R-CRAN-gapminder 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-modelsummary 
BuildRequires:    R-CRAN-dotwhisker 
BuildRequires:    R-CRAN-interplot 
BuildRequires:    R-CRAN-likert 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-ggeffects 
BuildRequires:    R-CRAN-summarytools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-learnr >= 0.10.1
Requires:         R-CRAN-gapminder 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-modelsummary 
Requires:         R-CRAN-dotwhisker 
Requires:         R-CRAN-interplot 
Requires:         R-CRAN-likert 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-ggeffects 
Requires:         R-CRAN-summarytools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-car 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-kableExtra 

%description
A fast, interactive tool built upon the 'learnr' function which will open
a shiny app for learners to interact with the instructions and tasks. The
best way to learn these skills together with the “Learning R with Dr. Hu”
online/offline workshops.

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
