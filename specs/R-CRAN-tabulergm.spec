%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tabulergm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Publication-Ready Tables and Summaries for Exponential-Family Random Graph Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm >= 4.0
BuildRequires:    R-CRAN-netplot >= 0.4.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-ergm >= 4.0
Requires:         R-CRAN-netplot >= 0.4.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-network 
Requires:         R-CRAN-yaml 

%description
Creates publication-ready tables documenting exponential-family random
graph models (ERGMs), a class of statistical models for social networks
(Robins et al., 2007, <doi:10.1016/j.socnet.2006.08.002>). Tables describe
model terms through their definitions, mathematical representations, and
graphical representations, and can be generated from ERGM formulas or from
models fitted with the 'ergm' package (Hunter et al., 2008,
<doi:10.18637/jss.v024.i03>). Resulting tables can be integrated into
'quarto' and 'rmarkdown' documents.

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
