%global packname  cccrm
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          Concordance Correlation Coefficient for Repeated (andNon-Repeated) Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-nlme 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-tidyselect 

%description
Estimates the Concordance Correlation Coefficient to assess agreement. The
scenarios considered are non-repeated measures, non-longitudinal repeated
measures (replicates) and longitudinal repeated measures. The estimation
approaches implemented are variance components and U-statistics
approaches.

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
