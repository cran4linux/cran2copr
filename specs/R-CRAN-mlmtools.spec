%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlmtools
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Level Model Assessment Kit

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Multilevel models (mixed effects models) are the statistical tool of
choice for analyzing multilevel data (Searle et al, 2009). These models
account for the correlated nature of observations within higher level
units by adding group-level error terms that augment the singular residual
error of a standard OLS regression. Multilevel and mixed effects models
often require specialized data pre-processing and further post-estimation
derivations and graphics to gain insight into model results. The package
presented here, 'mlmtools', is a suite of pre- and post-estimation tools
for multilevel models in 'R'. Package implements post-estimation tools
designed to work with models estimated using 'lme4''s (Bates et al., 2014)
lmer() function, which fits linear mixed effects regression models.
Searle, S. R., Casella, G., & McCulloch, C. E. (2009,
ISBN:978-0470009598). Bates, D., Mächler, M., Bolker, B., & Walker, S.
(2014) <doi:10.18637/jss.v067.i01>.

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
