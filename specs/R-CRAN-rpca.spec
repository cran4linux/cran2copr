%global packname  rpca
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          RobustPCA: Decompose a Matrix into Low-Rank and SparseComponents

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Suppose we have a data matrix, which is the superposition of a low-rank
component and a sparse component. Candes, E. J., Li, X., Ma, Y., & Wright,
J. (2011). Robust principal component analysis?. Journal of the ACM
(JACM), 58(3), 11. prove that we can recover each component individually
under some suitable assumptions. It is possible to recover both the
low-rank and the sparse components exactly by solving a very convenient
convex program called Principal Component Pursuit; among all feasible
decompositions, simply minimize a weighted combination of the nuclear norm
and of the L1 norm. This package implements this decomposition algorithm
resulting with Robust PCA approach.

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
%{rlibdir}/%{packname}/INDEX
