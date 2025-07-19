%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cmgnd
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Mixture of Generalized Normal Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gnorm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-gnorm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 

%description
The 'cmgnd' implements the constrained mixture of generalized normal
distributions model, a flexible statistical framework for modelling
univariate data exhibiting non-normal features such as skewness,
multi-modality, and heavy tails. By imposing constraints on model
parameters, the 'cmgnd' reduces estimation complexity while maintaining
high descriptive power, offering an efficient solution in the presence of
distributional irregularities. For more details see Duttilo and Gattone
(2025) <doi:10.1007/s00180-025-01638-x> and Duttilo et al (2025)
<doi:10.48550/arXiv.2506.03285>.

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
