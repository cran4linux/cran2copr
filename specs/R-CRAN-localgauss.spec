%global __brp_check_rpaths %{nil}
%global packname  localgauss
%global packver   0.41
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.41
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Local Gaussian Parameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 

%description
Computational routines for estimating local Gaussian parameters. Local
Gaussian parameters are useful for characterizing and testing for
non-linear dependence within bivariate data. See e.g. Tjostheim and
Hufthammer, Local Gaussian correlation: A new measure of dependence,
Journal of Econometrics, 2013, Volume 172 (1), pages 33-48
<DOI:10.1016/j.jeconom.2012.08.001>.

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
