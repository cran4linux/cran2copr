%global packname  NRejections
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Metrics for Multiple Testing with Correlated Outcomes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-StepwiseTest 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-StepwiseTest 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mvtnorm 

%description
Implements methods in Mathur and VanderWeele (in preparation) to
characterize global evidence strength across W correlated ordinary least
squares (OLS) hypothesis tests. Specifically, uses resampling to estimate
a null interval for the total number of rejections in, for example, 95% of
samples generated with no associations (the global null), the excess hits
(the difference between the observed number of rejections and the upper
limit of the null interval), and a test of the global null based on the
number of rejections.

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
