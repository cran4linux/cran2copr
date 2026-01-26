%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mrangr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mechanistic Metacommunity Simulator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-FieldSimR 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rangr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-FieldSimR 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gstat 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-parallel 
Requires:         R-CRAN-rangr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Flexible, mechanistic, and spatially explicit simulator of
metacommunities. It extends our previous package - 'rangr' (see
<https://github.com/ropensci/rangr>), which implemented a mechanistic
virtual species simulator integrating population dynamics and dispersal.
The 'mrangr' package adds the ability to simulate multiple species
interacting through an asymmetric matrix of pairwise relationships,
allowing users to model all types of biotic interactions — competitive,
facilitative, or neutral — within spatially explicit virtual environments.
This work was supported by the National Science Centre, Poland, grant no.
2018/29/B/NZ8/00066 and the Poznań Supercomputing and Networking Centre
(grant no. pl0090-01).

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
