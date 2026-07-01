%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NeighborFinder
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Find Neighbor Species of a Bacteria of Interest in the Human Gut Microbiota

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-network 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sna 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Implementation of the local approach described in Sola et al., 2026
<doi:10.64898/2025.12.05.692507> to identify companion species of a
bacteria of interest. From several abundance tables of metagenomic data,
'NeighborFinder' suggests a shortlist of companion species based on the
integration of results. A visualization via a network is proposed.

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
