%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompositionalSR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Regression Models with Compositional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-blockCV 
BuildRequires:    R-CRAN-Compositional 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gslnls 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rangen 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spmoran 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-blockCV 
Requires:         R-CRAN-Compositional 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gslnls 
Requires:         R-CRAN-minpack.lm 
Requires:         R-parallel 
Requires:         R-CRAN-rangen 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spmoran 
Requires:         R-stats 
Requires:         R-utils 

%description
Spatial and non-spatial regression models with compositional responses
(and compositional predictors) using the alpha--transformation. Relevant
papers include: Tsagris M. and Pantazis Y. (2026),
<doi:10.48550/arXiv.2510.12663>, Tsagris M. (2015),
<https://soche.cl/chjs/volumes/06/02/Tsagris(2015).pdf>, Tsagris M.T.,
Preston S. and Wood A.T.A. (2011), <doi:10.48550/arXiv.1106.1451>.

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
