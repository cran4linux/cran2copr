%global packname  ariExtra
%global packver   0.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.11
Release:          1%{?dist}
Summary:          Tools for Creating Automated Courses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-docxtractr >= 0.6.2
BuildRequires:    R-CRAN-text2speech >= 0.2.8
BuildRequires:    R-CRAN-ari >= 0.2.3
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-docxtractr >= 0.6.2
Requires:         R-CRAN-text2speech >= 0.2.8
Requires:         R-CRAN-ari >= 0.2.3
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mime 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-yaml 

%description
Leverages the 'ari' package and other tools to create automated courses
from slides and a script.  Also, uploads these to 'YouTube' and other
services using 'tuber' package.

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
