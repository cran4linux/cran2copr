%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spfcICOMP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shrinkage Principal Fitted Components with Information Complexity-Based Model Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Implements shrinkage principal fitted components for sufficient dimension
reduction in high-dimensional regression and classification. Provides
regularised covariance estimation using Oracle Approximating Shrinkage and
Maximum Entropy Covariance, structural-dimension selection using
conventional and information-complexity criteria, response-guided feature
screening, reduced-space prediction, and simulation utilities.
Methodological foundations include Cook and Forzani (2008)
<doi:10.1214/08-STS275>, Chen et al. (2010)
<doi:10.1109/TSP.2010.2053029>, Bozdogan (2000)
<doi:10.1006/jmps.1999.1277>, and Olorede and Yahya (2019)
<doi:10.48550/arXiv.1909.13017>.

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
