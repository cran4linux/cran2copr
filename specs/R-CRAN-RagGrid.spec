%global packname  RagGrid
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          A Wrapper of the 'JavaScript' Library 'agGrid'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.0
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-htmlwidgets >= 1.0
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-knitr 

%description
Data objects in 'R' can be rendered as 'HTML' tables using the
'JavaScript' library 'ag-grid' (typically via 'R Markdown' or 'Shiny').
The 'ag-grid' library has been included in this 'R' package. The package
name 'RagGrid' is an abbreviation of 'R agGrid'.

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
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
