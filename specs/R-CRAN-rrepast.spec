%global packname  rrepast
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          2%{?dist}
Summary:          Invoke 'Repast Simphony' Simulation Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-sensitivity 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-sensitivity 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
An R and Repast integration tool for running individual-based (IbM)
simulation models developed using 'Repast Simphony' Agent-Based framework
directly from R code supporting multicore execution. This package
integrates 'Repast Simphony' models within R environment, making easier
the tasks of running and analyzing model output data for automated
parameter calibration and for carrying out uncertainty and sensitivity
analysis using the power of R environment.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
