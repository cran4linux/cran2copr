%global packname  cgmanalysis
%global packver   2.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.1
Release:          1%{?dist}
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
continuous glucose monitor data. Currently it works with 'Dexcom'
(<https://www.dexcom.com>), 'iPro 2'
(<http://professional.medtronicdiabetes.com/ipro2-professional-cgm>),
Diasend (<https://diasend.com//us>), Libre
(<https://www.freestylelibre.us/>) or Carelink
(<https://www.medtronicdiabetes.com/products/carelink-personal-diabetes-software>)
data. The cleandata() function takes a directory of CGM data files and
prepares them for analysis. cgmvariables() iterates through a directory of
cleaned CGM data files and produces a single spreadsheet with data for
each file in either rows or columns. The column format of this spreadsheet
is compatible with REDCap data upload ("--1" is added to each subject ID
automatically for double data entry). cgmreport() also iterates through a
directory of cleaned data, and produces PDFs of individual and aggregate
AGP plots. Please visit
<https://github.com/childhealthbiostatscore/R-Packages/> to download the
new-user guide.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
