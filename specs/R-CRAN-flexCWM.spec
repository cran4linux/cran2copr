%global packname  flexCWM
%global packver   1.92
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.92
Release:          2%{?dist}
Summary:          Flexible Cluster-Weighted Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-ContaminatedMixt 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-ContaminatedMixt 

%description
Allows maximum likelihood fitting of cluster-weighted models, a class of
mixtures of regression models with random covariates. Methods are
described in Angelo Mazza, Antonio Punzo, Salvatore Ingrassia (2018)
<doi:10.18637/jss.v086.i02>.

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
