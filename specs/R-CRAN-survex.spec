%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survex
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Explainable Machine Learning in Survival Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX >= 2.2.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kernelshap 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-patchwork 
Requires:         R-CRAN-DALEX >= 2.2.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kernelshap 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-patchwork 

%description
Survival analysis models are commonly used in medicine and other areas.
Many of them are too complex to be interpreted by human. Exploration and
explanation is needed, but standard methods do not give a broad enough
picture. 'survex' provides easy-to-apply methods for explaining survival
models, both complex black-boxes and simpler statistical models. They
include methods specific to survival analysis such as SurvSHAP(t)
introduced in Krzyzinski et al., (2023)
<doi:10.1016/j.knosys.2022.110234>, SurvLIME described in Kovalev et al.,
(2020) <doi:10.1016/j.knosys.2020.106164> as well as extensions of
existing ones described in Biecek et al., (2021)
<doi:10.1201/9780429027192>.

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
