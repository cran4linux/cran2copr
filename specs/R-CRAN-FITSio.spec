%global packname  FITSio
%global packver   2.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          FITS (Flexible Image Transport System) Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Utilities to read and write files in the FITS (Flexible Image Transport
System) format, a standard format in astronomy (see e.g.
<https://en.wikipedia.org/wiki/FITS> for more information). Present
low-level routines allow: reading, parsing, and modifying FITS headers;
reading FITS images (multi-dimensional arrays); reading FITS binary and
ASCII tables; and writing FITS images (multi-dimensional arrays).
Higher-level functions allow: reading files composed of one or more
headers and a single (perhaps multidimensional) image or single table;
reading tables into data frames; generating vectors for image array axes;
scaling and writing images as 16-bit integers.  Known incompletenesses are
reading random group extensions, as well as bit, complex, and array
descriptor data types in binary tables.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/fitsExamples
%{rlibdir}/%{packname}/INDEX
