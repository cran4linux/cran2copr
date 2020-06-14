%global packname  x3ptools
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}
Summary:          Tools for Working with 3D Surface Measurements

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.8.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-rgl >= 0.99.9
BuildRequires:    R-CRAN-digest >= 0.6.15
BuildRequires:    R-CRAN-png >= 0.1.7
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-zoo >= 1.8.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-rgl >= 0.99.9
Requires:         R-CRAN-digest >= 0.6.15
Requires:         R-CRAN-png >= 0.1.7
Requires:         R-CRAN-assertthat 
Requires:         R-grDevices 

%description
The x3p file format is specified in ISO standard 5436:2000 to describe 3d
surface measurements. 'x3ptools' allows reading, writing and basic
modifications to the 3D surface measurements.

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
%doc %{rlibdir}/%{packname}/csafe-color.png
%doc %{rlibdir}/%{packname}/csafe-logo.x3p
%doc %{rlibdir}/%{packname}/make-logo.R
%doc %{rlibdir}/%{packname}/sample-land.x3p
%doc %{rlibdir}/%{packname}/sensofar2.xml
%doc %{rlibdir}/%{packname}/templateXML.xml
%{rlibdir}/%{packname}/INDEX
