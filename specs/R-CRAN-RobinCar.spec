%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RobinCar
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Inference for Covariate Adjustment in Randomized Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-emulator 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-AIPW 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-emulator 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-tidyverse 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-AIPW 
Requires:         R-CRAN-MASS 

%description
Performs robust estimation and inference when using covariate adjustment
and/or covariate-adaptive randomization in randomized clinical trials.
Ting Ye, Jun Shao, Yanyao Yi, Qinyuan Zhao (2023)
<doi:10.1080/01621459.2022.2049278>. Ting Ye, Marlena Bannick, Yanyao Yi,
Jun Shao (2023) <doi:10.1080/24754269.2023.2205802>. Ting Ye, Jun Shao,
Yanyao Yi (2023) <doi:10.1093/biomet/asad045>. Marlena Bannick, Jun Shao,
Jingyi Liu, Yu Du, Yanyao Yi, Ting Ye (2024) <doi:10.1093/biomet/asaf029>.
Xiaoyu Qiu, Yuhan Qian, Jaehwan Yi, Jinqiu Wang, Yu Du, Yanyao Yi, Ting Ye
(2025) <doi:10.48550/arXiv.2408.12541>.

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
