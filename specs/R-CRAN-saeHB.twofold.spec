%global __brp_check_rpaths %{nil}
%global packname  saeHB.twofold
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Bayes Twofold Subarea Level Model SAE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-data.table 
Requires:         R-utils 

%description
We designed this package to provides several functions for area and
subarea level of small area estimation under Twofold Subarea Level Model
using hierarchical Bayesian (HB) method with Univariate Normal
distribution for variables of interest. Some dataset simulated by a data
generation are also provided. The 'rjags' package is employed to obtain
parameter estimates using Gibbs Sampling algorithm. Model-based estimators
involves the HB estimators which include the mean, the variation of mean,
and the quantile. For the reference, see Rao and Molina (2015)
<doi:10.1002/9781118735855>, Torabi and Rao (2014)
<doi:10.1016/j.jmva.2014.02.001>, Leyla Mohadjer et al.(2007)
<http://www.asasrms.org/Proceedings/y2007/Files/JSM2007-000559.pdf>, and
Erciulescu et al.(2019) <doi:10.1111/rssa.12390>.

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
