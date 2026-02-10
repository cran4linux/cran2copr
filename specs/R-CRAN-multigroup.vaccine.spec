%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multigroup.vaccine
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Outbreak Models of Multi-Group Populations with Vaccination

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib >= 0.9.0
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-socialmixr 
Requires:         R-CRAN-bslib >= 0.9.0
Requires:         R-CRAN-deSolve 
Requires:         R-graphics 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-socialmixr 

%description
Model infectious disease dynamics in populations with multiple subgroups
having different vaccination rates, transmission characteristics, and
contact patterns. Calculate final and intermediate outbreak sizes, form
age-structured contact models with automatic fetching of U.S. census data,
and explore vaccination scenarios with an interactive 'shiny' dashboard
for a model with two subgroups, as described in Nguyen et al. (2024)
<doi:10.1016/j.jval.2024.03.039> and Duong et al. (2026)
<doi:10.1093/ofid/ofaf695.217>.

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
