%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mitey
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Serial Interval and Case Reproduction Number Estimation

License:          EUPL-1.2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 

%description
Provides methods to estimate serial intervals and time-varying case
reproduction numbers from infectious disease outbreak data. Serial
intervals measure the time between symptom onset in linked transmission
pairs, while case reproduction numbers quantify how many secondary cases
each infected individual generates over time. These parameters are
essential for understanding transmission dynamics, evaluating control
measures, and informing public health responses. The package implements
the maximum likelihood framework from Vink et al. (2014)
<doi:10.1093/aje/kwu209> for serial interval estimation and the
retrospective method from Wallinga & Lipsitch (2007)
<doi:10.1098/rspb.2006.3754> for reproduction number estimation.
Originally developed for scabies transmission analysis but applicable to
other infectious diseases including influenza, COVID-19, and emerging
pathogens. Designed for epidemiologists, public health researchers, and
infectious disease modelers working with outbreak surveillance data.

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
