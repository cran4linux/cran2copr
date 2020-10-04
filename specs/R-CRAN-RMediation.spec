%global packname  RMediation
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          2%{?dist}%{?buildtag}
Summary:          Mediation Analysis Confidence Intervals

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.0
Requires:         R-core >= 2.11.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-e1071 
Requires:         R-base 
Requires:         R-MASS 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-e1071 

%description
We provide functions to compute confidence intervals (CIs) for a
well-defined nonlinear function of the model parameters (e.g., product of
k coefficients) in single--level and multilevel structural equation
models.

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
