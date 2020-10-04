%global packname  fsia
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Import and Analysis of OMR Data from FormScanner

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Import data of tests and questionnaires from FormScanner. FormScanner is
an open source software that converts scanned images to data using optical
mark recognition (OMR) and it can be downloaded from
<http://sourceforge.net/projects/formscanner/>. The spreadsheet file
created by FormScanner is imported in a convenient format to perform the
analyses provided by the package. These analyses include the conversion of
multiple responses to binary (correct/incorrect) data, the computation of
the number of corrected responses for each subject or item, scoring using
weights,the computation and the graphical representation of the
frequencies of the responses to each item and the report of the responses
of a few subjects.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
