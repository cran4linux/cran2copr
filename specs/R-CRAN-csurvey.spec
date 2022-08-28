%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csurvey
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Regression for Survey Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-survey >= 3.36
BuildRequires:    R-CRAN-cgam >= 1.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-CRAN-survey >= 3.36
Requires:         R-CRAN-cgam >= 1.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-coneproj 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
Domain mean estimation with monotonicity or block monotone constraints.
See Xu X, Meyer MC and Opsomer JD (2021)<doi:10.1016/j.jspi.2021.02.004>
for more details.

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
