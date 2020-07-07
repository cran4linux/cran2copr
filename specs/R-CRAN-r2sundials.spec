%global packname  r2sundials
%global packver   5.0.0-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.0.7
Release:          3%{?dist}
Summary:          Wrapper for 'SUNDIALS' Solving ODE and Sensitivity Problem

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-rmumps >= 5.2.1.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-rmumps >= 5.2.1.6
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Wrapper for widely used 'SUNDIALS' software (SUite of Nonlinear and
DIfferential/ALgebraic Equation Solvers) and more precisely to its
'CVODES' solver. It is aiming to solve ordinary differential equations
(ODE) and optionally pending forward sensitivity problem. The wrapper is
made 'R' friendly by allowing to pass custom parameters to user's callback
functions. Such functions can be both written in 'R' and in 'C++'
('RcppArmadillo' flavor). In case of 'C++', performance is greatly
improved so this option is highly advisable when performance matters. If
provided, Jacobian matrix can be calculated either in dense or sparse
format. In the latter case 'rmumps' package is used to solve corresponding
linear systems. Root finding and pending event management are optional and
can be specified as 'R' or 'C++' functions too. This makes them a very
flexible tool for controlling the ODE system during the time course
simulation. 'SUNDIALS' library was published in Hindmarsh et al. (2005)
<doi:10.1145/1089014.1089020>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/cvodes.txt.in
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libsundials.a
