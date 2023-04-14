%global __brp_check_rpaths %{nil}
%global packname  evtree
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          3%{?dist}%{?buildtag}
Summary:          Evolutionary Learning of Globally Optimal Trees

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-partykit 
Requires:         R-CRAN-partykit 

%description
Commonly used classification and regression tree methods like the CART
algorithm are recursive partitioning methods that build the model in a
forward stepwise search. Although this approach is known to be an
efficient heuristic, the results of recursive tree methods are only
locally optimal, as splits are chosen to maximize homogeneity at the next
step only. An alternative way to search over the parameter space of trees
is to use global optimization methods like evolutionary algorithms. The
'evtree' package implements an evolutionary algorithm for learning
globally optimal classification and regression trees in R. CPU and
memory-intensive tasks are fully computed in C++ while the 'partykit'
package is leveraged to represent the resulting trees in R, providing
unified infrastructure for summaries, visualizations, and predictions.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
