%global __brp_check_rpaths %{nil}
%global packname  autoReg
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Linear and Logistic Regression and Survival Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-moonBook >= 0.3.0
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidycmprsk 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-maxstat 
BuildRequires:    R-CRAN-pammtools 
Requires:         R-CRAN-moonBook >= 0.3.0
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidycmprsk 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-maxstat 
Requires:         R-CRAN-pammtools 

%description
Make summary tables for descriptive statistics and select explanatory
variables automatically in various regression models. Support linear
models, generalized linear models and cox-proportional hazard models.
Generate publication-ready tables summarizing result of regression
analysis and plots. The tables and plots can be exported in "HTML",
"pdf('LaTex')", "docx('MS Word')" and "pptx('MS Powerpoint')" documents.

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
