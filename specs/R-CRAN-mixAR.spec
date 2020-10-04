%global packname  mixAR
%global packver   0.22.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22.4
Release:          2%{?dist}%{?buildtag}
Summary:          Mixture Autoregressive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-gbutils >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-gbutils >= 0.3.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-stats4 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-mvtnorm 

%description
Model time series using mixture autoregressive (MAR) models.  Implemented
are frequentist (EM) and Bayesian methods for estimation, prediction and
model evaluation. See Wong and Li (2002) <doi:10.1111/1467-9868.00222>,
Boshnakov (2009) <doi:10.1016/j.spl.2009.04.009>), and the extensive
references in the documentation.

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
