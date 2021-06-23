%global __brp_check_rpaths %{nil}
%global packname  survRatio
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating, Comparing and Visualising Time to Event Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 2.38.3
BuildRequires:    R-CRAN-ggplot2 > 2.1.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggpubr 
Requires:         R-CRAN-survival >= 2.38.3
Requires:         R-CRAN-ggplot2 > 2.1.0
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggpubr 

%description
The 'survRatio', provides numerical and graphical summaries for time to
event data. In this release functions are provided to estimate and compare
estimated survivor functions, the ratio of survivor functions and the
difference of survivor functions in independent and paired time to event
problems. Time intervals where the survival prospects may differ are
identified using pointwise confidence bands. See "Survival ratio plots
with permutation envelopes in survival data problems" by Newell J, et al.
(2006) <doi:10.1016/j.compbiomed.2005.03.005>.

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
