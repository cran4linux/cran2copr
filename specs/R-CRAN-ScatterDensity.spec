%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ScatterDensity
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Density Estimation and Visualization of 2D Scatter Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pracma 

%description
The user has the option to utilize the two-dimensional density estimation
techniques called smoothed density published by Eilers and Goeman (2004)
<doi:10.1093/bioinformatics/btg454>, and pareto density which was
evaluated for univariate data by Thrun, Gehlert and Ultsch, 2020
<doi:10.1371/journal.pone.0238835>. Moreover, it provides visualizations
of the density estimation in the form of two-dimensional scatter plots in
which the points are color-coded based on increasing density. Colors are
defined by the one-dimensional clustering technique called 1D distribution
cluster algorithm (DDCAL) published by Lux and Rinderle-Ma (2023)
<doi:10.1007/s00357-022-09428-6>.

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
