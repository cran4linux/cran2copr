%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  segregatr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Segregation Analysis for Variant Interpretation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.2.0
BuildRequires:    R-CRAN-pedprobr 
Requires:         R-CRAN-pedtools >= 2.2.0
Requires:         R-CRAN-pedprobr 

%description
An implementation of the full-likelihood Bayes factor (FLB) for evaluating
segregation evidence in clinical medical genetics. The method was
introduced by Thompson et al. (2003) <doi:10.1086/378100>. This
implementation supports custom penetrance values and liability classes,
and allows visualisations and robustness analysis as presented in Ratajska
et al. (2023) <doi:10.1002/mgg3.2107>. See also the online app 'shinyseg',
<https://chrcarrizosa.shinyapps.io/shinyseg>, which offers interactive
segregation analysis with many additional features (Carrizosa et al.
(2024) <doi:10.1093/bioinformatics/btae201>).

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
