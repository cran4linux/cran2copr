%global __brp_check_rpaths %{nil}
%global packname  codyn
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Community Dynamics Metrics

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-assertthat 
Requires:         R-stats 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-vegan 

%description
Univariate and multivariate temporal and spatial diversity indices, rank
abundance curves, and community stability measures. The functions
implement measures that are either explicitly temporal and include the
option to calculate them over multiple replicates, or spatial and include
the option to calculate them over multiple time points. Functions fall
into five categories: static diversity indices, temporal diversity
indices, spatial diversity indices, rank abundance curves, and community
stability measures. The diversity indices are temporal and spatial analogs
to traditional diversity indices. Specifically, the package includes
functions to calculate community richness, evenness and diversity at a
given point in space and time. In addition, it contains functions to
calculate species turnover, mean rank shifts, and lags in community
similarity between two time points. Details of the methods are available
in Hallett et al. (2016) <doi:10.1111/2041-210X.12569> and Avolio et al.
(2019) <doi:10.1002/ecs2.2881>.

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
