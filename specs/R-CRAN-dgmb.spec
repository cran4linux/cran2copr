%global packname  dgmb
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Simulating Data for PLS Mode B Structural Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         bwidget
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
Requires:         R-tcltk 
Requires:         R-MASS 
Requires:         R-CRAN-abind 

%description
A set of functions have been implemented to generate random data to
perform Monte Carlo simulations on structural models with formative
constructs and interaction and nonlinear effects (Two-Step PLS Mode B
structural models). The setup of the true model considers a simple
structure with three formative exogenous constructs related to one
formative endogenous construct. The routines take into account the
interaction and nonlinear effects of the exogenous constructs on the
endogenous construct.

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
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/INDEX
