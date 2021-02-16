%global packname  cgmanalysis
%global packver   2.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clean and Analyze Continuous Glucose Monitor Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-pastecs 
Requires:         R-tools 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-XML 

%description
This code provides several different functions for cleaning and analyzing
continuous glucose monitor data. Currently it works with 'Dexcom', 'iPro
2', 'Diasend', 'Libre', or 'Carelink' data. The cleandata() function takes
a directory of CGM data files and prepares them for analysis.
cgmvariables() iterates through a directory of cleaned CGM data files and
produces a single spreadsheet with data for each file in either rows or
columns. The column format of this spreadsheet is compatible with REDCap
data upload. cgmreport() also iterates through a directory of cleaned
data, and produces PDFs of individual and aggregate AGP plots. Please
visit <https://github.com/childhealthbiostatscore/R-Packages/> to download
the new-user guide.

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
