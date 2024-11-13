%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CIMPLE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Longitudinal Electronic Health Record (EHR) Data with Possibly Informative Observational Time

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-JMbayes2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-JMbayes2 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 

%description
Analyzes longitudinal Electronic Health Record (EHR) data with possibly
informative observational time. These methods are grouped into two classes
depending on the inferential task. One group focuses on estimating the
effect of an exposure on a longitudinal biomarker while the other group
assesses the impact of a longitudinal biomarker on time-to-diagnosis
outcomes. The accompanying paper is Du et al (2024)
<doi:10.48550/arXiv.2410.13113>.

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
