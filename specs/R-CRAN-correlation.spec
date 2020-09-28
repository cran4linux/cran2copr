%global packname  correlation
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Correlation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 0.8.0
BuildRequires:    R-CRAN-bayestestR >= 0.5.0
BuildRequires:    R-CRAN-parameters >= 0.5.0
BuildRequires:    R-CRAN-effectsize >= 0.2.0
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
Requires:         R-CRAN-insight >= 0.8.0
Requires:         R-CRAN-bayestestR >= 0.5.0
Requires:         R-CRAN-parameters >= 0.5.0
Requires:         R-CRAN-effectsize >= 0.2.0
Requires:         R-datasets 
Requires:         R-stats 

%description
Lightweight package for computing different kinds of correlations, such as
partial correlations, Bayesian correlations, multilevel correlations,
polychoric correlations, biweight correlations, distance correlations and
more. Relies on the easystats ecosystem (Lüdecke, Waggoner & Makowski
(2019) <doi:10.21105/joss.01412>).

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
