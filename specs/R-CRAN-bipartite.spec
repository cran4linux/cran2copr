%global packname  bipartite
%global packver   2.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.16
Release:          1%{?dist}%{?buildtag}
Summary:          Visualising Bipartite Networks and Calculating Some (Ecological) Indices

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-permute 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-permute 

%description
Functions to visualise webs and calculate a series of indices commonly
used to describe pattern in (ecological) webs. It focuses on webs
consisting of only two levels (bipartite), e.g. pollination webs or
predator-prey-webs. Visualisation is important to get an idea of what we
are actually looking at, while the indices summarise different aspects of
the web's topology.

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
