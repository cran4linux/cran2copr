%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtwSat
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Weighted Dynamic Time Warping for Satellite Image Time Series Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-twdtw 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-twdtw 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-proxy 

%description
Provides a robust approach to land use mapping using multi-dimensional
(multi-band) satellite image time series. By leveraging the Time-Weighted
Dynamic Time Warping (TWDTW) distance metric in tandem with a 1
Nearest-Neighbor (1-NN) Classifier, this package offers functions to
produce land use maps based on distinct seasonality patterns, commonly
observed in the phenological cycles of vegetation. The approach is
described in Maus et al. (2016) <doi:10.1109/JSTARS.2016.2517118> and Maus
et al. (2019) <doi:10.18637/jss.v088.i05>. A primary advantage of TWDTW is
its capability to handle irregularly sampled and noisy time series, while
also requiring minimal training sets. The package includes tools for
training the 1-NN-TWDTW model, visualizing temporal patterns, producing
land use maps, and visualizing the results.

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
