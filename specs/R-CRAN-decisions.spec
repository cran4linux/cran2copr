%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  decisions
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Typed Decisions from Decision Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.5
BuildRequires:    R-CRAN-rlang >= 1.3.0
BuildRequires:    R-CRAN-httr2 >= 1.2.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-S7 >= 0.2.0
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-jsonlite >= 1.8.5
Requires:         R-CRAN-rlang >= 1.3.0
Requires:         R-CRAN-httr2 >= 1.2.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-S7 >= 0.2.0
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 

%description
Sends texts and images to decision models: hosted or local models that
return a probability for each allowed answer to a typed question (true or
false, a choice, or an ordered score). Supports the web services of
'TypeSafe' <https://docs.typesafe.ai/introduction>, 'OpenAI'
<https://platform.openai.com>, 'OpenRouter' <https://openrouter.ai> and
'Microsoft Foundry' <https://ai.azure.com>, which need an API (application
programming interface) key and can charge for each call, and any local or
hosted server that uses the 'SystemOne' request format. Returns one row
for each input in the 'tidymodels' style, saves and scores a complete
decision setup, and applies a calibrator fitted with 'probably'. Includes
injury reports from the Severe Injury Reports of the U.S. Occupational
Safety and Health Administration
<https://www.osha.gov/severe-injury-reports>, food recall reports of the
U.S. Food and Drug Administration
<https://open.fda.gov/apis/food/enforcement/>, and simulated textile
images made with 'spc4sts', Bui and Apley (2021)
<doi:10.1080/00224065.2019.1707730>.

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
