%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pacs
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Supplementary Tools for R Packages Developers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringi 

%description
Supplementary utils for CRAN maintainers and R packages developers.
Validating the library, packages and lock files. Exploring a complexity of
a specific package like evaluating its size in bytes with all
dependencies. The shiny app complexity could be explored too. Assessing
the life duration of a specific package version. Checking a CRAN package
check page status for any errors and warnings. Retrieving a DESCRIPTION or
NAMESPACE file for any package version. Comparing DESCRIPTION or NAMESPACE
files between different package versions. Getting a list of all releases
for a specific package. The Bioconductor is partly supported.

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
