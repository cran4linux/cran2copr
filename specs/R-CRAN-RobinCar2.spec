%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobinCar2
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          ROBust INference for Covariate Adjustment in Randomized Clinical Trials

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 

%description
Performs robust estimation and inference when using covariate adjustment
and/or covariate-adaptive randomization in randomized controlled trials.
This package is trimmed to reduce the dependencies and validated to be
used across industry. See "FDA's final guidance on covariate
adjustment"<https://www.regulations.gov/docket/FDA-2019-D-0934>, Tsiatis
(2008) <doi:10.1002/sim.3113>, Bugni et al. (2018)
<doi:10.1080/01621459.2017.1375934>, Ye, Shao, Yi, and Zhao
(2023)<doi:10.1080/01621459.2022.2049278>, Ye, Shao, and Yi
(2022)<doi:10.1093/biomet/asab015>, Rosenblum and van der Laan
(2010)<doi:10.2202/1557-4679.1138>, Wang et al.
(2021)<doi:10.1080/01621459.2021.1981338>, Ye, Bannick, Yi, and Shao
(2023)<doi:10.1080/24754269.2023.2205802>, and Bannick, Shao, Liu, Du, Yi,
and Ye (2024)<doi:10.48550/arXiv.2306.10213>.

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
