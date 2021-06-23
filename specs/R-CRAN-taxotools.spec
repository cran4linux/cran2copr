%global __brp_check_rpaths %{nil}
%global packname  taxotools
%global packver   0.0.79
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.79
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Handle Taxonomic Lists

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-wikitaxa 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringdist 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-wikitaxa 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringdist 

%description
Tools include matching and merging taxonomic lists, casting and melting
scientific names, managing taxonomic lists from GBIF and ITIS, harvesting
names from wikipedia and fuzzy matching.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
