%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fic
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Focused Information Criteria for Model Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-mgcv 

%description
Compares how well different models estimate a quantity of interest (the
"focus") so that different models may be preferred for different purposes.
Comparisons within any class of models fitted by maximum likelihood are
supported, with shortcuts for commonly-used classes such as generalised
linear models and parametric survival models.  The methods originate from
Claeskens and Hjort (2003) <doi:10.1198/016214503000000819> and Claeskens
and Hjort (2008, ISBN:9780521852258).

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
