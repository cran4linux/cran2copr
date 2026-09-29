%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FCGR
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fatigue Crack Growth in Reliability

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kerdiest 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-sfsmisc 
Requires:         R-CRAN-kerdiest 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-sfsmisc 

%description
Fatigue Crack Growth in Reliability estimates the distribution of material
lifetime due to mechanical fatigue efforts. The 'FCGR' package provides
simultaneous crack growth curves fitting to different specimens in
materials under mechanical stress efforts. Linear mixed-effects models
with smoothing B-Splines and the linearized Paris-Erdogan law are applied.
Once defined the fail for a determined crack length, the distribution
function of failure times to fatigue is obtained. The density function is
estimated by applying nonparametric binned kernel density estimate
('bkde') and the kernel estimator of the distribution function ('kde').
The results of Pinheiro and Bates method based on nonlinear mixed-effects
regression ('nlme') can be also retrieved. The package contains the
crack.growth(), PLOT.cg(), IB.F(), and Alea.A (database) functions.

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
