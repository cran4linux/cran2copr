%global packname  SurvGSD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Group Sequential Design for a Clinical Trial with CensoredSurvival Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-ldbounds 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-stats 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-ldbounds 
Requires:         R-CRAN-mnormt 
Requires:         R-stats 

%description
Sample size calculation utilizing the information fraction and the alpha
spending function in a group sequential clinical trial with censored
survival data from underlying generalized gamma survival distributions or
log-logistic survival distributions. Hsu, C.-H., Chen, C.-H, Hsu, K.-N.
and Lu, Y.-H. (2018) A useful design utilizing the information fraction in
a group sequential clinical trial with censored survival data. To appear
in Biometrics.

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
