%global __brp_check_rpaths %{nil}
%global packname  vegdata
%global packver   0.9.11.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.11.3
Release:          1%{?dist}%{?buildtag}
Summary:          Access Vegetation Databases and Treat Taxonomy

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-CRAN-RSQLite >= 1.1.2
BuildRequires:    R-CRAN-dbplyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-DBI >= 0.6.1
BuildRequires:    R-CRAN-hoardr >= 0.1.0
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-indicspecies 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-curl >= 2.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-RSQLite >= 1.1.2
Requires:         R-CRAN-dbplyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-DBI >= 0.6.1
Requires:         R-CRAN-hoardr >= 0.1.0
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-indicspecies 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 

%description
Handling of vegetation data from different sources ( Turboveg 2.0
<https://www.synbiosys.alterra.nl/turboveg/>; the German national
repository <https://www.vegetweb.de> and others. Taxonomic harmonization
(given appropriate taxonomic lists, e.g. the German taxonomic standard
list "GermanSL", <https://germansl.infinitenature.org>).

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
