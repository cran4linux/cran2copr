%global packname  LTRCforests
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Methods for Survival Data with Time-Varying Covariates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-ipred 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-partykit 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-survival 
Requires:         R-CRAN-ipred 
Requires:         R-parallel 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-partykit 

%description
Implements the conditional inference forest and random survival forest
algorithm to modeling left-truncated right-censored data with
time-invariant covariates, and (left-truncated) right-censored survival
data with time-varying covariates. It also provides functions to tune the
parameters and evaluate the model fit. See Yao et al. (2020)
<arXiv:2006.00567>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
