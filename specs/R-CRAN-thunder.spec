%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  thunder
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Computation and Visualisation of Atmospheric Convective Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9.4
BuildRequires:    R-CRAN-aiRthermo 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-Rcpp >= 0.12.9.4
Requires:         R-CRAN-aiRthermo 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 

%description
Allow to compute and visualise convective parameters commonly used in the
operational prediction of severe convective storms. Core algorithm is
based on a highly optimized 'C++' code linked into 'R' via 'Rcpp'. Highly
efficient engine allows to derive thermodynamic and kinematic parameters
from large numerical datasets such as reanalyses or operational Numerical
Weather Prediction models in a reasonable amount of time. Package has been
developed since 2017 by research meteorologists specializing in severe
thunderstorms. The most relevant methods used in the package based on the
following publications Stipanuk (1973)
<https://apps.dtic.mil/sti/pdfs/AD0769739.pdf>, McCann et al. (1994)
<doi:10.1175/1520-0434(1994)009%%3C0532:WNIFFM%%3E2.0.CO;2>, Bunkers et al.
(2000) <doi:10.1175/1520-0434(2000)015%%3C0061:PSMUAN%%3E2.0.CO;2>, Corfidi
et al. (2003) <doi:10.1175/1520-0434(2003)018%%3C0997:CPAMPF%%3E2.0.CO;2>,
Showalter (1953) <doi:10.1175/1520-0477-34.6.250>, Coffer et al. (2019)
<doi:10.1175/WAF-D-19-0115.1>, Gropp and Davenport (2019)
<doi:10.1175/WAF-D-17-0150.1>, Czernecki et al. (2019)
<doi:10.1016/j.atmosres.2019.05.010>, Taszarek et al. (2020)
<doi:10.1175/JCLI-D-20-0346.1>, Sherburn and Parker (2014)
<doi:10.1175/WAF-D-13-00041.1>, Romanic et al. (2022)
<doi:10.1016/j.wace.2022.100474>.

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
