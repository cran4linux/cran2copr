%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AddiVortes
%global packver   0.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          (Bayesian) Additive Voronoi Tessellations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel >= 4.0.0
BuildRequires:    R-CRAN-pbapply >= 1.6
Requires:         R-parallel >= 4.0.0
Requires:         R-CRAN-pbapply >= 1.6

%description
Implements the Bayesian Additive Voronoi Tessellation model for
non-parametric regression and machine learning as introduced in Stone and
Gosling (2025) <doi:10.1080/10618600.2024.2414104>. This package provides
a flexible alternative to BART (Bayesian Additive Regression Trees) using
Voronoi tessellations instead of trees. Users can fit Bayesian regression
models, estimate posterior distributions, and visualise the resulting
tessellations. It is particularly useful for spatial data analysis,
machine learning regression, complex function approximation and Bayesian
modeling where the underlying structure is unknown. The method is
well-suited to capturing spatial patterns and non-linear relationships.

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
