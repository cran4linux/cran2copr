%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bpcp
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Beta Product Confidence Procedure for Right Censored Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Calculates nonparametric pointwise confidence intervals for the survival
distribution for right censored data, and for medians [Fay and Brittain
<DOI:10.1002/sim.6905>]. Has two-sample tests for dissimilarity (e.g.,
difference, ratio or odds ratio) in survival at a fixed time, and
differences in medians [Fay, Proschan, and Brittain
<DOI:10.1111/biom.12231>]. Basically, the package gives exact inference
methods for one- and two-sample exact inferences for Kaplan-Meier curves
(e.g., generalizing Fisher's exact test to allow for right censoring),
which are especially important for latter parts of the survival curve,
small sample sizes or heavily censored data. Includes mid-p options.

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
