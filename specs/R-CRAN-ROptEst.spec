%global packname  ROptEst
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Optimally Robust Estimation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-distrMod >= 2.8.1
BuildRequires:    R-CRAN-distr >= 2.8.0
BuildRequires:    R-CRAN-distrEx >= 2.8.0
BuildRequires:    R-CRAN-RandVar >= 1.2.0
BuildRequires:    R-CRAN-RobAStBase >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-distrMod >= 2.8.1
Requires:         R-CRAN-distr >= 2.8.0
Requires:         R-CRAN-distrEx >= 2.8.0
Requires:         R-CRAN-RandVar >= 1.2.0
Requires:         R-CRAN-RobAStBase >= 1.2.0
Requires:         R-methods 
Requires:         R-CRAN-startupmsg 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Optimally robust estimation in general smoothly parameterized models using
S4 classes and methods.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
