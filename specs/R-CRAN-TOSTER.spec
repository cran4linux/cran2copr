%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TOSTER
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Two One-Sided Tests (TOST) Equivalence Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 0.9.6.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggdist 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-jmvcore >= 0.9.6.4
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggdist 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lifecycle 

%description
Two one-sided tests (TOST) procedure to test equivalence for t-tests,
correlations, differences between proportions, and meta-analyses,
including power analysis for t-tests and correlations. Allows you to
specify equivalence bounds in raw scale units or in terms of effect sizes.
See: Lakens (2017) <doi:10.1177/1948550617697177>.

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
