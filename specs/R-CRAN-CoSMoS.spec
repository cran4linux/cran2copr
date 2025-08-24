%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoSMoS
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Complete Stochastic Modelling Solution

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-MBA 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mAr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-ggquiver 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-MBA 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mAr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-ggquiver 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-plot3D 

%description
Makes univariate, multivariate, or random fields simulations precise and
simple. Just select the desired time series or random fields’ properties
and it will do the rest. CoSMoS is based on the framework described in
Papalexiou (2018, <doi:10.1016/j.advwatres.2018.02.013>), extended for
random fields in Papalexiou and Serinaldi (2020,
<doi:10.1029/2019WR026331>), and further advanced in Papalexiou et al.
(2021, <doi:10.1029/2020WR029466>) to allow fine-scale space-time
simulation of storms (or even cyclone-mimicking fields).

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
