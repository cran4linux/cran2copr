%global packname  c14bazAAR
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Download and Prepare C14 Dates from Different Source Databases

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-pbapply >= 1.3.3
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-CRAN-dplyr >= 0.7.2
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-rlang >= 0.1.1
BuildRequires:    R-graphics 
Requires:         R-stats >= 3.4.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-pbapply >= 1.3.3
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-CRAN-dplyr >= 0.7.2
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-rlang >= 0.1.1
Requires:         R-graphics 

%description
Query different C14 date databases and apply basic data cleaning, merging
and calibration steps.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
