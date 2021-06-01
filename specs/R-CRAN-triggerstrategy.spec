%global packname  triggerstrategy
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Trigger Strategy in Clinical Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-gsDesign 
BuildRequires:    R-CRAN-gsrsb 
BuildRequires:    R-CRAN-ldbounds 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-gsDesign 
Requires:         R-CRAN-gsrsb 
Requires:         R-CRAN-ldbounds 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 

%description
The trigger strategy is a general framework for a multistage statistical
design with multiple hypotheses, allowing an adaptive selection of interim
analyses. The selection of interim stages can be associated with some
prespecified endpoints which serve as the trigger. This selection allows
us to refine the critical boundaries in hypotheses testing procedures, and
potentially increase the statistical power. This package includes several
trial designs using the trigger strategy. See Gou, J. (2021). Trigger
strategy in repeated tests on multiple hypotheses, Technical Report
(<https://raw.githubusercontent.com/jgvu/research/manuscripts/triggerStrategyV0git.pdf>)
and Gou, J. (2021). Sample size optimization and initial allocation of the
significance levels in group sequential trials with multiple endpoints,
Biometrical Journal
(<https://onlinelibrary.wiley.com/doi/10.1002/bimj.202000081>).

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
