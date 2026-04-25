%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  toolero
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Research Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-yaml 

%description
Provides utility functions to help researchers implement best practices
for their coding projects. Includes tools for reading and cleaning data
files, initializing R projects with a standard folder structure, creating
Quarto documents from a reproducible template, detecting the execution
context across interactive, Quarto, and script-based workflows, and
splitting data frames into group-level output files.

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
