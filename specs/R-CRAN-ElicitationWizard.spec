%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ElicitationWizard
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          LLM-Based Bayesian Prior Elicitation Wizard

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-ellmer 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-commonmark 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-ellmer 
Requires:         R-CRAN-future 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-commonmark 

%description
'Shiny' application for eliciting Bayesian prior distributions using large
language models (LLMs). Supports multiple LLM experts, linear opinion
pooling, and the Delphi method for iterative consensus. For more details
see J. R. Falconer et al. (2022) <doi:10.1287/deca.2022.0451> and D. Selby
et al. (2025) <doi:10.1002/sta4.70054>.

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
