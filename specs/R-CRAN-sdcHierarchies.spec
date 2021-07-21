%global __brp_check_rpaths %{nil}
%global packname  sdcHierarchies
%global packver   0.19.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.19.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create and (Interactively) Modify Nested Hierarchies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyTree 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyTree 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-Rcpp 

%description
Provides functionality to generate, (interactively) modify (by adding,
removing and renaming nodes) and convert nested hierarchies between
different formats. These tree like structures can be used to define for
example complex hierarchical tables used for statistical disclosure
control.

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
