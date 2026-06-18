%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AntClassify
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Guilds, Invasion Status, Endemism, and Rarity of Ants

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-curl 

%description
Provides functions for the analysis of ant communities, aiming to
standardize workflows in myrmecology. The package automates the assignment
of species to functional guilds based on trophic strategies, feeding
habits, and foraging behavior, using established classification frameworks
(Silva et al., 2015 <doi:10.7476/9788574554419>; Silvestre et al., 2003
<isbn:9588151236>; Delabie et al., 2000
<https://www.researchgate.net/publication/44961742_Sampling_Ground-Dwelling_Ants_Case_Studies_from_the_World%%27s_Rain_Forests>),
and also includes a novel classification system implemented within the
package, developed from ant species occurring in urban environments. It
also includes routines to flag exotic species of Brazil (Vieira, 2025,
unpublished master's thesis), identify endemic species (Silva et al., 2025
<doi:10.37885/250920259>), and classify species rarity and rarity forms of
the Atlantic Forest (Silva et al., 2024
<doi:10.1016/j.biocon.2024.110640>). The package reduces manual effort and
improves reproducibility, supporting research and biodiversity management
of Neotropical ant communities.

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
