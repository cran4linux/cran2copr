%global __brp_check_rpaths %{nil}
%global packname  TrenchR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Microclimate and Biophysical Ecology

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-msm 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
Tools for translating environmental change into organismal response.
Microclimate models to vertically scale weather station data to organismal
heights. The biophysical modeling tools include both general models for
heat flows and specific models to predict body temperatures for a variety
of ectothermic taxa. Additional functions model and temporally partition
air and soil temperatures and solar radiation. Utility functions estimate
the organismal and environmental parameters needed for biophysical
ecology. 'TrenchR' focuses on relatively simple and modular functions so
users can create transparent and flexible biophysical models. Many
functions are derived from Gates (1980) <doi:10.1007/978-1-4612-6024-0>
and Campbell and Norman (1988) <isbn:9780387949376>.

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
