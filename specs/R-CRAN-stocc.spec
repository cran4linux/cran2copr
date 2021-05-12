%global packname  stocc
%global packver   1.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.31
Release:          1%{?dist}%{?buildtag}
Summary:          Fit a Spatial Occupancy Model via Gibbs Sampling

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rARPACK 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rARPACK 

%description
Fit a spatial-temporal occupancy models using a probit formulation instead
of a traditional logit model.

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
