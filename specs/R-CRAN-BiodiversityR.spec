%global packname  BiodiversityR
%global packver   2.12-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.12.1
Release:          1%{?dist}
Summary:          Package for Community Ecology and Suitability Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.5.3
BuildRequires:    R-CRAN-vegan >= 2.5.1
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-vegan3d 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-Rcmdr >= 2.5.3
Requires:         R-CRAN-vegan >= 2.5.1
Requires:         R-tcltk 
Requires:         R-CRAN-vegan3d 
Requires:         R-CRAN-rgl 

%description
Graphical User Interface (via the R-Commander) and utility functions
(often based on the vegan package) for statistical analysis of
biodiversity and ecological communities, including species accumulation
curves, diversity indices, Renyi profiles, GLMs for analysis of species
abundance and presence-absence, distance matrices, Mantel tests, and
cluster, constrained and unconstrained ordination analysis. A book on
biodiversity and community ecology analysis is available for free download
from the website. In 2012, methods for (ensemble) suitability modelling
and mapping were expanded in the package.

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
