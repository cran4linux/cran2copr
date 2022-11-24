%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  marginaleffects
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Marginal Effects, Marginal Means, Predictions, and Contrasts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 0.18.5
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
Requires:         R-CRAN-insight >= 0.18.5
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-generics 
Requires:         R-methods 

%description
Compute and plot adjusted predictions, contrasts, marginal effects, and
marginal means for over 70 classes of statistical models in R. Conduct
linear and non-linear hypothesis tests using the delta method.

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
