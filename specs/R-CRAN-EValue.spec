%global __brp_check_rpaths %{nil}
%global packname  EValue
%global packver   4.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sensitivity Analyses for Unmeasured Confounding and Other Biases in Observational Studies and Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MetaUtility 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-metafor 
Requires:         R-methods 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MetaUtility 
Requires:         R-CRAN-dplyr 

%description
Conducts sensitivity analyses for unmeasured confounding, selection bias,
and measurement error (individually or in combination; VanderWeele & Ding
(2017) <doi:10.7326/M16-2607>; Smith & VanderWeele (2019)
<doi:10.1097/EDE.0000000000001032>; VanderWeele & Li (2019)
<doi:10.1093/aje/kwz133>; Smith & VanderWeele (2021) <arXiv:2005.02908>).
Also conducts sensitivity analyses for unmeasured confounding in
meta-analyses (Mathur & VanderWeele (2020a)
<doi:10.1080/01621459.2018.1529598>; Mathur & VanderWeele (2020b)
<doi:10.1097/EDE.0000000000001180>) and for additive measures of effect
modification (Mathur et al., under review).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
