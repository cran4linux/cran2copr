%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rfuzzydid
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy Difference in Differences

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Differences in differences is a methodology to measure the impact of a
treatment by comparing a control group, which remains untreated at two
different time periods, with a treatment group, which receives the
treatment at the later date. In many cases, this approach is used in
situations where the intervention doesn't fully apply the treatment to the
entire treatment group but rather increases the treatment rate. In
response to such fuzzy scenarios, de Chaisemartin and D'Haultfoeuille
(2018) <doi:10.1093/restud/rdx049> introduce estimands capable of
identifying local average and quantile treatment effects under various
assumptions. This R package computes the estimators they are proposing.

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
