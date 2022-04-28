%global __brp_check_rpaths %{nil}
%global packname  maic
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Matching-Adjusted Indirect Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-weights 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-weights 

%description
A generalised workflow for generation of subject weights to be used in
Matching-Adjusted Indirect Comparison (MAIC) per Signorovitch et al.
(2012) <doi:10.1016/j.jval.2012.05.004>, Signorovitch et al (2010)
<doi:10.2165/11538370-000000000-00000>. In MAIC, unbiased comparison
between outcomes of two trials is facilitated by weighting the
subject-level outcomes of one trial with weights derived such that the
weighted aggregate measures of the prognostic or effect modifying
variables are equal to those of the sample in the comparator trial. The
functions and classes included in this package wrap and abstract the
process demonstrated in the UK National Institute for Health and Care
Excellence Decision Support Unit (NICE DSU)'s example (Phillippo et al,
(2016) [see URL]), providing a repeatable and easily specifiable workflow
for producing multiple comparison variable sets against a variety of
target studies, with preprocessing for a number of aggregate target forms
(e.g. mean, median, domain limits).

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
