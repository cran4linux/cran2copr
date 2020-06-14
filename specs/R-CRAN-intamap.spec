%global packname  intamap
%global packver   1.4-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.9
Release:          2%{?dist}
Summary:          Procedures for Automated Interpolation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gstat >= 0.9.36
BuildRequires:    R-CRAN-sp >= 0.9.0
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gstat >= 0.9.36
Requires:         R-CRAN-sp >= 0.9.0
Requires:         R-CRAN-automap 
Requires:         R-CRAN-mvtnorm 
Requires:         R-MASS 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rgdal 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 

%description
Provides classes and methods for automated spatial interpolation.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
