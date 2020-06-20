%global packname  WebPower
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Basic and Advanced Statistical Power Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-PearsonDS 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lavaan 
Requires:         R-parallel 
Requires:         R-CRAN-PearsonDS 

%description
This is a collection of tools for conducting both basic and advanced
statistical power analysis including correlation, proportion, t-test,
one-way ANOVA, two-way ANOVA, linear regression, logistic regression,
Poisson regression, mediation analysis, longitudinal data analysis,
structural equation modeling and multilevel modeling. It also serves as
the engine for conducting power analysis online at
<https://webpower.psychstat.org>.

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

%files
%{rlibdir}/%{packname}
