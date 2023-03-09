%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funspace
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Creating and Representing Functional Trait Spaces

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-paran 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-paran 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-viridis 

%description
Estimation of functional spaces based on traits of organisms. The package
includes functions to impute missing trait values (with or without
considering phylogenetic information), and to create, represent and
analyse two dimensional functional spaces based on principal components
analysis, other ordination methods, or raw traits. It also allows for
mapping a third variable onto the functional space.  See 'Carmona et al.
(2021)' <doi:10.1038/s41586-021-03871-y>, 'Puglielli et al.  (2021)'
<doi:10.1111/nph.16952>, 'Carmona et al. (2021)'
<doi:10.1126/sciadv.abf2675>, 'Carmona et al. (2019)'
<doi:10.1002/ecy.2876> for more information.

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
