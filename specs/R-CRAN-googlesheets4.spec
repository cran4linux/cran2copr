%global packname  googlesheets4
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Access Google Sheets using the Sheets API V4

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-googledrive >= 1.0.0
BuildRequires:    R-CRAN-gargle >= 0.4.0
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-googledrive >= 1.0.0
Requires:         R-CRAN-gargle >= 0.4.0
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Interact with Google Sheets through the Sheets API v4
<https://developers.google.com/sheets/api>. "API" is an acronym for
"application programming interface"; the Sheets API allows users to
interact with Google Sheets programmatically, instead of via a web
browser. The "v4" refers to the fact that the Sheets API is currently at
version 4. This package helps the user to retrieve Sheet metadata and to
read data out of specific worksheets or ranges into an R object, such as a
data frame.

%prep
%setup -q -c -n %{packname}


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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/secret
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
