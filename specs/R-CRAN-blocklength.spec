%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blocklength
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Select an Optimal Block-Length to Bootstrap Dependent Data (Block Bootstrap)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-stats 
Requires:         R-CRAN-tseries 
Requires:         R-stats 

%description
A set of functions to select the optimal block-length for a dependent
bootstrap (block-bootstrap). Includes the Hall, Horowitz, and Jing (1995)
<doi:10.1093/biomet/82.3.561> subsampling-based cross-validation method,
the Politis and White (2004) <doi:10.1081/ETC-120028836> Spectral Density
Plug-in method, including the Patton, Politis, and White (2009)
<doi:10.1080/07474930802459016> correction, and the Lahiri, Furukawa, and
Lee (2007) <doi:10.1016/j.stamet.2006.08.002> nonparametric plug-in
method, with a corresponding set of S3 plot methods.

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
