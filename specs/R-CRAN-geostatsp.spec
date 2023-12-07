%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geostatsp
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Geostatistical Modelling with Likelihood and Bayes

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.6.2
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix >= 1.6.2
Requires:         R-CRAN-terra 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-stats 

%description
Geostatistical modelling facilities using 'SpatRaster' and 'SpatVector'
objects are provided. Non-Gaussian models are fit using 'INLA', and
Gaussian geostatistical models use Maximum Likelihood Estimation.  For
details see Brown (2015) <doi:10.18637/jss.v063.i12>. The 'RandomFields'
package is available at
<https://www.wim.uni-mannheim.de/schlather/publications/software>.

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
