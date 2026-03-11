%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ArchipelagoEngine
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Weight Construction for Archipelagic Geographies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-magrittr 

%description
Implements specialized K-Nearest Neighbor (KNN) logic to address the
unique challenges of spatial modeling in archipelagic environments.
Standard contiguity models often leave significant portions of island
nations (e.g., 20%% of the Philippines) mathematically isolated. This
package provides tools to ensure 100%% network connectivity, neutralizing
spatial bias and enabling robust econometric inference. Methodology
follows Anselin (1988, ISBN:9024737354) and LeSage and Pace (2009)
<doi:10.1201/9781420064254>.

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
