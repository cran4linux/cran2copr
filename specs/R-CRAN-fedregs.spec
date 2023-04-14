%global __brp_check_rpaths %{nil}
%global packname  fedregs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Text Analysis of the US Code of Federal Regulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-stringi >= 1.1.7
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-tidytext >= 0.1.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-stringi >= 1.1.7
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-tidytext >= 0.1.9

%description
The Code of Federal Regulations (CFR) annual edition is the codification
of the general and permanent rules published in the Federal Register by
the departments and agencies of the Federal Government of the United
States of America. Simply, the 'fedregs' package facilitates word
processing and sentiment analysis of the CFR using tidy principles. Note:
According to the Code of Federal Regulations XML Rendition User Guide
Document: "In general, there are no restrictions on re-use of information
in Code of Federal Regulations material because U.S. Government works are
not subject to copyright. OFR and GPO do not restrict downstream uses of
Code of Federal Regulations data, except that independent providers should
be aware that only the OFR and GPO are entitled to represent that they are
the providers of the official versions of the Code of Federal Regulations
and related Federal Register publications."

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
