%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  texreg
%global packver   1.39.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.39.4
Release:          1%{?dist}%{?buildtag}
Summary:          Conversion of R Regression Output to LaTeX or HTML Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       pandoc
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-httr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-httr 

%description
Converts coefficients, standard errors, significance stars, and
goodness-of-fit statistics of statistical models into LaTeX tables or HTML
tables/MS Word documents or to nicely formatted screen output for the R
console for easy model comparison. A list of several models can be
combined in a single table. The output is highly customizable. New model
types can be easily implemented. Details can be found in Leifeld (2013),
JStatSoft <doi:10.18637/jss.v055.i08>.)

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
