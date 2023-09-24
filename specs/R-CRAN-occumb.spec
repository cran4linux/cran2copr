%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  occumb
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Site Occupancy Modeling for Environmental DNA Metabarcoding

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jagsUI 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-jagsUI 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-knitr 

%description
Fits multispecies site occupancy models to environmental DNA metabarcoding
data collected using spatially-replicated survey design. Model fitting
results can be used to evaluate and compare the effectiveness of species
detection to find an efficient survey design. Reference: Fukaya et al.
(2022) <doi:10.1111/2041-210X.13732>.

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
