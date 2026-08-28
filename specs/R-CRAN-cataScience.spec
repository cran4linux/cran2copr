%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cataScience
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Training App for Data Science and AI Skills

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.8.1
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-bslib >= 0.6.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-naniar 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-VIM 
Requires:         R-CRAN-shiny >= 1.8.1
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-bslib >= 0.6.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-naniar 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-skimr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-VIM 

%description
An interactive 'shiny' training companion for people who are new to data,
developed for World Health Organization data trainings. Bundles hands-on
modules for importing data, missing values, outliers, text cleaning,
merging, visualization, and basic statistics, plus a set of AI-skills
pages (prompting levels, a prompt gallery, AI safety rules, and a
methodology case study) and an interactive quiz with per-session topic
filters. Launch the app with run_cata().

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
