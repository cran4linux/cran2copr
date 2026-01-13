%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LLMTranslate
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          'shiny' App for TRAPD/ISPOR Survey Translation with LLMs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-shiny 

%description
A 'shiny' application to automate forward and back survey translation with
optional reconciliation using large language models (LLMs). Supports both
item-by-item and batch translation modes for optimal performance and
context-aware translations. Handles multi-sheet Excel files and supports
OpenAI (GPT), Google Gemini, and Anthropic Claude models. Follows the
TRAPD (Translation, Review, Adjudication, Pretesting, Documentation)
framework and ISPOR (International Society for Pharmacoeconomics and
Outcomes Research) recommendations. See Harkness et al. (2010)
<doi:10.1002/9780470609927.ch7> and Wild et al. (2005)
<doi:10.1111/j.1524-4733.2005.04054.x>.

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
