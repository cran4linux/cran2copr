%global packname  cli
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}
Summary:          Helpers for Developing Command Line Interfaces

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fansi 
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-fansi 

%description
A suite of tools to build attractive command line interfaces ('CLIs'),
from semantic elements: headings, lists, alerts, paragraphs, etc. Supports
custom themes via a 'CSS'-like language. It also contains a number of
lower level 'CLI' elements: rules, boxes, trees, and 'Unicode' symbols
with 'ASCII' alternatives. It integrates with the 'crayon' package to
support 'ANSI' terminal colors.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/logo.txt
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
