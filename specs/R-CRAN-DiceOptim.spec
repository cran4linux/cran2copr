%global packname  DiceOptim
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Kriging-Based Optimization for Computer Experiments

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-DiceKriging >= 1.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-DiceDesign 
Requires:         R-CRAN-DiceKriging >= 1.2
Requires:         R-methods 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-DiceDesign 

%description
Efficient Global Optimization (EGO) algorithm and adaptations for parallel
infill (multipoint EI), problems with noise, and problems with
constraints.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
