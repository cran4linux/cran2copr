%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mgwnbr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiscale Geographically Weighted Negative Binomial Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-sp 

%description
Fits a geographically weighted regression model with different scales for
each covariate. Uses the negative binomial distribution as default, but
also accepts the normal, Poisson, or logistic distributions. Can fit the
global versions of each regression and also the geographically weighted
alternatives with only one scale, since they are all particular cases of
the multiscale approach. Hanchen Yu (2024). "Exploring Multiscale
Geographically Weighted Negative Binomial Regression", Annals of the
American Association of Geographers <doi:10.1080/24694452.2023.2289986>.
Fotheringham AS, Yang W, Kang W (2017). "Multiscale Geographically
Weighted Regression (MGWR)", Annals of the American Association of
Geographers <doi:10.1080/24694452.2017.1352480>. Da Silva AR, Rodrigues
TCV (2014). "Geographically Weighted Negative Binomial Regression -
incorporating overdispersion", Statistics and Computing
<doi:10.1007/s11222-013-9401-9>.

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
