%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  csurvey
%global packver   1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Regression for Survey Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.1
Requires:         R-core >= 4.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.2.1
BuildRequires:    R-CRAN-cgam >= 1.27
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-zeallot 
Requires:         R-CRAN-survey >= 4.2.1
Requires:         R-CRAN-cgam >= 1.27
Requires:         R-CRAN-coneproj 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-zeallot 

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
