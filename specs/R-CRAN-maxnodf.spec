%global packname  maxnodf
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Approximate Maximisation of Nestedness in Bipartite Graphs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-stats >= 3.4.4
BuildRequires:    R-utils >= 3.4.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-stats >= 3.4.4
Requires:         R-utils >= 3.4.4
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Functions to generate graphs that maximise the NODF (nestedness metric
based on overlap and decreasing fill) metric for a given number of rows,
columns and links. NODF was originally defined by Almeida-Neto et al.
(2008) <doi:10.1111/j.0030-1299.2008.16644.x>. As nestedness in ecological
networks depends on the size of the networks we require normalisation to
make them comparable. We offer three highly optimised algorithms to find
the optimising graphs so that users can choose an appropriate trade off
between computation time and NODF value for the task at hand.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
