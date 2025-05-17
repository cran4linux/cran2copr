%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinychat
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Chat UI Component for 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-promises >= 1.3.2
BuildRequires:    R-CRAN-shiny >= 1.10.0
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-ellmer 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-promises >= 1.3.2
Requires:         R-CRAN-shiny >= 1.10.0
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-ellmer 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 

%description
Provides a scrolling chat interface with multiline input, suitable for
creating chatbot apps based on Large Language Models (LLMs). Designed to
work particularly well with the 'ellmer' R package for calling LLMs.

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
