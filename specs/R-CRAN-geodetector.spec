%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geodetector
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified Heterogeneity Measure, Dominant Driving Force Detection, Interaction Relationship Investigation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Spatial stratified heterogeneity (SSH), referring to the within strata are
more similar than the between strata, a model with global parameters would
be confounded if input data is SSH. Note that the "spatial" here can be
either geospatial or the space in mathematical meaning. Geographical
detector is a novel tool to investigate SSH: (1) measure and find SSH of a
variable Y; (2) test the power of determinant X of a dependent variable Y
according to the consistency between their spatial distributions; and (3)
investigate the interaction between two explanatory variables X1 and X2 to
a dependent variable Y (Wang et al 2014 <doi:10.1080/13658810802443457>,
Wang, Zhang, and Fu 2016 <doi:10.1016/j.ecolind.2016.02.052>).

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
