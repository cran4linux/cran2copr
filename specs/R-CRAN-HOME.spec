%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HOME
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Harmonized Orphanhood Mortality Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
Implements indirect demographic methods for estimating adult mortality
from orphanhood data. The package includes the standard Brass and Hill
(1973) method
<https://scholar.google.com/scholar_lookup?&title=Estimating%%20Adult%%20Mortality%%20from%%20Orphanhood&pages=111-23&publication_year=1973&author=Brass%%2CW.&author=Hill.%%2CK.>,
the regression-based approach developed by Timaeus (1992)
<https://pubmed.ncbi.nlm.nih.gov/12317481/>, and the adjustments proposed
by Luy (2012) <doi:10.1007/s13524-012-0101-4> for low-mortality
populations. A relational model is used to harmonize estimates into
comparable adult mortality indicators. The package also provides
diagnostic tools to assess the sensitivity of results to assumptions about
the mean age of childbearing and the choice of model life table family.

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
