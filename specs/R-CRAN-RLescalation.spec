%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RLescalation
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Dose Escalation Using Deep Reinforcement Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-zip 

%description
An implementation to compute an optimal dose escalation rule using deep
reinforcement learning in phase I oncology trials (Matsuura et al. (2023)
<doi:10.1080/10543406.2023.2170402>). The dose escalation rule can
directly optimize the percentages of correct selection (PCS) of the
maximum tolerated dose (MTD).

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
