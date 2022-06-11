%global __brp_check_rpaths %{nil}
%global packname  dataone
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to the DataONE REST API

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.95.0.1
BuildRequires:    R-CRAN-datapack >= 1.4.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-parsedate 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-XML >= 3.95.0.1
Requires:         R-CRAN-datapack >= 1.4.0
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-parsedate 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 

%description
Provides read and write access to data and metadata from the DataONE
network <https://www.dataone.org> of data repositories. Each DataONE
repository implements a consistent repository application programming
interface. Users call methods in R to access these remote repository
functions, such as methods to query the metadata catalog, get access to
metadata for particular data packages, and read the data objects from the
data repository. Users can also insert and update data objects on
repositories that support these methods.

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
