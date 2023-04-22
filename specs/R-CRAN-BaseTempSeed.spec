%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BaseTempSeed
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Seed Germination Base Temperature in Thermal Modelling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-NlcOptim 
Requires:         R-stats 
Requires:         R-CRAN-NlcOptim 

%description
All the seeds do not germinate at a single point in time due to
physiological mechanisms determined by temperature which vary among
individual seeds in the population. Seeds germinate by following
accumulation of thermal time in degree days/hours, quantified by
multiplying the time of germination with excess of base temperature
required by each seed for its germination, which follows log-normal
distribution. The theoretical germination course can be obtained by
regressing the rate of germination at various fractions against
temperature (Garcia et al., 1982), where the fraction-wise regression
lines intersect the temperature axis at base temperature and the
methodology of determining optimum base temperature has been described by
Ellis et al. (1987). This package helps to find the base temperature of
seed germination using algorithms of Garcia et al. (1982) and Ellis et al.
(1982) <doi:10.1093/JXB/38.6.1033> <doi:10.1093/jxb/33.2.288>.

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
