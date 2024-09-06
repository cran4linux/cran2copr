%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmints
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Workflows for Building Web Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-shiny 

%description
Sharing statistical methods or simulation frameworks through 'shiny'
applications often requires workflows for handling data. To help save and
display simulation results, the postgresUI() and postgresServer()
functions in 'mmints' help with persistent data storage using a
'PostgreSQL' database. The 'mmints' package also offers data upload
functionality through the csvUploadUI() and csvUploadServer() functions
which allow users to upload data, view variables and their types, and edit
variable types before fitting statistical models within the 'shiny'
application. These tools aim to enhance efficiency and user interaction in
'shiny' based statistical and simulation applications.

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
