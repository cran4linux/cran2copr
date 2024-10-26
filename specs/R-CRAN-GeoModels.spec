%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeoModels
%global packver   2.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Procedures for Gaussian and Non Gaussian Geostatistical (Large) Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-dotCall64 
BuildRequires:    R-CRAN-FastGP 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-nabor 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-minqa 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-codetools 
Requires:         R-methods 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-dotCall64 
Requires:         R-CRAN-FastGP 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-zipfR 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-nabor 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-minqa 

%description
Functions for Gaussian and Non Gaussian (bivariate) spatial and
spatio-temporal data analysis are provided for a) (fast) simulation of
random fields, b) inference for random fields using standard likelihood
and a likelihood approximation method called weighted composite likelihood
based on pairs and b) prediction using (local) best linear unbiased
prediction. Weighted composite likelihood can be very efficient for
estimating massive datasets. Both regression and spatial (temporal)
dependence analysis can be jointly performed. Flexible covariance models
for spatial and spatial-temporal data on Euclidean domains and spheres are
provided. There are also many useful functions for plotting and performing
diagnostic analysis. Different non Gaussian random fields can be
considered in the analysis. Among them, random fields with marginal
distributions such as Skew-Gaussian, Student-t, Tukey-h, Sin-Arcsin,
Two-piece, Weibull, Gamma, Log-Gaussian, Binomial, Negative Binomial and
Poisson. See the URL for the papers associated with this package, as for
instance, Bevilacqua and Gaetan (2015) <doi:10.1007/s11222-014-9460-6>,
Bevilacqua et al. (2016) <doi:10.1007/s13253-016-0256-3>, Vallejos et al.
(2020) <doi:10.1007/978-3-030-56681-4>, Bevilacqua et. al (2020)
<doi:10.1002/env.2632>, Bevilacqua et. al (2021) <doi:10.1111/sjos.12447>,
Bevilacqua et al. (2022) <doi:10.1016/j.jmva.2022.104949>,
Morales-Navarrete et al. (2023) <doi:10.1080/01621459.2022.2140053>, and a
large class of examples and tutorials.

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
