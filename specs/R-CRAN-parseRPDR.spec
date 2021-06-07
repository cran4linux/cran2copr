%global packname  parseRPDR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parse and Manipulate Research Patient Data Registry ('RPDR') Text Queries

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bigmemory >= 4.5.36
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-data.table >= 1.13.2
BuildRequires:    R-CRAN-doParallel >= 1.0.16
Requires:         R-CRAN-bigmemory >= 4.5.36
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-data.table >= 1.13.2
Requires:         R-CRAN-doParallel >= 1.0.16

%description
Functions to load Research Patient Data Registry ('RPDR') text queries
from Partners Healthcare institutions into R. The package also provides
helper functions to manipulate data and execute common procedures such as
finding the closest radiological exams considering a given timepoint.
'parseRPDR' currently supports txt sources: "mrn", "con", "dem", "enc",
"rdt", "lab", "med", "dia", "rfv", "prc", "phy", "lno", "car", "dis",
"end", "hnp", "opn", "pat", "prg", "pul", "rad" and "vis". All
functionalities are parallelized for fast and efficient analyses.

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
