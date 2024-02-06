%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDCM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Transition Diagnostic Classification Model Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-CDM 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-stringr 

%description
Estimate the transition diagnostic classification model (TDCM) described
in Madison & Bradshaw (2018) <doi:10.1007/s11336-018-9638-5>, a
longitudinal extension of the log-linear cognitive diagnosis model (LCDM)
in Henson, Templin & Willse (2009) <doi:10.1007/s11336-008-9089-5>. As the
LCDM subsumes many other diagnostic classification models (DCMs), many
other DCMs can be estimated longitudinally via the TDCM. The 'TDCM'
package includes functions to estimate the single-group and multigroup
TDCM, summarize results of interest including item parameters, growth
proportions, transition probabilities, transitional reliability, attribute
correlations, model fit, and growth plots.

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
