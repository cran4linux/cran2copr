%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppmSuite
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Models that Employ Product Partition Distributions as a Prior on Partitions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-Matrix 

%description
Provides a suite of functions that fit models that use PPM type priors for
partitions. Models include hierarchical Gaussian and probit ordinal models
with a (covariate dependent) PPM.  If a covariate dependent product
partition model is selected, then all the options detailed in Page, G.L.;
Quintana, F.A. (2018) <doi:10.1007/s11222-017-9777-z> are available.  If
covariate values are missing, then the approach detailed in Page, G.L.;
Quintana, F.A.; Mueller, P (2020) <doi:10.1080/10618600.2021.1999824> is
employed.  Also included in the package is a function that fits a Gaussian
likelihood spatial product partition model that is detailed in Page, G.L.;
Quintana, F.A. (2016) <doi:10.1214/15-BA971>, and multivariate PPM change
point models that are detailed in Quinlan, J.J.; Page, G.L.; Castro, L.M.
(2023) <doi:10.1214/22-BA1344>.

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
