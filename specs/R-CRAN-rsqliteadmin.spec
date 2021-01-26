%global packname  rsqliteadmin
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A GUI to Manage SQLite Databases

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-golem 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-shinyjqui 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-disk.frame 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-config 
Requires:         R-CRAN-golem 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-shinyjqui 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-disk.frame 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 

%description
A comprehensive tool written in R Shiny to explore, manage and update
SQLite Databases.

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
