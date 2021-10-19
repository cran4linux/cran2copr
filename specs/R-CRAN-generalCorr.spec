%global __brp_check_rpaths %{nil}
%global packname  generalCorr
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Correlations and Various Causal Paths

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable >= 1.8
BuildRequires:    R-CRAN-meboot >= 1.4
BuildRequires:    R-CRAN-np >= 0.60
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-xtable >= 1.8
Requires:         R-CRAN-meboot >= 1.4
Requires:         R-CRAN-np >= 0.60
Requires:         R-CRAN-psych 
Requires:         R-CRAN-lattice 

%description
Since causal paths from data are important for all sciences, the package
provides many sophisticated functions. causeSummBlk() gives
easy-to-interpret causal paths.  Let Z denote control variables and
compare two flipped kernel regressions: X=f(Y, Z)+e1 and Y=g(X,Z)+e2. Our
criterion Cr1 says that if |e1*Y|>|e2*X| then variation in X is more
"exogenous or independent" than in Y and causal path is X to Y. Criterion
Cr2 requires |e2|<|e1|. These inequalities between many absolute values
are quantified by four orders of stochastic dominance. Our third criterion
Cr3 for the causal path X to Y requires new generalized partial
correlations to satisfy |r*(x|y,z)|< |r*(y|x,z)|. The function parcorVec()
reports generalized partials between the first variable and all others.
The package provides several R functions including get0outliers() for
outlier detection, bigfp() for numerical integration by the trapezoidal
rule, stochdom2() for stochastic dominance, pillar3D() for 3D charts,
canonRho() for generalized canonical correlations, depMeas() measures
nonlinear dependence, and causeSummary(mtx) reports summary of causal
paths among matrix columns is easiest to use. Several functions whose
names begin with 'boot' provide bootstrap statistical inference including
a new bootGcRsq() test for "Granger-causality" allowing nonlinear
relations. See five vignettes of the package for theory and usage tips.
See Vinod (2019) doi{10.1080/03610918.2015.1122048}.

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
