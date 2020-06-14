%global packname  apsimr
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Edit, Run and Evaluate APSIM Simulations Easily Using R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-reshape2 
Requires:         R-MASS 
Requires:         R-mgcv 

%description
The Agricultural Production Systems sIMulator (APSIM) is a widely used
simulator of agricultural systems.  This package includes functions to
create, edit and run APSIM simulations from R.  It also includes functions
to visualize the results of an APSIM simulation and perform
sensitivity/uncertainty analysis of APSIM either via functions in the
sensitivity package or by novel emulator-based functions. For more on
APSIM including download instructions go to url{www.apsim.info}.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
