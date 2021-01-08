%global packname  nmm
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Nonlinear Multivariate Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-mlogit 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-mlogit 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 

%description
Estimates a subset of nonlinear multivariate models (NMM): system of
nonlinear regressions (SNR), logit, and a joint model of SNR and logit.
'nmm' uniquely accounts for correlations between the error terms from
nonlinear regressions and the probabilities from logit models. It also
enables a very flexible design of logit: alternative-specific indirect
utilities, individual-specific choice set and number of actual choices.

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
