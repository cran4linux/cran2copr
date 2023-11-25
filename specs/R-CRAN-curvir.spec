%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  curvir
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Specify Reserve Demand Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-qgam 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-qgam 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-randomForest 

%description
Automatic specification and estimation of reserve demand curves for
central bank operations. The package can help to choose the best demand
curve and identify additional explanatory variables. Various plot and
predict options are included. For more details, see Chen et al. (2023)
<https://www.imf.org/en/Publications/WP/Issues/2023/09/01/Modeling-the-Reserve-Demand-to-Facilitate-Central-Bank-Operations-538754>.

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
