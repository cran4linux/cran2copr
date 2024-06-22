%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpatFD
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Geostatistics: Univariate and Multivariate Functional Spatial Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-fda.usc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-geoR 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-fda.usc 

%description
Performance of functional kriging, cokriging, optimal sampling and
simulation for spatial prediction of functional data. The framework of
spatial prediction, optimal sampling and simulation are extended from
scalar to functional data. 'SpatFD' is based on the Karhunen-Loève
expansion that allows to represent the observed functions in terms of its
empirical functional principal components. Based on this approach, the
functional auto-covariances and cross-covariances required for spatial
functional predictions and optimal sampling, are completely determined by
the sum of the spatial auto-covariances and cross-covariances of the
respective score components. The package provides new classes of data and
functions for modeling spatial dependence structure among curves. The
spatial prediction of curves at unsampled locations can be carried out
using two types of predictors, and both of them report, the respective
variances of the prediction error. In addition, there is a function for
the determination of spatial locations sampling configuration that ensures
minimum variance of spatial functional prediction. There are also two
functions for plotting predicted curves at each location and mapping the
surface at each time point, respectively. References Bohorquez, M.,
Giraldo, R., and Mateu, J. (2016) <doi:10.1007/s10260-015-0340-9>,
Bohorquez, M., Giraldo, R., and Mateu, J. (2016)
<doi:10.1007/s00477-016-1266-y>, Bohorquez M., Giraldo R. and Mateu J.
(2021) <doi:10.1002/9781119387916>.

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
