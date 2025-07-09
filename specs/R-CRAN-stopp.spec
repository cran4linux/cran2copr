%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stopp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Point Pattern Methods, Model Fitting, Diagnostics, Simulation, Local Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-CRAN-spatstat.explore 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.linnet 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-spatstat.model 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-CRAN-stlnpp 
BuildRequires:    R-CRAN-stpp 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-spatstat.univar 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-sparr 
Requires:         R-CRAN-spatstat.explore 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.linnet 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-spatstat.model 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-CRAN-stlnpp 
Requires:         R-CRAN-stpp 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-spatstat.univar 

%description
Toolbox for different kinds of spatio-temporal analyses to be performed on
observed point patterns, following the growing stream of literature on
point process theory. This R package implements functions to perform
different kinds of analyses on point processes, proposed in the papers
(Siino, Adelfio, and Mateu 2018<doi:10.1007/s00477-018-1579-0>; Siino et
al. 2018<doi:10.1002/env.2463>; Adelfio et al.
2020<doi:10.1007/s00477-019-01748-1>; D’Angelo, Adelfio, and Mateu
2021<doi:10.1016/j.spasta.2021.100534>; D’Angelo, Adelfio, and Mateu
2022<doi:10.1007/s00362-022-01338-4>; D’Angelo, Adelfio, and Mateu
2023<doi:10.1016/j.csda.2022.107679>). The main topics include modeling,
statistical inference, and simulation issues on spatio-temporal point
processes on Euclidean space and linear networks. Version 1.0.0 has been
updated for accompanying the journal publication D Angelo and Adelfio 2025
<doi:10.18637/jss.v113.i10>.

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
