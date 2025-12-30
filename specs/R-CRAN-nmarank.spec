%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nmarank
%global packver   0.3-0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Complex Hierarchy Questions in Network Meta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-netmeta >= 2.7.0
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-netmeta >= 2.7.0
Requires:         R-CRAN-meta 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tidyr 

%description
Derives the most frequent hierarchies along with their probability of
occurrence. One can also define complex hierarchy criteria and calculate
their probability. Methodology based on Papakonstantinou et al. (2021)
<DOI:10.21203/rs.3.rs-858140/v1>.

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
