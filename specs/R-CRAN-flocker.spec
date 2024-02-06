%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flocker
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Occupancy Estimation with Stan

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms >= 2.20.3
BuildRequires:    R-CRAN-loo >= 2.0.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-brms >= 2.20.3
Requires:         R-CRAN-loo >= 2.0.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Fit occupancy models in 'Stan' via 'brms'. The full variety of 'brms'
formula-based effects structures are available to use in multiple classes
of occupancy model, including single-season models, models with data
augmentation for never-observed species, dynamic (multiseason) models with
explicit colonization and extinction processes, and dynamic models with
autologistic occupancy dynamics. Formulas can be specified for all
relevant distributional terms, including detection and one or more of
occupancy, colonization, extinction, and autologistic depending on the
model type. Several important forms of model post-processing are provided.
References: Bürkner (2017) <doi:10.18637/jss.v080.i01>; Carpenter et al.
(2017) <doi:10.18637/jss.v076.i01>; Socolar & Mills (2023)
<doi:10.1101/2023.10.26.564080>.

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
