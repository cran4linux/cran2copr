%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mmodely
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Multivariate Origins Determinants - Evolutionary Lineages in Ecology

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caper 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caroline 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-caper 
Requires:         R-stats 
Requires:         R-CRAN-caroline 
Requires:         R-CRAN-ape 

%description
Perform multivariate modeling of evolved traits, with special attention to
understanding the interplay of the multi-factorial determinants of their
origins in complex ecological settings (Stephens, 2007
<doi:10.1016/j.tree.2006.12.003>). This software primarily concentrates on
phylogenetic regression analysis, enabling implementation of tree
transformation averaging and visualization functionality. Functions
additionally support information theoretic approaches (Grueber, 2011
<doi:10.1111/j.1420-9101.2010.02210.x>; Garamszegi, 2011
<doi:10.1007/s00265-010-1028-7>) such as model averaging and selection of
phylogenetic models. There are other numerous functions for visualizing
confounded variables, plotting phylogenetic trees, as well as reporting
and exporting modeling results. Lastly, as challenges to ecology are
inherently multifarious, and therefore often multi-dataset, this package
features several functions to support the identification, interpolation,
merging, and updating of missing data and outdated nomenclature.

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
