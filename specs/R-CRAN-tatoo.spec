%global packname  tatoo
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Combine and Export Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.0.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-colt 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-openxlsx >= 4.0.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-colt 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-withr 

%description
Functions to combine data.frames in ways that require additional effort in
base R, and to add metadata (id, title, ...) that can be used for printing
and xlsx export. The 'Tatoo_report' class is provided as a convenient
helper to write several such tables to a workbook, one table per
worksheet. Tatoo is built on top of 'openxlsx', but intimate knowledge of
that package is not required to use tatoo.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
