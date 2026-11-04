%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sas2r
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          1%{?dist}%{?buildtag}
Summary:          Translate 'SAS' Programs to R with Dependency-Aware Migration

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.4
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli >= 3.4
Requires:         R-CRAN-callr 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-yaml 

%description
Translates 'SAS' programs and projects into R code, orders connected
programs by their dependencies, and executes generated code. Compares
generated datasets with supplied reference outputs and reports unresolved
translation and validation findings. Rule-based translation works offline
without a 'SAS' installation. Optional language model translation, review,
and repair use a user-configured provider through 'ellmer' and may require
an account and API credentials.

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
