%global packname  bartMachine
%global packver   1.2.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4.2
Release:          2%{?dist}
Summary:          Bayesian Additive Regression Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bartMachineJARs >= 1.0
BuildRequires:    R-CRAN-rJava >= 0.9.8
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-bartMachineJARs >= 1.0
Requires:         R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-car 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-missForest 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
An advanced implementation of Bayesian Additive Regression Trees with
expanded features for data analysis and visualization.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
