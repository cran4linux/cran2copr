%global __brp_check_rpaths %{nil}
%global packname  scdhlm
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Hierarchical Linear Models for Single-Case Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lmeInfo > 0.2.0
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-lmeInfo > 0.2.0
Requires:         R-CRAN-nlme 
Requires:         R-stats 
Requires:         R-CRAN-readxl 

%description
Provides a set of tools for estimating hierarchical linear models and
effect sizes based on data from single-case designs. Functions are
provided for calculating standardized mean difference effect sizes that
are directly comparable to standardized mean differences estimated from
between-subjects randomized experiments, as described in Hedges,
Pustejovsky, and Shadish (2012) <DOI:10.1002/jrsm.1052>; Hedges,
Pustejovsky, and Shadish (2013) <DOI:10.1002/jrsm.1086>; and Pustejovsky,
Hedges, and Shadish (2014) <DOI:10.3102/1076998614547577>. Includes an
interactive web interface.

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
