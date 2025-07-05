%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  equatiomatic
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Transform Models into 'LaTeX' Equations

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-broom >= 0.7.0
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-broom >= 0.7.0
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-knitr 
Requires:         R-stats 
Requires:         R-utils 

%description
The goal of 'equatiomatic' is to reduce the pain associated with writing
'LaTeX' formulas from fitted models. The primary function of the package,
extract_eq(), takes a fitted model object as its input and returns the
corresponding 'LaTeX' code for the model.

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
