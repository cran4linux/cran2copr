%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  deeptrafo
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Deep Conditional Transformation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 2.2.0
BuildRequires:    R-CRAN-keras >= 2.2.0
BuildRequires:    R-CRAN-tfprobability >= 0.15
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-deepregression 
BuildRequires:    R-CRAN-mlt 
BuildRequires:    R-CRAN-variables 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow >= 2.2.0
Requires:         R-CRAN-keras >= 2.2.0
Requires:         R-CRAN-tfprobability >= 0.15
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-deepregression 
Requires:         R-CRAN-mlt 
Requires:         R-CRAN-variables 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-reticulate 

%description
Allows for the specification of deep conditional transformation models
(DCTMs) and ordinal neural network transformation models, as described in
Baumann et al (2021) <doi:10.1007/978-3-030-86523-8_1> and Kook et al
(2022) <doi:10.1016/j.patcog.2021.108263>. Extensions such as
autoregressive DCTMs (Ruegamer et al, 2022,
<doi:10.48550/arXiv.2110.08248>) and transformation ensembles (Kook et al,
2022, <doi:10.48550/arXiv.2205.12729>) are implemented.

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
