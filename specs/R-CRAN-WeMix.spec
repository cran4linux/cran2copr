%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WeMix
%global packver   4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Mixed-Effects Models Using Multilevel Pseudo Maximum Likelihood Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.5.4.1
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-Matrix >= 1.5.4.1
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-numDeriv 
Requires:         R-methods 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-matrixStats 

%description
Run mixed-effects models that include weights at every level. The WeMix
package fits a weighted mixed model, also known as a multilevel, mixed, or
hierarchical linear model (HLM). The weights could be inverse selection
probabilities, such as those developed for an education survey where
schools are sampled probabilistically, and then students inside of those
schools are sampled probabilistically. Although mixed-effects models are
already available in R, WeMix is unique in implementing methods for mixed
models using weights at multiple levels. Both linear and logit models are
supported. Models may have up to three levels. Random effects are
estimated using the PIRLS algorithm from 'lme4pureR' (Walker and Bates
(2013) <https://github.com/lme4/lme4pureR>).

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
