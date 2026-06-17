%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nicheR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ellipsoid-Based Virtual Niches and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-terra 

%description
Provides a robust set of tools for researchers and modelers to construct
and define virtual ecological niches using ellipsoid geometries. It
enables the identification and extraction of suitable environmental areas,
simulation of species occurrence points with various sampling strategies,
and visualization of niche boundaries and simulated occurrences in both
environmental and geographic space. Inspired by methodologies in 'NicheA'
and the 'virtualspecies' R package, 'nicheR' aims to streamline the
process of niche conceptualization and data generation for ecological
studies. Methodological and theoretical foundations are described in
Peterson et al. (2011, ISBN:9780691136882), Etherington et al. (2009)
<doi:10.1111/j.1365-2699.2008.02041.x>, Qiao et al. (2015)
<doi:10.1111/ecog.01961>, Nunez-Penichet et al. (2021)
<doi:10.21425/F5FBG52142>, Cobos and Peterson (2022)
<doi:10.17161/bi.v17i.15985>, Alkishe et al. (2022)
<doi:10.5194/we-22-33-2022>, and Leroy et al. (2015)
<doi:10.1111/ecog.01388>.

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
