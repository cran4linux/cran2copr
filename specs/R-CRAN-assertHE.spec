%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  assertHE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisation and Verification of Health Economic Decision Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-covr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-waiter 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-covr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-roxygen2 
Requires:         R-methods 
Requires:         R-CRAN-waiter 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-httr 

%description
Designed to help health economic modellers when building and reviewing
models. The visualisation functions allow users to more easily review the
network of functions in a project, and get lay summaries of them. The
asserts included are intended to check for common errors, thereby freeing
up time for modellers to focus on tests specific to the individual model
in development or review. For more details see Smith and colleagues
(2024)<doi:10.12688/wellcomeopenres.23180.1>.

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
