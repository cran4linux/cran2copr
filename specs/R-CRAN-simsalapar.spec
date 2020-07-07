%global packname  simsalapar
%global packver   1.0-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          3%{?dist}
Summary:          Tools for Simulation Studies in Parallel

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridBase >= 0.4.6
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-CRAN-gridBase >= 0.4.6
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-colorspace 

%description
Tools for setting up ("design"), conducting, and evaluating large-scale
simulation studies with graphics and tables, including parallel
computations.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/saved-sim
%doc %{rlibdir}/%{packname}/xtraR
%{rlibdir}/%{packname}/INDEX
