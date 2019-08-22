%global packname  basictabler
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Construct Rich Tables for Output to 'HTML'/'Excel'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-htmlwidgets >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-htmlwidgets >= 0.8
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-htmltools >= 0.3.5

%description
Easily create tables from data frames/matrices.  Create/manipulate tables
row-by-row, column-by-column or cell-by-cell. Use common
formatting/styling to output rich tables as 'HTML', 'HTML widgets' or to
'Excel'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
