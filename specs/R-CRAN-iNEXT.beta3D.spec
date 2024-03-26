%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iNEXT.beta3D
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interpolation and Extrapolation with Beta Diversity for Three Dimensions of Biodiversity

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-iNEXT.3D 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidytree 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-phyclust 
BuildRequires:    R-CRAN-ape 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-iNEXT.3D 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidytree 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-phyclust 
Requires:         R-CRAN-ape 

%description
As a sequel to 'iNEXT', the 'iNEXT.beta3D' package provides functions to
compute standardized taxonomic, phylogenetic, and functional diversity
(3D) estimates with a common sample size (for alpha and gamma diversity)
or sample coverage (for alpha, beta, gamma diversity as well as
dissimilarity or turnover indices). Hill numbers and their generalizations
are used to quantify 3D and to make multiplicative decomposition (gamma =
alpha x beta). The package also features size- and coverage-based
rarefaction and extrapolation sampling curves to facilitate rigorous
comparison of beta diversity across datasets. See Chao et al. (2023)
<doi:10.1002/ecm.1588> for more details.

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
