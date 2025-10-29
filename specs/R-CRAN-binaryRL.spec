%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binaryRL
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Reinforcement Learning Tools for Two-Alternative Forced Choice Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-progressr 

%description
Tools for building Rescorla-Wagner Models for Two-Alternative Forced
Choice tasks, commonly employed in psychological research. Most concepts
and ideas within this R package are referenced from Sutton and Barto
(2018) <ISBN:9780262039246>. The package allows for the intuitive
definition of RL models using simple if-else statements and three basic
models built into this R package are referenced from Niv et al.
(2012)<doi:10.1523/JNEUROSCI.5498-10.2012>. Our approach to constructing
and evaluating these computational models is informed by the guidelines
proposed in Wilson & Collins (2019) <doi:10.7554/eLife.49547>. Example
datasets included with the package are sourced from the work of Mason et
al. (2024) <doi:10.3758/s13423-023-02415-x>.

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
