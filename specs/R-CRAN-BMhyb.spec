%global packname  BMhyb
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}
Summary:          Comparative Methods for Phylogenetic Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-TreeSim 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metR 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-TreeSim 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-viridis 
Requires:         R-Matrix 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-metR 
Requires:         R-parallel 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-plyr 

%description
Analyze the phenotypic evolution of species of hybrid origin on a
phylogenetic network. This can detect a burst of variation at the
formation of a hybrid as well as an increase or decrease in trait value at
a hybridization event. Parameters are estimated by maximum likelihood, and
model averaging can be done automatically. Users need to enter a
comparative data set and a phylogenetic network.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
