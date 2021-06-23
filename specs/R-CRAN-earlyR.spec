%global __brp_check_rpaths %{nil}
%global packname  earlyR
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Transmissibility in the Early Stages of a Disease Outbreak

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-distcrete 
BuildRequires:    R-CRAN-EpiEstim 
BuildRequires:    R-CRAN-epitrix 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-distcrete 
Requires:         R-CRAN-EpiEstim 
Requires:         R-CRAN-epitrix 
Requires:         R-CRAN-ggplot2 

%description
Implements a simple, likelihood-based estimation of the reproduction
number (R0) using a branching process with a Poisson likelihood. This
model requires knowledge of the serial interval distribution, and dates of
symptom onsets. Infectiousness is determined by weighting R0 by the
probability mass function of the serial interval on the corresponding day.
It is a simplified version of the model introduced by Cori et al. (2013)
<doi:10.1093/aje/kwt133>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
