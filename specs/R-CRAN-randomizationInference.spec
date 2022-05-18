%global __brp_check_rpaths %{nil}
%global packname  randomizationInference
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Randomization-Based Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-permute >= 0.7.8
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-permute >= 0.7.8
Requires:         R-CRAN-matrixStats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Allows the user to conduct randomization-based inference for a wide
variety of experimental scenarios. The package leverages a potential
outcomes framework to output randomization-based p-values and null
intervals for test statistics geared toward any estimands of interest,
according to the specified null and alternative hypotheses. Users can
define custom randomization schemes so that the randomization
distributions are accurate for their experimental settings. The package
also creates visualizations of randomization distributions and can test
multiple test statistics simultaneously.

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
