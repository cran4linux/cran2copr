%global __brp_check_rpaths %{nil}
%global packname  sampsizeval
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size for Validation of Risk Models with Binary Outcomes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 

%description
Estimation of the required sample size to validate a risk model for binary
outcomes, based on the sample size equations proposed by Pavlou et al.
(2021) <doi:10.1177/09622802211007522>. For precision-based sample size
calculations, the user is required to enter the anticipated values of the
C-statistic and outcome prevalence, which can be obtained from a previous
study. The user also needs to specify the required precision (standard
error) for the C-statistic, the calibration slope and the calibration in
the large. The calculations are valid under the assumption of marginal
normality for the distribution of the linear predictor.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
