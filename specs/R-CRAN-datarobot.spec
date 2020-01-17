%global packname  datarobot
%global packver   2.16.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.16.0
Release:          1%{?dist}
Summary:          'DataRobot' Predictive Modeling API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.7
BuildRequires:    R-CRAN-yaml >= 2.1.13
BuildRequires:    R-CRAN-httr >= 1.2.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-curl >= 2.7
Requires:         R-CRAN-yaml >= 2.1.13
Requires:         R-CRAN-httr >= 1.2.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-methods 
Requires:         R-stats 

%description
For working with the 'DataRobot' predictive modeling platform's API
<https://www.datarobot.com/>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/icons
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
