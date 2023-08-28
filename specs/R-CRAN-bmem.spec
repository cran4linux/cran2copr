%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bmem
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Mediation Analysis with Missing Data Using Bootstrap

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.7
Requires:         R-core >= 1.7
BuildArch:        noarch
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-sem 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-sem 

%description
Four methods for mediation analysis with missing data: Listwise deletion,
Pairwise deletion, Multiple imputation, and Two Stage Maximum Likelihood
algorithm. For MI and TS-ML, auxiliary variables can be included.
Bootstrap confidence intervals for mediation effects are obtained. The
robust method is also implemented for TS-ML. Since version 1.4, bmem adds
the capability to conduct power analysis for mediation models. Details
about the methods used can be found in these articles. Zhang and Wang
(2003) <doi:10.1007/s11336-012-9301-5>. Zhang (2014)
<doi:10.3758/s13428-013-0424-0>.

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
