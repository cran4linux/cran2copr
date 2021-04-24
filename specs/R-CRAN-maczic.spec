%global packname  maczic
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mediation Analysis for Count and Zero-Inflated Count Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mediation 
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pscl 
Requires:         R-graphics 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-mediation 
Requires:         R-CRAN-emplik 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-mathjaxr 

%description
Performs causal mediation analysis for count and zero-inflated count data
without or with a post-treatment confounder; calculates power to detect
prespecified causal mediation effects, direct effects, and total effects;
performs sensitivity analysis when there is a treatment- induced
mediator-outcome confounder as described by Cheng, J., Cheng, N.F., Guo,
Z., Gregorich, S., Ismail, A.I., Gansky, S.A. (2018)
<doi:10.1177/0962280216686131>. Implements Instrumental Variable (IV)
method to estimate the controlled (natural) direct and mediation effects,
and compute the bootstrap Confidence Intervals as described by Guo, Z.,
Small, D.S., Gansky, S.A., Cheng, J. (2018) <doi:10.1111/rssc.12233>. This
software was made possible by Grant R03DE028410 from the The National
Institute of Dental and Craniofacial Research, a component of the National
Institutes of Health.

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
