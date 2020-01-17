%global packname  LexisNexisTools
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Working with Files from 'LexisNexis'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3.0
BuildRequires:    R-parallel >= 3.3.0
BuildRequires:    R-stats >= 3.3.0
BuildRequires:    R-utils >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 1.4.0
BuildRequires:    R-CRAN-pbapply >= 1.3.4
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-stringi >= 1.1.7
BuildRequires:    R-CRAN-quanteda >= 1.1.0
BuildRequires:    R-CRAN-stringdist >= 0.9.4.0
Requires:         R-methods >= 3.3.0
Requires:         R-parallel >= 3.3.0
Requires:         R-stats >= 3.3.0
Requires:         R-utils >= 3.3.0
Requires:         R-CRAN-tibble >= 1.4.0
Requires:         R-CRAN-pbapply >= 1.3.4
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-stringi >= 1.1.7
Requires:         R-CRAN-quanteda >= 1.1.0
Requires:         R-CRAN-stringdist >= 0.9.4.0

%description
My PhD supervisor once told me that everyone doing newspaper analysis
starts by writing code to read in files from the 'LexisNexis' newspaper
archive (retrieved e.g., from <http://www.nexis.com/> or any of the
partner sites). However, while this is a nice exercise I do recommend, not
everyone has the time. This package takes TXT files downloaded from the
newspaper archive of 'LexisNexis', reads them into R and offers functions
for further processing.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
