%global __brp_check_rpaths %{nil}
%global packname  SDALGCP
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Discrete Approximation to Log-Gaussian Cox Processes for Aggregated Disease Count Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-mapview >= 2.6.0
BuildRequires:    R-CRAN-splancs >= 2.1.40
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-geoR >= 1.7.5.2.1
BuildRequires:    R-CRAN-PrevMap >= 1.4.1
BuildRequires:    R-CRAN-sp >= 1.2.7
BuildRequires:    R-CRAN-spacetime >= 1.2.2
BuildRequires:    R-CRAN-Matrix >= 1.2.14
BuildRequires:    R-CRAN-pdist >= 1.2
BuildRequires:    R-CRAN-progress >= 1.1.2
BuildRequires:    R-CRAN-maptools >= 1.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-mapview >= 2.6.0
Requires:         R-CRAN-splancs >= 2.1.40
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-geoR >= 1.7.5.2.1
Requires:         R-CRAN-PrevMap >= 1.4.1
Requires:         R-CRAN-sp >= 1.2.7
Requires:         R-CRAN-spacetime >= 1.2.2
Requires:         R-CRAN-Matrix >= 1.2.14
Requires:         R-CRAN-pdist >= 1.2
Requires:         R-CRAN-progress >= 1.1.2
Requires:         R-CRAN-maptools >= 1.1.1
Requires:         R-methods 
Requires:         R-CRAN-spatstat.geom 

%description
Provides a computationally efficient discrete approximation to
log-Gaussian Cox process model for spatially aggregated disease count
data. It uses Monte Carlo Maximum Likelihood for model parameter
estimation as proposed by Christensen (2004) <doi: 10.1198/106186004X2525>
and delivers prediction of spatially discrete and continuous relative
risk. It performs inference for static spatial and spatio-temporal
dataset. The details of the methods are provided in Johnson et al (2019)
<doi:10.1002/sim.8339>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
