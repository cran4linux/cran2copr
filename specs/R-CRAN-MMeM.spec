%global packname  MMeM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Multivariate Mixed Effects Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-jointDiag 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-jointDiag 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-stringr 

%description
Analyzing data under multivariate mixed effects model using multivariate
REML and multivariate Henderson3 methods. See Meyer (1985)
<doi:10.2307/2530651> and Wesolowska Janczarek (1984)
<doi:10.1002/bimj.4710260613>.

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
