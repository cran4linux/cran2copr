%global packname  functClust
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Clustering of Redundant Components of a System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-clusterCrit 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-clusterCrit 

%description
Cluster together the components that make up an interactive system on the
basis of their functional redundancy for one or more collective, systemic
performances. Plot the hierarchical tree of component clusters, the
modelled and predicted performances of component assemblages, and other
results associated with a functional clustering. Test and prioritize the
significance of the different components that make up the interactive
system, of the different assemblages of components that make up the
dataset, and of the different performances observed on the component
assemblages. The method finds application in ecology, for instance, where
the system is an ecosystem, the components are organisms or species, and
the systemic performance is the production of biomass or the respiration
of the ecosystem. The method is extensively described in Jaillard B,
Deleporte P, Loreau M, Violle C (2018) "A combinatorial analysis using
observational data identifies species that govern ecosystem functioning"
<doi:10.1371/journal.pone.0201135>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
