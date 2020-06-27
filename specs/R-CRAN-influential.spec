%global packname  influential
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Identification and Classification of the Most Influential Nodes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-coop 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-coop 
Requires:         R-CRAN-reshape2 

%description
Contains functions for the classification and ranking of top candidate
features, reconstruction of networks from adjacency matrices and data
frames, analysis of the topology of the network and calculation of
centrality measures, and identification of the most influential nodes.
Also, a function is provided for running SIRIR model, which is the
combination of leave-one-out cross validation technique and the
conventional SIR model, on a network to unsupervisedly rank the true
influence of vertices. Additionally, some functions have been provided for
the assessment of dependence and correlation of two network centrality
measures as well as the conditional probability of deviation from their
corresponding means in opposite direction. Fred Viole and David Nawrocki
(2013, ISBN:1490523995). Csardi G, Nepusz T (2006). "The igraph software
package for complex network research." InterJournal, Complex Systems,
1695. Adopted algorithms and sources are referenced in function document.

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
