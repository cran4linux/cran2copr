%global packname  incadata
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}
Summary:          Recognize and Handle Data in Formats Used by Swedish CancerCenters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-decoder 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-sweidnumbr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-decoder 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-sweidnumbr 
Requires:         R-CRAN-xml2 

%description
Handle data in formats used by cancer centers in Sweden, both from 'INCA'
(<https://rcc.incanet.se>) and by the older register platform 'Rockan'.
All variables are coerced to suitable classes based on their format. Dates
(from various formats such as with missing month or day, with or without
century prefix or with just a week number) are all recognized as dates and
coerced to the ISO 8601 standard (Y-m-d). Boolean variables (internally
stored either as 0/1 or "True"/"False"/blanks when exported) are coerced
to logical. Variable names ending in '_Beskrivning' and '_Varde' will be
character, and 'PERSNR' will be coerced (if possible) to a valid personal
identification number 'pin' (by the 'sweidnumbr' package). The package
also allow the user to interactively choose if a variable should be
coerced into a potential format even though not all of its values might
conform to the recognized pattern. It also contain a caching mechanism in
order to temporarily store data sets with its newly decided formats in
order to not rerun the identification process each time. The package also
include a mechanism to aid the documentation process connected to projects
build on data from 'INCA'. From version 0.7, some general help functions
are also included, as previously found in the 'rccmisc' package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
