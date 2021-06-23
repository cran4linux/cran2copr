%global __brp_check_rpaths %{nil}
%global packname  ImportExport
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Import and Export Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-utils 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-haven 
Requires:         R-utils 

%description
Import and export data from the most common statistical formats by using R
functions that guarantee the least loss of the data information, giving
special attention to the date variables and the labelled ones.

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
