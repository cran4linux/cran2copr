%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  estimators
%global packver   0.8.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.5
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements estimation methods for parameters of common distribution
families. The common d, p, q, r function family for each distribution is
enriched with the ll, e, and v counterparts, computing the log-likelihood,
performing estimation, and calculating the asymptotic variance -
covariance matrix, respectively. Parameter estimation is performed
analytically whenever possible.

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
