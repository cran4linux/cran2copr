%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aplime
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Piecewise Local Model-Agnostic Explanations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-earth 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements Adaptive Piecewise Local Interpretable Model-Agnostic
Explanations (AP-LIME) and its second-order interaction extension
(AP2-LIME) for interpreting predictions from machine learning models. The
methods replace the conventional locally weighted linear surrogate in LIME
with Multivariate Adaptive Regression Splines (MARS). AP-LIME uses
additive piecewise-linear hinge functions, whereas AP2-LIME allows
pairwise interactions between hinge functions. The package generates
proximity-weighted local explanations, estimates feature contributions,
evaluates local surrogate fit, and assesses explanation stability across
repeated runs. Stability is measured using the Variables Stability Index
(VSI) and Coefficients Stability Index (CSI), including normal-theory and
percentile bootstrap confidence intervals. MARS terms with the same
predictors, hinge directions, and interaction structure are matched
independently of knot locations. Coefficients within matched groups are
summarized by their arithmetic mean, while the original knot thresholds
remain available for inspection. The MARS-based local explanation approach
is discussed by Somuncuoglu and Purutcuoglu (2027,
ISBN:978-1-041-34431-5), "Explainable AI Approaches in Biomedical Signals:
A Case Study with Pima Indians Diabetes Dataset", in "Biomedical Data
Science: A Focus on Signaling", CRC Press.

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
