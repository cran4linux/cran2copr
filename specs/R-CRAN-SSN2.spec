%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSN2
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Modeling on Stream Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spmodel >= 0.14.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-filematrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-spmodel >= 0.14.0
Requires:         R-stats 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tibble 
Requires:         R-graphics 
Requires:         R-CRAN-RSQLite 
Requires:         R-utils 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-filematrix 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-iterators 

%description
Fit, summarize, and predict for spatial linear and generalized linear
models on stream networks. Stream covariance models use moving average
constructions based on in-stream distance. Parameters are estimated using
likelihood methods. Additional modeling features include Euclidean
covariance, anisotropy, non-spatial random effects, partition factors, and
big data methods. Model-fit statistics are used to summarize, visualize,
and compare models, and predictions at unobserved locations are readily
obtainable. For additional details, see Ver Hoef and Peterson (2010)
<DOI:10.1198/jasa.2009.ap08248> and Dumelle et al. (2024)
<DOI:10.21105/joss.06389>.

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
