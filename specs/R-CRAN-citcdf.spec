%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  citcdf
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Independence Testing with Cumulative Distribution Functions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RcppNumerical 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pbapply 
Requires:         R-parallel 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-RcppNumerical 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-viridisLite 

%description
Complex hypothesis testing through conditional cumulative distribution
function estimation. Method is detailed in: Gauthier M, Agniel D, Thiébaut
R & Hejblum BP (2021). "Distribution-free complex hypothesis testing for
single-cell RNA-seq differential expression analysis", bioRxiv
<doi:10.1101/2021.05.21.445165>.

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
