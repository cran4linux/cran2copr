%global packname  intamapInteractive
%global packver   1.1-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.12
Release:          2%{?dist}
Summary:          Interactive Add-on Functionality for 'intamap'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intamap 
BuildRequires:    R-CRAN-spcosa 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-intamap 
Requires:         R-CRAN-spcosa 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-CRAN-sp 

%description
Includes additional functionality for spatial interpolation in the intamap
package, such as bias correction and network optimization.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX
