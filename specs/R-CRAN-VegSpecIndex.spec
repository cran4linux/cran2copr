%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VegSpecIndex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vegetation and Spectral Indices for Environmental Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Earth system dynamics, such as plant dynamics, water bodies, and fire
regimes, are widely monitored using spectral indicators obtained from
multispectral remote sensing products. There is a great need for spectral
index catalogues and computing tools as a result of the quick rise of
suggested spectral indices. Unfortunately, the majority of these resources
lack a standard Application Programming Interface, are out-of-date,
closed-source, or are not linked to a catalogue. We now introduce
'VegSpecIndex', a standardised list of spectral indices for studies of the
earth system. A thorough inventory of spectral indices is offered by
'VegSpecIndex' and is connected to an R library. For every spectral index,
'VegSpecIndex' provides a comprehensive collection of information, such as
names, formulae, and source references. The user community may add more
items to the catalogue, which will keep 'VegSpecIndex' up to date and
allow for further scientific uses. Additionally, the R library makes it
possible to apply the catalogue to actual data, which makes it easier to
employ remote sensing resources effectively across a variety of Earth
system domains.

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
