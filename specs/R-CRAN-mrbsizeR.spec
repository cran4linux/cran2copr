%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mrbsizeR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Scale Space Multiresolution Analysis of Random Signals

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-fields >= 8.10
BuildRequires:    R-CRAN-maps >= 3.1.1
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-methods >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-fields >= 8.10
Requires:         R-CRAN-maps >= 3.1.1
Requires:         R-stats >= 3.0.0
Requires:         R-grDevices >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-methods >= 3.0.0
Requires:         R-CRAN-Rcpp >= 0.12.14

%description
A method for the multiresolution analysis of spatial fields and images to
capture scale-dependent features. mrbsizeR is based on scale space
smoothing and uses differences of smooths at neighbouring scales for
finding features on different scales. To infer which of the captured
features are credible, Bayesian analysis is used. The scale space
multiresolution analysis has three steps: (1) Bayesian signal
reconstruction. (2) Using differences of smooths, scale-dependent features
of the reconstructed signal can be found. (3) Posterior credibility
analysis of the differences of smooths created. The method has first been
proposed by Holmstrom, Pasanen, Furrer, Sain (2011)
<DOI:10.1016/j.csda.2011.04.011> and extended in Flury, Gerber, Schmid and
Furrer (2021) <DOI:10.1016/j.spasta.2020.100483>.

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
