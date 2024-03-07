%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  accessibility
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Transport Accessibility Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-utils 

%description
A set of fast and convenient functions to help conducting accessibility
analyses. Given a pre-computed travel cost matrix and a land use dataset
(containing the location of jobs, healthcare and population, for example),
the package allows one to calculate accessibility levels and accessibility
poverty and inequality. The package covers the majority of the most
commonly used accessibility measures (such as cumulative opportunities,
gravity-based and floating catchment areas methods), as well as the most
frequently used inequality and poverty metrics (such as the Palma ratio,
the concentration and Theil indices and the FGT family of measures).

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
