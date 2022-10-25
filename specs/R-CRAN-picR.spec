%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  picR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Information Criteria for Model Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Computation of predictive information criteria (PIC) from select model
object classes for model selection in predictive contexts. In contrast to
the more widely used Akaike Information Criterion (AIC), which are derived
under the assumption that target(s) of prediction (i.e. validation data)
are independently and identically distributed to the fitting data, the PIC
are derived under less restrictive assumptions and thus generalize AIC to
the more practically relevant case of training/validation data
heterogeneity. The methodology featured in this package is based on Flores
(2021)
<https://iro.uiowa.edu/esploro/outputs/doctoral/A-new-class-of-information-criteria/9984097169902771?institution=01IOWA_INST>
"A new class of information criteria for improved prediction in the
presence of training/validation data heterogeneity".

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
