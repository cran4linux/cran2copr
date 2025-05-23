%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chatLLM
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Flexible Interface for 'LLM' API Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.7.2
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-stats 
Requires:         R-CRAN-jsonlite >= 1.7.2
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-stats 

%description
Provides a flexible interface for interacting with Large Language Model
('LLM') providers including 'OpenAI', 'Groq', 'Anthropic', 'DeepSeek',
'DashScope', and 'GitHub Models'. Supports both synchronous and
asynchronous chat-completion APIs, with features such as retry logic,
dynamic model selection, customizable parameters, and multi-message
conversation handling. Designed to streamline integration with
state-of-the-art LLM services across multiple platforms.

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
