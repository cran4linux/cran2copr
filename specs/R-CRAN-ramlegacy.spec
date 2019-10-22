%global packname  ramlegacy
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Download and Read RAM Legacy Stock Assessment Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-readxl >= 1.1.0
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-readxl >= 1.1.0
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-rappdirs >= 0.3.1

%description
Contains functions to download, cache and read in 'Excel' version of the
RAM Legacy Stock Assessment Data Base, an online compilation of stock
assessment results for commercially exploited marine populations from
around the world. The database is named after Dr. Ransom A. Myers whose
original stock-recruitment database, is no longer being updated. More
information about the database can be found at <https://ramlegacy.org/>.
Ricard, D., Minto, C., Jensen, O.P. and Baum, J.K. (2012)
<doi:10.1111/j.1467-2979.2011.00435.x>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
