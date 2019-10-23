%global packname  triversity
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Diversity Measures on Tripartite Graphs

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-data.tree 
Requires:         R-Matrix 
Requires:         R-CRAN-data.tree 

%description
Computing diversity measures on tripartite graphs. This package first
implements a parametrized family of such diversity measures which apply on
probability distributions. Sometimes called "True Diversity", this family
contains famous measures such as the richness, the Shannon entropy, the
Herfindahl-Hirschman index, and the Berger-Parker index. Second, the
package allows to apply these measures on probability distributions
resulting from random walks between the levels of tripartite graphs. By
defining an initial distribution at a given level of the graph and a path
to follow between the three levels, the probability of the walker's
position within the final level is then computed, thus providing a
particular instance of diversity to measure.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
