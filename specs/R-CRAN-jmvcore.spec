%global packname  jmvcore
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Dependencies for the 'jamovi' Framework

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-R6 >= 1.0.1
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-stringi 

%description
A framework for creating rich interactive analyses for the jamovi platform
(see <https://www.jamovi.org> for more information).

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
%doc %{rlibdir}/%{packname}/jamovi.proto
%{rlibdir}/%{packname}/INDEX
