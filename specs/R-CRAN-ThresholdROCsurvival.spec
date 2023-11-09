%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThresholdROCsurvival
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostic Ability Assessment with Right-Censored Data at a Fixed Time t

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-InformativeCensoring 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ThresholdROC 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-InformativeCensoring 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ThresholdROC 

%description
We focus on the diagnostic ability assessment of medical tests when the
outcome of interest is the status (alive or dead) of the subjects at a
certain time-point t. This binary status is determined by right-censored
times to event and it is unknown for those subjects censored before t.
Here we provide three methods (unknown status exclusion, imputation of
censored times and using time-dependent ROC curves) to evaluate the
diagnostic ability of binary and continuous tests in this context. Two
references for the methods used here are Skaltsa et al. (2010)
<doi:10.1002/bimj.200900294> and Heagerty et al. (2000)
<doi:10.1111/j.0006-341x.2000.00337.x>.

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
