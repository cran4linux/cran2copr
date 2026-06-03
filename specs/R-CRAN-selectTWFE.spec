%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  selectTWFE
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Selection Between TWFE and ETWFE

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-etwfe 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-etwfe 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Estimates both a vanilla two-way fixed effects (TWFE) model and an
extended TWFE (ETWFE) model, then selects between them using Cochran's Q
test for heterogeneity. When ETWFE wins, reports the heterogeneity
fraction (I-squared) and cohort-time estimates with empirical Bayes
shrinkage and Bonferroni multiplicity correction. Methods build on
Wooldridge (2025) <doi:10.1007/s00181-025-02807-z> and Callaway and
Sant'Anna (2021) <doi:10.1016/j.jeconom.2020.12.001>.

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
