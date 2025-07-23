%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metacor
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analytic Effect Size Calculation for Pre-Post Designs with Correlation Imputation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-stringr 
Requires:         R-stats 

%description
Tools for the calculation of effect sizes (standardised mean difference)
and mean difference in pre-post controlled studies, including robust
imputation of missing variances (standard deviation of changes) and
correlations (Pearson correlation coefficient). The main function
metacor_dual() implements several methods for imputing missing standard
deviation of changes or Pearson correlation coefficient, and generates
transparent imputation reports. Designed for meta-analyses with incomplete
summary statistics. For more details on the methods, see Higgins et al.
(2023) and Fu et al. (2013).

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
