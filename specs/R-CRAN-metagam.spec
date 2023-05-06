%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metagam
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Generalized Additive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-rlang 

%description
Meta-analysis of generalized additive models and generalized additive
mixed models. A typical use case is when data cannot be shared across
locations, and an overall meta-analytic fit is sought. 'metagam' provides
functionality for removing individual participant data from models
computed using the 'mgcv' and 'gamm4' packages such that the model objects
can be shared without exposing individual data. Furthermore, methods for
meta-analysing these fits are provided. The implemented methods are
described in Sorensen et al. (2020),
<doi:10.1016/j.neuroimage.2020.117416>, extending previous works by
Schwartz and Zanobetti (2000) and Crippa et al. (2018)
<doi:10.6000/1929-6029.2018.07.02.1>.

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
