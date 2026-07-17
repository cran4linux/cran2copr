%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuantileGH
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantile Least Mahalanobis Distance Estimator for Tukey g-&-h Mixture

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6
Requires:         R-core >= 4.6
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-cli 

%description
Functions for simulation, estimation, and model selection of finite
mixtures of Tukey g-and-h distributions.  The author has retired from
academic research. Accordingly, this package should not be considered a
validated tool for use in peer-reviewed publications or as the basis for
grant applications. Backward compatibility with user-code published in
<doi:10.1007/s11222-025-10596-9> is not maintained in versions >= 0.3.0
(July 2026) of this package. The authors of those publications are the
appropriate contacts for reproducibility inquiries.

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
