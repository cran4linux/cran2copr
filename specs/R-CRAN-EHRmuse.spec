%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EHRmuse
%global packver   0.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Cohort Selection Bias Correction using IPW and AIPW Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nnet >= 7.3.17
BuildRequires:    R-CRAN-survey >= 4.1.0
BuildRequires:    R-CRAN-nleqslv >= 3.3.2
BuildRequires:    R-CRAN-xgboost >= 1.4.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-simplexreg >= 0.1
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-nnet >= 7.3.17
Requires:         R-CRAN-survey >= 4.1.0
Requires:         R-CRAN-nleqslv >= 3.3.2
Requires:         R-CRAN-xgboost >= 1.4.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-simplexreg >= 0.1
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Comprehensive toolkit for addressing selection bias in binary disease
models across diverse non-probability samples, each with unique selection
mechanisms. It utilizes Inverse Probability Weighting (IPW) and Augmented
Inverse Probability Weighting (AIPW) methods to reduce selection bias
effectively in multiple non-probability cohorts by integrating data from
either individual-level or summary-level external sources. The package
also provides a variety of variance estimation techniques. Please refer to
Kundu et al. <doi:10.48550/arXiv.2412.00228>.

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
