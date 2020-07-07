%global packname  neldermead
%global packver   1.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          3%{?dist}
Summary:          R Port of the 'Scilab' Neldermead Module

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-optimbase >= 1.0.9
BuildRequires:    R-CRAN-optimsimplex >= 1.0.7
BuildRequires:    R-methods 
Requires:         R-CRAN-optimbase >= 1.0.9
Requires:         R-CRAN-optimsimplex >= 1.0.7
Requires:         R-methods 

%description
Provides several direct search optimization algorithms based on the
simplex method. The provided algorithms are direct search algorithms, i.e.
algorithms which do not use the derivative of the cost function. They are
based on the update of a simplex. The following algorithms are available:
the fixed shape simplex method of Spendley, Hext and Himsworth
(unconstrained optimization with a fixed shape simplex), the variable
shape simplex method of Nelder and Mead (unconstrained optimization with a
variable shape simplex made), and Box's complex method (constrained
optimization with a variable shape simplex).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
