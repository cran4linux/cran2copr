%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rirods
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Client for 'iRODS'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-httr2 >= 0.2.2
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-httr2 >= 0.2.2
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-base64enc 
Requires:         R-methods 
Requires:         R-CRAN-rappdirs 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
The open sourced data management software 'Integrated Rule-Oriented Data
System' ('iRODS') offers solutions for the whole data life cycle
(<https://irods.org/>). The loosely constructed and highly configurable
architecture of 'iRODS' frees the user from strict formatting constraints
and single-vendor solutions. This package provides an interface to the
'iRODS' REST API, allowing you to manage your data and metadata in 'iRODS'
with R. Storage of annotated files and R objects in 'iRODS' ensures
findability, accessibility, interoperability, and reusability of data.

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
