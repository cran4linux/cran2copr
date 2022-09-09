%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mglasso
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multiscale Graphical Lasso

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.25
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-reticulate >= 1.25
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rstudioapi 

%description
Inference of Multiscale graphical models with neighborhood selection
approach.  The method is based on solving a convex optimization problem
combining a Lasso and fused-group Lasso penalties.  This allows to infer
simultaneously a conditional independence graph and a clustering
partition. The optimization is based on the Continuation with Nesterov
smoothing in a Shrinkage-Thresholding Algorithm solver (Hadj-Selem et al.
2018) <doi:10.1109/TMI.2018.2829802> implemented in python.

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
