%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CensSpatial
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Censored Spatial Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-optimx >= 2021.10.12
BuildRequires:    R-CRAN-numDeriv >= 2.11.1
BuildRequires:    R-CRAN-geoR >= 1.8.1
BuildRequires:    R-CRAN-tmvtnorm >= 1.4
BuildRequires:    R-CRAN-tlrmvnmvt >= 1.1.0
BuildRequires:    R-CRAN-moments >= 0.14
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-optimx >= 2021.10.12
Requires:         R-CRAN-numDeriv >= 2.11.1
Requires:         R-CRAN-geoR >= 1.8.1
Requires:         R-CRAN-tmvtnorm >= 1.4
Requires:         R-CRAN-tlrmvnmvt >= 1.1.0
Requires:         R-CRAN-moments >= 0.14
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-lattice 

%description
It fits linear regression models for censored spatial data. It provides
different estimation methods as the SAEM (Stochastic Approximation of
Expectation Maximization) algorithm and seminaive that uses Kriging
prediction to estimate the response at censored locations and predict new
values at unknown locations. It also offers graphical tools for assessing
the fitted model. More details can be found in Ordonez et al. (2018)
<doi:10.1016/j.spasta.2017.12.001>.

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
