%global packname  FAOSTAT
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Download Data from the FAOSTAT Database of the Food andAgricultural Organization (FAO) of the United Nations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.22
BuildRequires:    R-CRAN-data.table >= 1.8.2
BuildRequires:    R-CRAN-plyr >= 1.7.1
BuildRequires:    R-CRAN-RJSONIO >= 0.96.0
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3
BuildRequires:    R-CRAN-classInt >= 0.1.19
BuildRequires:    R-CRAN-labeling >= 0.1
Requires:         R-MASS >= 7.3.22
Requires:         R-CRAN-data.table >= 1.8.2
Requires:         R-CRAN-plyr >= 1.7.1
Requires:         R-CRAN-RJSONIO >= 0.96.0
Requires:         R-CRAN-ggplot2 >= 0.9.3
Requires:         R-CRAN-classInt >= 0.1.19
Requires:         R-CRAN-labeling >= 0.1

%description
A list of functions to download statistics from FAOSTAT (database of the
Food and Agricultural Organization of the United Nations) and WDI
(database of the World Bank), and to perform some harmonization
operations.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
