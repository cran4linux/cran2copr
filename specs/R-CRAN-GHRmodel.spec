%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GHRmodel
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Hierarchical Modelling of Spatio-Temporal Health Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-dlnm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-GHRexplore 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-dlnm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-GHRexplore 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 

%description
Supports modeling health outcomes using Bayesian hierarchical
spatio-temporal models with complex covariate effects (e.g., linear,
non-linear, interactions, distributed lag linear and non-linear models) in
the 'INLA' framework. It is designed to help users identify key drivers
and predictors of disease risk by enabling streamlined model exploration,
comparison, and visualization of complex covariate effects. See an
application of the modelling framework in Lowe, Lee, O'Reilly et al.
(2021) <doi:10.1016/S2542-5196(20)30292-8>.

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
