%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cvpa
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Canadian Voting and Policy Attitudes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nanoparquet 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nanoparquet 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
The main focus of the package is to give weighted party support and issue
attitudes by demographic groups over time. As of 0.2.0, policy-issue and
vote data are read on demand from the cp3 project's hosted Parquet files
(see update_cvpa_data()) rather than bundled with the package, covering
several hundred policy questions across seven issue domains in addition to
vote choice/intention. The vote data are described in Lucas, Romualdi,
Armstrong, and Goodyear-Grant (2025) <doi:10.1017/S0008423925000241>.

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
