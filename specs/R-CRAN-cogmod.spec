%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cogmod
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cognitive Models for Subjective Scales and Decision Making Tasks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-stats 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-insight 
Requires:         R-stats 

%description
Implements cognitive models for data from subjective (Likert or analog)
scales and from decision making tasks with reaction times and choice data.
Provides random generation, density functions, and custom response
distributions for Bayesian estimation with 'brms', covering
discreted-beta, ordered beta and choice-confidence models for subjective
ratings, reaction-times families (Shifted Log-Normal, Shifted Wald), as
well as sequential sampling models including the drift diffusion model
(DDM), the racing diffusion model (RDM), the lognormal race model (LNR),
and linear ballistic accumulator (LBA) model. The website provides
examples and tutorials for using and interpreting the models. Methods are
described in Ratcliff and McKoon (2008) <doi:10.1162/neco.2008.12-06-420>,
Brown and Heathcote (2008) <doi:10.1016/j.cogpsych.2007.12.002>, Rouder et
al. (2015) <doi:10.1007/s11336-013-9396-3>, Tillman et al. (2020)
<doi:10.3758/s13423-020-01719-6>, Kubinec (2023)
<doi:10.1017/pan.2022.20>, and Sciandra et al. (2024)
<doi:10.1007/s10651-023-00592-5>.

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
