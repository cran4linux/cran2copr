%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DMCfun
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Diffusion Model of Conflict (DMC) in Reaction Time Tasks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-DEoptim 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-tidyr 

%description
DMC model simulation detailed in Ulrich, R., Schroeter, H., Leuthold, H.,
& Birngruber, T. (2015). Automatic and controlled stimulus processing in
conflict tasks: Superimposed diffusion processes and delta functions.
Cognitive Psychology, 78, 148-174. Ulrich et al. (2015)
<doi:10.1016/j.cogpsych.2015.02.005>. Decision processes within choice
reaction-time (CRT) tasks are often modelled using evidence accumulation
models (EAMs), a variation of which is the Diffusion Decision Model (DDM,
for a review, see Ratcliff & McKoon, 2008). Ulrich et al. (2015)
introduced a Diffusion Model for Conflict tasks (DMC). The DMC model
combines common features from within standard diffusion models with the
addition of superimposed controlled and automatic activation. The DMC
model is used to explain distributional reaction time (and error rate)
patterns in common behavioural conflict-like tasks (e.g., Flanker task,
Simon task). This R-package implements the DMC model and provides
functionality to fit the model to observed data. Further details are
provided in the following paper: Mackenzie, I.G., & Dudschig, C. (2021).
DMCfun: An R package for fitting Diffusion Model of Conflict (DMC) to
reaction time and error rate data. Methods in Psychology, 100074.
<doi:10.1016/j.metip.2021.100074>.

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
