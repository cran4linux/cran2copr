%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tempodisco
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Temporal Discounting Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RWiener 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-RWiener 

%description
Tools for working with temporal discounting data, designed for behavioural
researchers to simplify data cleaning/scoring and model fitting. The
package implements widely used methods such as computing indifference
points from adjusting amount task (Frye et al., 2016,
<doi:10.3791/53584>), testing for non-systematic discounting per the
criteria of Johnson & Bickel (2008, <doi:10.1037/1064-1297.16.3.264>),
scoring questionnaires according to the methods of Kirby et al. (1999,
<doi:10.1037//0096-3445.128.1.78>) and Wileyto et al (2004,
<doi:10.3758/BF03195548>), Bayesian model selection using a range of
discount functions (Franck et al., 2015, <doi:10.1002/jeab.128>), drift
diffusion models of discounting (Peters & D'Esposito, 2020,
<doi:10.1371/journal.pcbi.1007615>), and model-agnostic measures of
discounting such as area under the curve (Myerson et al., 2001,
<doi:10.1901/jeab.2001.76-235>) and ED50 (Yoon & Higgins, 2008,
<doi:10.1016/j.drugalcdep.2007.12.011>).

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
