%global __brp_check_rpaths %{nil}
%global packname  ClimProjDiags
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Set of Tools to Compute Various Climate Indices

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiApply >= 2.0.0
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-climdex.pcic 
BuildRequires:    R-stats 
Requires:         R-CRAN-multiApply >= 2.0.0
Requires:         R-CRAN-PCICt 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-climdex.pcic 
Requires:         R-stats 

%description
Set of tools to compute metrics and indices for climate analysis. The
package provides functions to compute extreme indices, evaluate the
agreement between models and combine theses models into an ensemble.
Multi-model time series of climate indices can be computed either after
averaging the 2-D fields from different models provided they share a
common grid or by combining time series computed on the model native grid.
Indices can be assigned weights and/or combined to construct new indices.

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
