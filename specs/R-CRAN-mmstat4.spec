%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmstat4
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access to Teaching Materials from a ZIP File or GitHub

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-tools 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-tcltk 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringdist 
Requires:         R-tools 

%description
Provides access to teaching materials for various statistics courses,
including R and Python programs, Shiny apps, data, and PDF/HTML documents.
These materials are stored on the Internet as a ZIP file (e.g., in a
GitHub repository) and can be downloaded and displayed or run locally. The
content of the ZIP file is temporarily or permanently stored. By default,
the package uses the GitHub repository 'sigbertklinke/mmstat4.data.'
Additionally, the package includes 'association_measures.R' from the
archived package 'ryouready' by Mark Heckman and some auxiliary functions.

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
