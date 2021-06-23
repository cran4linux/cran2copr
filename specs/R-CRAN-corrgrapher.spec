%global __brp_check_rpaths %{nil}
%global packname  corrgrapher
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Explore Correlations Between Variables in a Machine Learning Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-ingredients 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-ingredients 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 

%description
When exploring data or models we often examine variables one by one. This
analysis is incomplete if the relationship between these variables is not
taken into account. The 'corrgrapher' package facilitates simultaneous
exploration of the Partial Dependence Profiles and the correlation between
variables in the model. The package 'corrgrapher' is a part of the
'DrWhy.AI' universe.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
