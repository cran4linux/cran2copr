%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tfNeuralODE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Neural Ordinary Differential Equations with 'tensorflow'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-deSolve 

%description
Provides a framework for the creation and use of Neural ordinary
differential equations with the 'tensorflow' and 'keras' packages. The
idea of Neural ordinary differential equations comes from Chen et al.
(2018) <doi:10.48550/arXiv.1806.07366>, and presents a novel way of
learning and solving differential systems.

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
