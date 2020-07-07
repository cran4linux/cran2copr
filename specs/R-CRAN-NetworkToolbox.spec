%global packname  NetworkToolbox
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          2%{?dist}
Summary:          Methods and Measures for Brain, Cognitive, and PsychometricNetwork Analysis

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-IsingFit 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-Matrix 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-ppcor 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-MASS 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-IsingFit 
Requires:         R-CRAN-pbapply 

%description
Implements network analysis and graph theory measures used in
neuroscience, cognitive science, and psychology. Methods include various
filtering methods and approaches such as threshold, dependency (Kenett,
Tumminello, Madi, Gur-Gershgoren, Mantegna, & Ben-Jacob, 2010
<doi:10.1371/journal.pone.0015032>), Information Filtering Networks
(Barfuss, Massara, Di Matteo, & Aste, 2016
<doi:10.1103/PhysRevE.94.062306>), and Efficiency-Cost Optimization
(Fallani, Latora, & Chavez, 2017 <doi:10.1371/journal.pcbi.1005305>).
Brain methods include the recently developed Connectome Predictive
Modeling (see references in package). Also implements several network
measures including local network characteristics (e.g., centrality),
community-level network characteristics (e.g., community centrality),
global network characteristics (e.g., clustering coefficient), and various
other measures associated with the reliability and reproducibility of
network analysis.

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
