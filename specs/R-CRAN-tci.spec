%global packname  tci
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Target Controlled Infusion (TCI)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape 

%description
Implementation of target-controlled infusion algorithms for compartmental
pharmacokinetic and pharmacokinetic-pharmacodynamic models. Jacobs (1990)
<doi:10.1109/10.43622>; Marsh et al. (1991) <doi:10.1093/bja/67.1.41>;
Shafer and Gregg (1993) <doi:10.1007/BF01070999>; Schnider et al. (1998)
<doi:10.1097/00000542-199805000-00006>; Abuhelwa, Foster, and Upton (2015)
<doi:10.1016/j.vascn.2015.03.004>; Eleveld et al. (2018)
<doi:10.1016/j.bja.2018.01.018>.

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
