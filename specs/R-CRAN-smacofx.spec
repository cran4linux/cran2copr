%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  smacofx
%global packver   0.6-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Multidimensional Scaling and 'smacof' Extensions

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-smacof >= 1.10.4
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-ProjectionBasedClustering 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-smacof >= 1.10.4
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-ProjectionBasedClustering 
Requires:         R-CRAN-weights 
Requires:         R-CRAN-vegan 

%description
Flexible multidimensional scaling (MDS) methods centered around scaling
with majorization and extensions to the package 'smacof'. This package
enhances 'smacof' and contains various functions, wrappers, methods and
classes for fitting, plotting and displaying a large number of different
flexible MDS models (some as of yet unpublished) such as Torgerson scaling
(Torgerson, 1958, ISBN:978-0471879459) with powers, Sammon mapping
(Sammon, 1969, <doi:10.1109/T-C.1969.222678>) with ratio and interval
optimal scaling, Multiscale MDS (Ramsay, 1977, <doi:10.1007/BF02294052>)
with ratio and interval optimal scaling, S-stress MDS (ALSCAL; Takane,
Young & De Leeuw, 1977, <doi:10.1007/BF02293745>) with ratio and interval
optimal scaling, elastic scaling (McGee, 1966,
<doi:10.1111/j.2044-8317.1966.tb00367.x>) with ratio and interval optimal
scaling, r-stress MDS (De Leeuw, Groenen & Mair, 2016,
<https://rpubs.com/deleeuw/142619>) with ratio, interval and non-metric
optimal scaling, power-stress MDS (POST-MDS; Buja & Swayne, 2002
<doi:10.1007/s00357-001-0031-0>) with ratio and interval optimal scaling,
restricted power-stress (Rusch, Mair & Hornik, 2021,
<doi:10.1080/10618600.2020.1869027>) with ratio and interval optimal
scaling, approximate power-stress with ratio optimal scaling (Rusch, Mair
& Hornik, 2021, <doi:10.1080/10618600.2020.1869027>), Box-Cox MDS (Chen &
Buja, 2013, <https://jmlr.org/papers/v14/chen13a.html>), local MDS (Chen &
Buja, 2009, <doi:10.1198/jasa.2009.0111>), curvilinear component analysis
(Demartines & Herault, 1997, <doi:10.1109/72.554199>) and curvilinear
distance analysis (Lee, Lendasse & Verleysen, 2004,
<doi:10.1016/j.neucom.2004.01.007>). There also are experimental models
(e.g., sparsified MDS and sparsified POST-MDS). Some functions are
suitably flexible to allow any other sensible combination of explicit
power transformations for weights, distances and input proximities with
implicit ratio, interval or non-metric optimal scaling of the input
proximities. Most functions use a Majorization-Minimization algorithm.

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
