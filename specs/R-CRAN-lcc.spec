%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lcc
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Analysis of Longitudinal Data Using the Concordance Correlation Coefficient

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme >= 3.1.124
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-hnp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-nlme >= 3.1.124
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-hnp 
Requires:         R-parallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 

%description
Methods for assessing agreement between repeated measurements obtained by
two or more methods using the longitudinal concordance correlation
coefficient (LCC). Polynomial mixed-effects models (via 'nlme') describe
how concordance, Pearson correlation and accuracy evolve over time.
Functions are provided for model fitting, diagnostic plots, extraction of
summaries, and non-parametric bootstrap confidence intervals (including
parallel computation), following Oliveira et al. (2018)
<doi:10.1007/s13253-018-0321-1>.

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
