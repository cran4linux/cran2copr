%global packname  htmltab
%global packver   0.7.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1.1
Release:          3%{?dist}
Summary:          Assemble Data Frames from HTML Tables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.3
BuildRequires:    R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-XML >= 3.98.1.3
Requires:         R-CRAN-httr >= 1.0.0

%description
HTML tables are a valuable data source but extracting and recasting these
data into a useful format can be tedious. This package allows to collect
structured information from HTML tables. It is similar to readHTMLTable()
of the XML package but provides three major advantages. First, the
function automatically expands row and column spans in the header and body
cells. Second, users are given more control over the identification of
header and body rows which will end up in the R table, including semantic
header information that appear throughout the body. Third, the function
preprocesses table code, corrects common types of malformations, removes
unneeded parts and so helps to alleviate the need for tedious
post-processing.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
