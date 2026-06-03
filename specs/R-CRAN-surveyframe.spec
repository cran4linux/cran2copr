%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveyframe
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Instrument Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openssl >= 2.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-openssl >= 2.1.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-rlang >= 1.1.0

%description
Supports survey research workflows built around a typed instrument object
(the sframe). Features include visual instrument design via a
browser-based builder or 'Shiny' studio, export to a self-contained static
HTML survey, an embeddable 'Shiny' module, SHA-256 integrity-checked
serialisation to the '.sframe' format, multi-page survey rendering,
branching logic, response quality checking, scale scoring, psychometric
diagnostics, analysis-plan execution, model syntax planning, an
interactive response dashboard, codebook generation, and reproducible HTML
reporting.

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
