%global packname  RandomFields
%global packver   3.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.8
Release:          1%{?dist}
Summary:          Simulation and Analysis of Random Fields

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RandomFieldsUtils >= 0.5.1
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RandomFieldsUtils >= 0.5.1
Requires:         R-CRAN-sp 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Methods for the inference on and the simulation of Gaussian fields are
provided, as well as methods for the simulation of extreme value random
fields. Main geostatistical parts are based on the books by Christian
Lantuejoul <doi:10.1007/978-3-662-04808-5>, Jean-Paul Chiles and Pierre
Delfiner <doi:10.1002/9781118136188> and Noel A. Cressie
<doi:10.1002/9781119115151>. For the extreme value random fields see
Oesting, Schlather, Schillings (2019) <doi.org/10.1002/sta4.228> and
Schlather (2002) <doi.org/10.1023/A:1020977924878>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
