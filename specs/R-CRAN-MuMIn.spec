%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MuMIn
%global packver   1.48.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.48.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Model Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-insight 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-insight 

%description
Tools for model selection and model averaging with support for a wide
range of statistical models. Automated model selection through subsets of
the maximum model, with optional constraints for model inclusion.
Averaging of model parameters and predictions based on model weights
derived from information criteria (AICc and alike) or custom model
weighting schemes.

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
