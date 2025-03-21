%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  questionr
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Make Surveys Processing Easier

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       xclip
BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-labelled >= 2.6.0
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-styler 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-labelled >= 2.6.0
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-styler 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-htmltools 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Set of functions to make the processing and analysis of surveys easier :
interactive shiny apps and addins for data recoding, contingency tables,
dataset metadata handling, and several convenience functions.

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
