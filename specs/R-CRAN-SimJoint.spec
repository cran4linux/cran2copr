%global packname  SimJoint
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          2%{?dist}
Summary:          Simulate Joint Distribution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-RcppParallel 

%description
Simulate multivariate correlated data given nonparametric marginals and
their joint structure characterized by a Pearson or Spearman correlation
matrix. The simulator engages the problem from a purely computational
perspective. It assumes no statistical models such as copulas or
parametric distributions, and can approximate the target correlations
regardless of theoretical feasibility. The algorithm integrates and
advances the Iman-Conover (1982) approach <doi:10.1080/03610918208812265>
and the Ruscio-Kaczetow iteration (2008) <doi:10.1080/00273170802285693>.
Package functions are carefully implemented in C++ for squeezing computing
speed, suitable for large input in a manycore environment. Precision of
the approximation and computing speed both substantially outperform
various CRAN packages to date. Benchmarks are detailed in function
examples. A simple heuristic algorithm is additionally designed to
optimize the joint distribution in the post-simulation stage. The
heuristic demonstrated good potential of achieving the same level of
precision of approximation without the enhanced
Iman-Conover-Ruscio-Kaczetow. The package contains a copy of Permuted
Congruential Generator from <http://www.pcg-random.org>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
