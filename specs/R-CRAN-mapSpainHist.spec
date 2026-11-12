%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mapSpainHist
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Historical Municipal Boundaries of Spain (1900-2001)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-sf 
Requires:         R-tools 
Requires:         R-utils 

%description
Municipal boundaries of Spain for each population census between 1900 and
2001, together with provinces, judicial districts and electoral districts
(Cortes of the Restoration in 1920 and constituencies of the Second
Republic in 1931, 1933 and 1936) built from them, and the census figures
of every municipality from 1842 to 2011. All maps derive from a single
partition of the territory, so they have no gaps or overlaps and can be
aggregated consistently. Boundaries of historical municipalities are an
approximate reconstruction. Geometries are downloaded from 'Zenodo'
<doi:10.5281/zenodo.23663208> and cached locally.

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
