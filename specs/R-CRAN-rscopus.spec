%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rscopus
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Scopus Database 'API' Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-tools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 

%description
Uses Elsevier 'Scopus' API <https://dev.elsevier.com/sc_apis.html> to
download information about authors and their citations.

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
