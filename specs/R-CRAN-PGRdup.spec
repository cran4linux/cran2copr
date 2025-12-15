%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PGRdup
%global packver   0.2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discover Probable Duplicates in Plant Genetic Resources Collections

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-data.table >= 1.9.3
BuildRequires:    R-CRAN-stringdist >= 0.9.4
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.9.3
Requires:         R-CRAN-stringdist >= 0.9.4
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides functions to aid the identification of probable/possible
duplicates in Plant Genetic Resources (PGR) collections using 'passport
databases' comprising of information records of each constituent sample.
These include methods for cleaning the data, creation of a searchable Key
Word in Context (KWIC) index of keywords associated with sample records
and the identification of nearly identical records with similar
information by fuzzy, phonetic and semantic matching of keywords.

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
