%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ollamar
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Ollama' Language Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 

%description
An interface to easily run local language models with 'Ollama'
<https://ollama.com> server and API endpoints (see
<https://github.com/ollama/ollama/blob/main/docs/api.md> for details). It
lets you run open-source large language models locally on your machine.

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
