%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hyper.gam
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Additive Models with Hyper Column

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5
Requires:         R-core >= 4.5
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-groupedHyperframe 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nlme 
Requires:         R-parallel 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-groupedHyperframe 

%description
Generalized additive models with a numeric hyper column tabulated on a
common grid. Sign-adjustment based on the correlation of model prediction
and a selected slice of the hyper column. Visualization of the integrand
surface over the hyper column.

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
