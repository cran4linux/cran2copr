%global packname  econetwork
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Ecological Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rdiversity 
BuildRequires:    R-CRAN-Matrix.utils 
BuildRequires:    R-CRAN-blockmodels 
BuildRequires:    R-CRAN-bipartite 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rdiversity 
Requires:         R-CRAN-Matrix.utils 
Requires:         R-CRAN-blockmodels 
Requires:         R-CRAN-bipartite 

%description
A collection of advanced tools, methods and models specifically designed
for analyzing different types of ecological networks - especially
antagonistic (food webs, host-parasite), mutualistic (plant-pollinator,
plant-fungus, etc) and competitive networks, as well as their variability
in time and space. Statistical models are developed to describe and
understand the mechanisms that determine species interactions, and to
decipher the organization of these (multi-layer) ecological networks.

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
