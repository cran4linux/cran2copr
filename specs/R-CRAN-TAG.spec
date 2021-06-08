%global packname  TAG
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Transformed Additive Gaussian Processes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-FastGP 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-FastGP 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-foreach 

%description
Implement the transformed additive Gaussian (TAG) process and the
transformed approximately additive Gaussian (TAAG) process proposed in Lin
and Joseph (2020) <DOI:10.1080/00401706.2019.1665592>. These functions can
be used to model deterministic computer experiments, obtain predictions at
new inputs, and quantify the uncertainty of the predictions. This research
is supported by a U.S. National Science Foundation grant DMS-1712642 and a
U.S. Army Research Office grant W911NF-17-1-0007.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
