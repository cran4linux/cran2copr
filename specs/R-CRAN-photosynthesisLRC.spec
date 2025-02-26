%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  photosynthesisLRC
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Least Squares Models for Photosynthetic Light Response

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-stats >= 4.2.3
BuildRequires:    R-graphics >= 4.2.3
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
Requires:         R-stats >= 4.2.3
Requires:         R-graphics >= 4.2.3
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4

%description
Provides functions for modeling, comparing, and visualizing photosynthetic
light response curves using established mechanistic and empirical models
like the rectangular hyperbola Michaelis-Menton based models ((eq1 (Baly
(1935) <doi:10.1098/rspb.1935.0026>)) (eq2 (Kaipiainenn (2009)
<doi:10.1134/S1021443709040025>)) (eq3 (Smith (1936)
<doi:10.1073/pnas.22.8.504>))), hyperbolic tangent based models ((eq4
(Jassby & Platt (1976) <doi:10.4319/LO.1976.21.4.0540>)) (eq5 (Abe et al.
(2009) <doi:10.1111/j.1444-2906.2008.01619.x>))), the non-rectangular
hyperbola model (eq6 (Prioul & Chartier (1977)
<doi:10.1093/oxfordjournals.aob.a085354>)), exponential based models ((eq8
(Webb et al. (1974) <doi:10.1007/BF00345747>)), (eq9 (Prado & de Moraes
(1997) <doi:10.1007/BF02982542>))), and finally the Ye model (eq11 (Ye
(2007) <doi:10.1007/s11099-007-0110-5>)). Each of these nonlinear least
squares models are commonly used to express photosynthetic response under
changing light conditions and has been well supported in the literature,
but distinctions in each mathematical model represent moderately different
assumptions about physiology and trait relationships which ultimately
produce different calculated functional trait values. These models were
all thoughtfully discussed and curated by Lobo et al. (2013)
<doi:10.1007/s11099-013-0045-y> to express the importance of selecting an
appropriate model for analysis, and methods were established in Davis et
al. (in review) to evaluate the impact of analytical choice in
phylogenetic analysis of the function-valued traits. Gas exchange data on
28 wild sunflower species from Davis et al.are included as an example data
set here.

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
