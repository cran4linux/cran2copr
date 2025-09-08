%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AuxSurvey
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Survey Analysis with Auxiliary Discretized Variables

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-rstanarm 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 

%description
Probability surveys often use auxiliary continuous data from
administrative records, but the utility of this data is diminished when it
is discretized for confidentiality. We provide a set of survey estimators
to make full use of information from the discretized variables. See
Williams, S.Z., Zou, J., Liu, Y., Si, Y., Galea, S. and Chen, Q. (2024),
Improving Survey Inference Using Administrative Records Without Releasing
Individual-Level Continuous Data. Statistics in Medicine, 43: 5803-5813.
<doi:10.1002/sim.10270> for details.

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
