%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BT
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          (Adaptive) Boosting Trees Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
Requires:         R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 

%description
Performs (Adaptive) Boosting Trees for Poisson distributed response
variables, using log-link function. The code approach is similar to the
one used in 'gbm'/'gbm3'. Moreover, each tree in the expansion is built
thanks to the 'rpart' package. This package is based on following books
and articles Denuit, M., Hainaut, D., Trufin, J. (2019)
<doi:10.1007/978-3-030-25820-7> Denuit, M., Hainaut, D., Trufin, J. (2019)
<doi:10.1007/978-3-030-57556-4> Denuit, M., Hainaut, D., Trufin, J. (2019)
<doi:10.1007/978-3-030-25827-6> Denuit, M., Hainaut, D., Trufin, J. (2022)
<doi:10.1080/03461238.2022.2037016> Denuit, M., Huyghe, J., Trufin, J.
(2022)
<https://dial.uclouvain.be/pr/boreal/fr/object/boreal%%3A244325/datastream/PDF_01/view>
Denuit, M., Trufin, J., Verdebout, T. (2022)
<https://dial.uclouvain.be/pr/boreal/fr/object/boreal%%3A268577>.

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
