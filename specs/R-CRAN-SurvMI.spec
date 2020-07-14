%global packname  SurvMI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Multiple Imputation Method in Survival Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-survival >= 3.1.11
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-base 
Requires:         R-survival >= 3.1.11
Requires:         R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-base 

%description
In clinical trials, endpoints are sometimes evaluated with uncertainty.
Adjudication is commonly adopted to ensure the study integrity. We propose
to use multiple imputation (MI) introduced by Robin (1987)
<doi:10.1002/9780470316696> to incorporate these uncertainties if
reasonable event probabilities were provided. The method has been applied
to Cox Proportional Hazard (PH) model, Kaplan-Meier (KM) estimation and
Log-rank test in this package. Moreover, weighted estimations discussed in
Cook (2004) <doi:10.1016/S0197-2456(00)00053-2> were also implemented with
weights calculated from event probabilities. In conclusion, this package
can handle time-to-event analysis if events presented with uncertainty by
different methods.

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
