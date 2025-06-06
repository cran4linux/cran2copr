%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  officer
%global packver   0.6.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.10
Release:          1%{?dist}%{?buildtag}
Summary:          Manipulation of Microsoft Word and PowerPoint Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.1.0
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-zip >= 2.1.0
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ragg 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
Access and manipulate 'Microsoft Word', 'RTF' and 'Microsoft PowerPoint'
documents from R.  The package focuses on tabular and graphical reporting
from R; it also provides two functions that let users get document content
into data objects. A set of functions lets add and remove images, tables
and paragraphs of text in new or existing documents.  The package does not
require any installation of Microsoft products to be able to write
Microsoft files.

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
