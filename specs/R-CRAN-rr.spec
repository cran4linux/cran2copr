%global __brp_check_rpaths %{nil}
%global packname  rr
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Methods for the Randomized Response Technique

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-magic 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-magic 

%description
Enables researchers to conduct multivariate statistical analyses of survey
data with randomized response technique items from several designs,
including mirrored question, forced question, and unrelated question. This
includes regression with the randomized response as the outcome and
logistic regression with the randomized response item as a predictor. In
addition, tools for conducting power analysis for designing randomized
response items are included. The package implements methods described in
Blair, Imai, and Zhou (2015) ''Design and Analysis of the Randomized
Response Technique,'' Journal of the American Statistical Association
<https://graemeblair.com/papers/randresp.pdf>.

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
