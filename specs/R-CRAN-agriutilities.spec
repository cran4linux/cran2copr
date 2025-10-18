%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agriutilities
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Data Analysis in Agriculture

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-statgenSTA 
BuildRequires:    R-CRAN-SpATS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-statgenSTA 
Requires:         R-CRAN-SpATS 

%description
Utilities designed to make the analysis of field trials easier and more
accessible for everyone working in plant breeding. It provides a simple
and intuitive interface for conducting single and multi-environmental
trial analysis, with minimal coding required. Whether you're a beginner or
an experienced user, 'agriutilities' will help you quickly and easily
carry out complex analyses with confidence. With built-in functions for
fitting Linear Mixed Models, 'agriutilities' is the ideal choice for
anyone who wants to save time and focus on interpreting their results.
Some of the functions require the R package 'asreml' for the 'ASReml'
software, this can be obtained upon purchase from 'VSN' international
<https://vsni.co.uk/software/asreml-r/>.

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
