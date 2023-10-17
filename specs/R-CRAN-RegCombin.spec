%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RegCombin
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Partially Linear Regression under Data Combination

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-RationalExp 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-RationalExp 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-pracma 

%description
We implement linear regression when the outcome of interest and some of
the covariates are observed in two different datasets that cannot be
linked, based on D'Haultfoeuille, Gaillac, Maurel (2022)
<doi:10.3386/w29953>. The package allows for common regressors observed in
both datasets, and for various shape constraints on the effect of
covariates on the outcome of interest. It also provides the tools to
perform a test of point identification. See the associated vignette
<https://github.com/cgaillac/RegCombin/blob/master/RegCombin_vignette.pdf>
for theory and code examples.

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
