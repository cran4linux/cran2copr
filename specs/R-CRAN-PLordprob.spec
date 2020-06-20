%global packname  PLordprob
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Multivariate Ordered Probit Model via Pairwise Likelihood

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-mnormt 
Requires:         R-CRAN-mnormt 

%description
Multivariate ordered probit model, i.e. the extension of the scalar
ordered probit model where the observed variables have dimension greater
than one. Estimation of the parameters is done via maximization of the
pairwise likelihood, a special case of the composite likelihood obtained
as product of bivariate marginal distributions. The package uses the
Fortran 77 subroutine SADMVN by Alan Genz, with minor adaptations made by
Adelchi Azzalini in his "mvnormt" package for evaluating the
two-dimensional Gaussian integrals involved in the pairwise
log-likelihood. Optimization of the latter objective function is performed
via quasi-Newton box-constrained optimization algorithm, as implemented in
nlminb.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
