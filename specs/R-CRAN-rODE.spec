%global packname  rODE
%global packver   0.99.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.6
Release:          3%{?dist}
Summary:          Ordinary Differential Equation (ODE) Solvers Written in R UsingS4 Classes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-data.table 

%description
Show physics, math and engineering students how an ODE solver is made and
how effective R classes can be for the construction of the equations that
describe natural phenomena. Inspiration for this work comes from the book
on "Computer Simulations in Physics" by Harvey Gould, Jan Tobochnik, and
Wolfgang Christian. Book link:
<http://www.compadre.org/osp/items/detail.cfm?ID=7375>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/notebooks
%doc %{rlibdir}/%{packname}/test_examples
%{rlibdir}/%{packname}/INDEX
