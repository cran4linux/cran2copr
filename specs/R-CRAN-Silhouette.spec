%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Silhouette
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Proximity Measure Based Diagnostics for Standard, Soft, and Multi-Way Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Quantifies clustering quality by measuring both cohesion within clusters
and separation between clusters. Silhouette widths are computed from the n
by K matrices that clustering algorithms return (distances or similarities
to cluster prototypes, fuzzy memberships, or posterior probabilities)
instead of all pairwise dissimilarities, for the partition an algorithm
produced or one supplied by the user. Implements the simplified silhouette
of Van der Laan et al. (2003) <doi:10.1080/0094965031000136012>, the
probability of alternative cluster normalization of Raymaekers and
Rousseeuw (2022) <doi:10.1080/10618600.2022.2050249>, the fuzzy silhouette
average of Campello and Hruschka (2006) <doi:10.1016/j.fss.2006.07.006>,
the density-based silhouette of Menardi (2011)
<doi:10.1007/s11222-010-9169-0>, the soft silhouettes of Bhat Kapu and
Kiruthika (2024) <doi:10.1080/23737484.2024.2408534>, and the extended
silhouette for multi-way clustering of Schepers et al. (2008)
<doi:10.1007/s00357-008-9005-9> and Bhat Kapu and Kiruthika (2025)
<doi:10.21203/rs.3.rs-6973596/v1>. Provides summaries and 'ggplot2'
silhouette plots in the style of Rousseeuw (1987)
<doi:10.1016/0377-0427(87)90125-7>.

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
