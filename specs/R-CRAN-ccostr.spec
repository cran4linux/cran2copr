%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ccostr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Mean Costs in Censored Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rdpack 

%description
Implementation of estimators for inferring the mean of censored cost data.
Including the estimators BT from Bang and Tsiatis (2000)
<doi:10.1093/biomet/87.2.329> and ZT from Zhao and Tian (2001)
<doi:10.1111/j.0006-341X.2001.01002.x>.

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
