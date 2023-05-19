%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Morphoscape
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Computation and Visualization of Adaptive Landscapes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-spatial 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-alphahull 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-spatial 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-alphahull 

%description
Implements adaptive landscape methods first described by Polly et al.
(2016) <doi:10.1080/02724634.2016.1111225> for the integration, analysis
and visualization of biological trait data on a phenotypic morphospace -
typically defined by shape metrics.

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
