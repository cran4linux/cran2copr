%global __brp_check_rpaths %{nil}
%global packname  riskPredictClustData
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing Risk Predictions for Clustered Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 

%description
Assessing and comparing risk prediction rules for clustered data. The
method is based on the paper: Rosner B, Qiu W, and Lee MLT.(2013) <doi:
10.1007/s10985-012-9240-6>.

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
