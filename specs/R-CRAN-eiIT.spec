%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eiIT
%global packver   0.0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference via Information Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nloptr 

%description
Estimates RxC transfer matrices from aggregated marginal data using a
two-stage (GME+IPF) information-theoretic approach within a two-step
(global+local) estimation procedure. The resulting matrices are consistent
with observed row and column marginals across collections of subtables
(e.g. precincts, polling stations, or districts). References: Golan, A.,
Judge, G., & Miller, D. (1996). Maximum Entropy Econometrics: Robust
Estimation with Limited Data. Wiley. Judge, G., Miller, D.J., & Cho,
W.K.T. (2004). An information theoretic approach to ecological estimation
and inference. In G. King, O. Rosen, & M. A. Tanner (Eds.), Ecological
Inference: New Methodological Strategies (pp. 162–187). Cambridge
University Press. Mittelhammer, R., Judge, G., & Miller, D. (2000).
Econometric Foundations. Cambridge University Press. Pavia, J.M. (2023)
<doi:10.1007/s43545-023-00658-y> Acknowledgements: The author wish to
thank Conselleria de Economia, Hacienda y Administracion Publica (grant
CIACIO/2023/031) for supporting this research.

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
