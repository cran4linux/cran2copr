%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ahw
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Continuous Time Likelihood Ratio Weights Assuming Multiplicative Intensity Models and Additive Hazard Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-timereg 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-methods 
Requires:         R-CRAN-timereg 
Requires:         R-CRAN-plyr 

%description
Estimates continuous time weights for performing causal survival analysis.
For instance, weighted Nelson-Aalen or Kaplan-Meier estimates can be given
a causal interpretation. See Ryalen, Stensrud, and Røysland (2019)
<doi:10.1007/s10985-019-09468-y> and Ryalen (2019)
<https://www.duo.uio.no/handle/10852/70353> for theory and examples.

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
