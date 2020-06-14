%global packname  CausalKinetiX
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Learning Stable Structures in Kinetic Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sundialr >= 0.1.3
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-sundialr >= 0.1.3
Requires:         R-CRAN-fda 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-deSolve 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-pspline 
Requires:         R-utils 
Requires:         R-CRAN-glmnet 

%description
Implementation of 'CausalKinetiX', a framework for learning stable
structures in kinetic systems. Apart from the main functions
CausalKinetiX() and CausalKinetiX.modelranking() it includes functions to
generate data from three simulations models, which can be used to
benchmark structure learning methods for linear ordinary differential
equation models. A detailed description of the underlying methods as well
as details on the examples are given in Pfister, Bauer and Peters (2018)
<arXiv:1810.11776>.

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
