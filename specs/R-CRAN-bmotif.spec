%global __brp_check_rpaths %{nil}
%global packname  bmotif
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Motif Analyses of Bipartite Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-tensor >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-tensor >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Counts occurrences of motifs in bipartite networks, as well as the number
of times each node or link appears in each unique position within motifs.
Has support for both binary and weighted motifs: can calculate the mean
weight of motifs and the standard deviation of their mean weights.
Intended for use in ecology, but its methods are general and can be
applied to any bipartite network. Full details are given in Simmons et al.
(2019) <doi:10.1111/2041-210X.13149>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
