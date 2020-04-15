%global packname  bbricks
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Bayesian Methods and Graphical Model Structures for StatisticalModeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
A class of frequently used Bayesian parametric and nonparametric model
structures, as well as a set of tools for common analytical tasks.
Structures include Gaussian and Normal-Inverse-Wishart conjugate
structure, Gaussian and Normal-Inverse-Gamma conjugate structure,
Categorical and Dirichlet conjugate structure, Dirichlet Process on
positive integers, Dirichlet Process in general, Hierarchical Dirichlet
Process ... Tasks include updating posteriors, calculating marginal
likelihood, calculating posterior predictive densities, sampling from
posterior predictive distributions, calculating "Maximum A Posteriori"
(MAP) estimates ... See Murphy (2012, <doi:10.1080/09332480.2014.914768>),
Koller and Friedman (2009, <doi:10.1017/s0269888910000275>) and Andrieu,
de Freitas, Doucet and Jordan (2003, <doi:10.1023/A:1020281327116>) for
more information. See <https://chenhaotian.github.io/Bayesian-Bricks/> to
get started.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
