%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metamedian
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Medians

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-estmeansd 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-metaBLUE 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
Requires:         R-CRAN-estmeansd 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-metaBLUE 
Requires:         R-CRAN-metafor 
Requires:         R-stats 

%description
Implements several methods to meta-analyze studies that report the sample
median of the outcome. When the primary studies are one-group studies, the
methods of McGrath et al. (2019) <doi:10.1002/sim.8013> and Ozturk and
Balakrishnan (2020) <doi:10.1002/sim.8738> can be applied to estimate the
pooled median. In the two-group context, the methods of McGrath et al.
(2020a) <doi:10.1002/bimj.201900036> can be applied to estimate the pooled
difference of medians across groups. Additionally, a number of methods
(e.g., McGrath et al. (2020b) <doi:10.1177/0962280219889080>, Cai et al.
(2021) <doi:10.1177/09622802211047348>, and McGrath et al. (2023)
<doi:10.1177/09622802221139233>) are implemented to estimate
study-specific (difference of) means and their standard errors in order to
estimate the pooled (difference of) means.

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
