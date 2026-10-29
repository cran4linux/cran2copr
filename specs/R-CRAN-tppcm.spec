%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tppcm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Step Discriminations for the Two-Parameter Partial Credit Model on Top of 'TAM'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-TAM 
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-stats 
Requires:         R-CRAN-TAM 
Requires:         R-CRAN-CDM 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-sirt 
Requires:         R-stats 

%description
In the two-parameter partial credit model (TPPCM) of Yu (1991)
<https://hdl.handle.net/2142/21459>, every step of a polytomous item has
its own discrimination. Estimation is left to existing software: 'TAM'
(tam.mml.3pl() with a step design matrix, tam.mml.2pl(), tam.mml()) and,
for the bilinear product form and non-negativity constraints, 'sirt'
(xxirt()). The package adds what these packages do not provide: standard
errors of step discriminations based on the full observed information,
step-level Wald tests, and score tests with modification indices and
expected parameter changes for moving down the model ladder saturated
TPPCM -> product form -> generalized partial credit model -> partial
credit model, limited-information fit statistics (the M2 statistic, root
mean square error of approximation, standardized root mean squared
residual, comparative fit index and Tucker-Lewis index; Maydeu-Olivares
and Joe (2006) <doi:10.1007/s11336-005-1295-9>) for any step design, step
contributions to the item information, and tests of differential step
functioning across groups: per-step Lagrange multiplier tests from one
multigroup fit (Glas (1998)
<https://www3.stat.sinica.edu.tw/statistica/j8n3/j8n32/j8n32.htm>), with
the generalized score test of Boos (1992)
<doi:10.1080/00031305.1992.10475921>, likelihood ratio tests with
configural, metric, scalar and partial multigroup designs, score-based
tests (Merkle and Zeileis (2013) <doi:10.1007/s11336-012-9302-4>) and
model-based trees (Zeileis, Hothorn and Hornik (2008)
<doi:10.1198/106186008X319331>). The generalized partial credit model of
Muraki (1992) <doi:10.1177/014662169201600206> is the special case with
equal steps within items.

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
