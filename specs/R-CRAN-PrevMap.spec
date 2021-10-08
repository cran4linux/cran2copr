%global __brp_check_rpaths %{nil}
%global packname  PrevMap
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Geostatistical Modelling of Spatially Referenced Prevalence Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-truncnorm 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 

%description
Provides functions for both likelihood-based and Bayesian analysis of
spatially referenced prevalence data. For a tutorial on the use of the R
package, see Giorgi and Diggle (2017) <doi:10.18637/jss.v078.i08>.

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
