%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glober
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Functions with Multivariate B-Splines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-genlasso 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-genlasso 
Requires:         R-CRAN-fda 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 

%description
Generalized LassO applied to knot selection in multivariate B-splinE
Regression (GLOBER) implements a novel approach for estimating functions
in a multivariate nonparametric regression model based on an adaptive knot
selection for B-splines using the Generalized Lasso. For further details
we refer the reader to the paper Savino, M. E. and Lévy-Leduc, C. (2023),
<arXiv:2306.00686>.

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
