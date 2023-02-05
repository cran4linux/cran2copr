%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuantileGH
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Least Mahalanobis Distance Estimator for Tukey g-&-h Mixture

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-rstpm2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tclust 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-goftest 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-rstpm2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tclust 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-sn 

%description
Functions for simulation, estimation, and model selection of finite
mixtures of Tukey's g-and-h distributions.

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
