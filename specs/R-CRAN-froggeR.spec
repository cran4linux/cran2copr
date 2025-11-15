%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  froggeR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enhance 'Quarto' Project Workflows and Standards

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-usethis >= 2.2.0
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.6.0
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-quarto >= 1.3.0
BuildRequires:    R-CRAN-here >= 1.0.1
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-usethis >= 2.2.0
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-glue >= 1.6.0
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-quarto >= 1.3.0
Requires:         R-CRAN-here >= 1.0.1
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-yaml 

%description
Streamlines 'Quarto' workflows by providing tools for consistent project
setup and documentation. Enables portability through reusable metadata,
automated project structure creation, and standardized templates. Features
include enhanced project initialization, pre-formatted 'Quarto' documents,
inclusion of 'Quarto' brand functionality, comprehensive data protection
settings, custom styling, and structured documentation generation.
Designed to improve efficiency and collaboration in R data science
projects by reducing repetitive setup tasks while maintaining consistent
formatting across multiple documents.

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
