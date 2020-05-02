%global packname  cfdecomp
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Counterfactual Decomposition: MC Integration of the G-Formula

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Provides a set of functions for counterfactual decomposition (cfdecomp).
The functions available in this package decompose differences in an
outcome attributable to a mediating variable (or sets of mediating
variables) between groups based on counterfactual (causal inference)
theory. By using Monte Carlo (MC) integration (simulations based on
empirical estimates from multivariable models) we provide added
flexibility compared to existing (analytical) approaches, at the cost of
computational power or time. The added flexibility means that we can
decompose difference between groups in any outcome or and with any
mediator (any variable type and distribution). See Sudharsanan & Bijlsma
(2019) <doi:10.4054/MPIDR-WP-2019-004> for more information.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
