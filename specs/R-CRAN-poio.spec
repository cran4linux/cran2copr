%global packname  poio
%global packver   0.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}
Summary:          Input/Output Functionality for "PO" and "POT" MessageTranslation Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-assertive.base 
BuildRequires:    R-CRAN-assertive.properties 
BuildRequires:    R-CRAN-assertive.types 
BuildRequires:    R-CRAN-assertive.files 
BuildRequires:    R-CRAN-assertive.sets 
BuildRequires:    R-CRAN-assertive.strings 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whoami 
Requires:         R-CRAN-assertive.base 
Requires:         R-CRAN-assertive.properties 
Requires:         R-CRAN-assertive.types 
Requires:         R-CRAN-assertive.files 
Requires:         R-CRAN-assertive.sets 
Requires:         R-CRAN-assertive.strings 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-whoami 

%description
Read and write PO and POT files, for package translations.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
