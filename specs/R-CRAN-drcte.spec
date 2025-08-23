%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drcte
%global packver   1.0.65
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.65
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Approaches for Time-to-Event Data in Agriculture

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-drc 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-drc 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-nor1mix 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-car 

%description
A specific and comprehensive framework for the analyses of time-to-event
data in agriculture. Fit non-parametric and parametric time-to-event
models. Compare time-to-event curves for different experimental groups.
Plots and other displays. It is particularly tailored to the analyses of
data from germination and emergence assays. The methods are described in
Onofri et al. (2022) "A unified framework for the analysis of germination,
emergence, and other time-to-event data in weed science", Weed Science,
70, 259-271 <doi:10.1017/wsc.2022.8>.

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
