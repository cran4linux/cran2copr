%global packname  plm
%global packver   2.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Models for Panel Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-CRAN-zoo 
Requires:         R-nlme 
Requires:         R-CRAN-sandwich 
Requires:         R-lattice 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Formula 
Requires:         R-stats 

%description
A set of estimators and tests for panel data econometrics, as described in
Baltagi (2013) Econometric Analysis of Panel Data,
ISBN-13:978-1-118-67232-7, Hsiao (2014) Analysis of Panel Data
<doi:10.1017/CBO9781139839327> and Croissant and Millo (2018), Panel Data
Econometrics with R, ISBN:978-1-118-94918-4.

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
