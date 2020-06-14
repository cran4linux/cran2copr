%global packname  ivmte
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Instrumental Variables: Extrapolation by Marginal TreatmentEffects

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Formula 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
The marginal treatment effect was introduced by Heckman and Vytlacil
(2005) <doi:10.1111/j.1468-0262.2005.00594.x> to provide a
choice-theoretic interpretation to instrumental variables models that
maintain the monotonicity condition of Imbens and Angrist (1994)
<doi:10.2307/2951620>. This interpretation can be used to extrapolate from
the compliers to estimate treatment effects for other subpopulations. This
package provides a flexible set of methods for conducting this
extrapolation. It allows for parametric or nonparametric sieve estimation,
and allows the user to maintain shape restrictions such as monotonicity.
The package operates in the general framework developed by Mogstad, Santos
and Torgovitsky (2018) <doi:10.3982/ECTA15463>, and accommodates either
point identification or partial identification (bounds). In the partially
identified case, bounds are computed using linear programming. Support for
three linear programming solvers is provided. Gurobi and the Gurobi R API
can be obtained from <http://www.gurobi.com/index>. CPLEX can be obtained
from <https://www.ibm.com/analytics/cplex-optimizer>. CPLEX R APIs
'Rcplex' and 'cplexAPI' are available from CRAN. The lp_solve library is
freely available from <http://lpsolve.sourceforge.net/5.5/>, and is
included when installing its API 'lpSolveAPI', which is available from
CRAN.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
