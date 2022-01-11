%global __brp_check_rpaths %{nil}
%global packname  GEInfo
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gene-Environment Interaction Analysis Incorporating Prior Information

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pheatmap 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Realize three approaches for Gene-Environment interaction analysis. All of
them adopt Sparse Group Minimax Concave Penalty to identify important G
variables and G-E interactions, and simultaneously respect the hierarchy
between main G and G-E interaction effects. All the three approaches are
available for Linear, Logistic, and Poisson regression. Also realize to
mine and construct prior information for G variables and G-E interactions.

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
