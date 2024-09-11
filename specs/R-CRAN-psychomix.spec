%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psychomix
%global packver   1.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Psychometric Mixture Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexmix >= 2.3.7
BuildRequires:    R-CRAN-Formula >= 1.1.0
BuildRequires:    R-CRAN-psychotools >= 0.4.2
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-modeltools 
Requires:         R-CRAN-flexmix >= 2.3.7
Requires:         R-CRAN-Formula >= 1.1.0
Requires:         R-CRAN-psychotools >= 0.4.2
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-modeltools 

%description
Psychometric mixture models based on 'flexmix' infrastructure. At the
moment Rasch mixture models with different parameterizations of the score
distribution (saturated vs. mean/variance specification), Bradley-Terry
mixture models, and MPT mixture models are implemented. These mixture
models can be estimated with or without concomitant variables. See Frick
et al. (2012) <doi:10.18637/jss.v048.i07> and Frick et al. (2015)
<doi:10.1177/0013164414536183> for details on the Rasch mixture models.

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
