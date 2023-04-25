%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hierarchicalSets
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Set Data Visualization Using Hierarchies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-ggdendro 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gtable 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-patchwork 

%description
Pure set data visualization approaches are often limited in scalability
due to the combinatorial explosion of distinct set families as the number
of sets under investigation increases. hierarchicalSets applies a set
centric hierarchical clustering of the sets under investigation and uses
this hierarchy as a basis for a range of scalable visual representations.
hierarchicalSets is especially well suited for collections of sets that
describe comparable comparable entities as it relies on the sets to have a
meaningful relational structure.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
