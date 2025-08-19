%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WData
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference for Weighted Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bayesmeta 
BuildRequires:    R-CRAN-evmix 
BuildRequires:    R-CRAN-KScorrect 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-bayesmeta 
Requires:         R-CRAN-evmix 
Requires:         R-CRAN-KScorrect 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 

%description
Analyzes and models data subject to sampling biases. Provides functions to
estimate the density and cumulative distribution functions from biased
samples of continuous distributions. Includes the estimators proposed by
Bhattacharyya et al. (1988) <doi:10.1080/03610928808829825> and Jones
(1991) <doi:10.2307/2337020> for density, and by Cox (2005,
ISBN:052184939X) and Bose and Dutta (2022)
<doi:10.1007/s00184-021-00824-3> for distribution, with different
bandwidth selectors. Also includes a real length-biased dataset on shrub
width from Muttlak (1988)
<https://www.proquest.com/openview/3dd74592e623cdbcfa6176e85bd3d390/1?cbl=18750&diss=y&pq-origsite=gscholar>.

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
