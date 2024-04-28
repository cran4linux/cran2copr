%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chattr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with Large Language Models in 'RStudio'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 1.0.1
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-httr2 >= 1.0.1
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-config 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fs 

%description
Enables user interactivity with large-language models ('LLM') inside the
'RStudio' integrated development environment (IDE). The user can interact
with the model using the 'shiny' app included in this package, or directly
in the 'R' console. It comes with back-ends for 'OpenAI', 'GitHub'
'Copilot', and 'LlamaGPT'.

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
