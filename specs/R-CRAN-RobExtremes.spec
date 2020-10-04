%global packname  RobExtremes
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Optimally Robust Estimation for Extreme Value Distributions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-distrMod >= 2.8.1
BuildRequires:    R-CRAN-distrEx >= 2.8.0
BuildRequires:    R-CRAN-ROptEst >= 1.2.0
BuildRequires:    R-CRAN-RobAStBase >= 1.2.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-RobAStRDA 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-RandVar 
BuildRequires:    R-CRAN-startupmsg 
BuildRequires:    R-CRAN-actuar 
Requires:         R-CRAN-distrMod >= 2.8.1
Requires:         R-CRAN-distrEx >= 2.8.0
Requires:         R-CRAN-ROptEst >= 1.2.0
Requires:         R-CRAN-RobAStBase >= 1.2.0
Requires:         R-methods 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-RobAStRDA 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-RandVar 
Requires:         R-CRAN-startupmsg 
Requires:         R-CRAN-actuar 

%description
Optimally robust estimation for extreme value distributions using S4
classes and methods (based on packages 'distr', 'distrEx', 'distrMod',
'RobAStBase', and 'ROptEst').

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
%doc %{rlibdir}/%{packname}/AddMaterial
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/TOBEDONE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
