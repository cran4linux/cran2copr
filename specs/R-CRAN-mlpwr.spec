%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlpwr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Power Analysis Toolbox to Find Cost-Efficient Study Designs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-WeightSVM 
BuildRequires:    R-CRAN-rgenoud 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-WeightSVM 
Requires:         R-CRAN-rgenoud 

%description
We implement a surrogate modeling algorithm to guide simulation-based
sample size planning. The method is described in detail in a recent
preprint (Zimmer & Debelak (2022) <doi:10.31234/osf.io/tnhb2>). It
supports multiple study design parameters and optimization with respect to
a cost function. It can find optimal designs that correspond to a desired
statistical power or that fulfill a cost constraint.

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
