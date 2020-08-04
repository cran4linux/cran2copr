%global packname  safedata
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Interface to Data from the SAFE Project

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-igraph 

%description
The SAFE Project (<https://www.safeproject.net/>) is a large scale
ecological experiment in Malaysian Borneo that explores the impact of
habitat fragmentation and conversion on ecosystem function and services.
Data collected at the SAFE Project is made available under a common format
through the Zenodo data repository and this package makes it easy to
discover and load that data into R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
