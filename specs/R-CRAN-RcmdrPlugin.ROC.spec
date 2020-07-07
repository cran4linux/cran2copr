%global packname  RcmdrPlugin.ROC
%global packver   1.0-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.18
Release:          3%{?dist}
Summary:          Rcmdr Receiver Operator Characteristic Plug-In PACKAGE

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 1.7.0
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ResourceSelection 
Requires:         R-CRAN-Rcmdr >= 1.7.0
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ResourceSelection 

%description
Rcmdr GUI extension plug-in for Receiver Operator Characteristic tools
from pROC and ROCR packages. Also it ads a Rcmdr GUI extension for Hosmer
and Lemeshow GOF test from the package ResourceSelection.

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
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
