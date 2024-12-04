%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  basicspace
%global packver   0.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.25
Release:          1%{?dist}%{?buildtag}
Summary:          Recovering a Basic Space from Issue Scales

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-tools 
Requires:         R-tools 

%description
Provides functions to estimate latent dimensions of choice and judgment
using Aldrich-McKelvey and Blackbox scaling methods, as described in Poole
et al. (2016, <doi:10.18637/jss.v069.i07>). These techniques allow
researchers (particularly those analyzing political attitudes, public
opinion, and legislative behavior) to recover spatial estimates of
political actors' ideal points and stimuli from issue scale data,
accounting for perceptual bias, multidimensional spaces, and missing data.
The package uses singular value decomposition and alternating least
squares (ALS) procedures to scale self-placement and perceptual data into
a common latent space for the analysis of ideological or evaluative
dimensions. Functionality also include tools for assessing model fit,
handling complex survey data structures, and reproducing simulated
datasets for methodological validation.

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
