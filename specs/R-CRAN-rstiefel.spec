%global packname  rstiefel
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Random Orthonormal Matrix Generation and Optimization on theStiefel Manifold

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
Simulation of random orthonormal matrices from linear and quadratic
exponential family distributions on the Stiefel manifold. The most general
type of distribution covered is the matrix-variate Bingham-von
Mises-Fisher distribution. Most of the simulation methods are presented in
Hoff(2009) "Simulation of the Matrix Bingham-von Mises-Fisher
Distribution, With Applications to Multivariate and Relational Data"
<doi:10.1198/jcgs.2009.07177>. The package also includes functions for
optimization on the Stiefel manifold based on algorithms described in Wen
and Yin (2013) "A feasible method for optimization with orthogonality
constraints" <doi:10.1007/s10107-012-0584-1>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
