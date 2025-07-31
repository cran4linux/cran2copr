%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Silhouette
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Proximity Measure Based Diagnostics for Standard, Soft, and Multi-Way Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-methods 

%description
Quantifies clustering quality by measuring both cohesion within clusters
and separation between clusters. Implements advanced silhouette width
computations for diverse clustering structures, including: simplified
silhouette (Van der Laan et al., 2003) <doi:10.1080/0094965031000136012>,
Probability of Alternative Cluster normalization methods (Raymaekers &
Rousseeuw, 2022) <doi:10.1080/10618600.2022.2050249>, fuzzy clustering and
silhouette diagnostics using membership probabilities (Campello &
Hruschka, 2006; Bhat & Kiruthika, 2024) <doi:10.1016/j.fss.2006.07.006>,
<doi:10.1080/23737484.2024.2408534>, and multi-way clustering extensions
such as block and tensor clustering (Schepers et al., 2008; Bhat &
Kiruthika, 2025) <doi:10.1007/s00357-008-9005-9>,
<doi:10.21203/rs.3.rs-6973596/v1>. Provides tools for computation and
visualization (Rousseeuw, 1987) <doi:10.1016/0377-0427(87)90125-7> to
support robust and reproducible cluster diagnostics across standard, soft,
and multi-way clustering settings.

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
