%global packname  mdsdt
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Functions for Analysis of Data with General Recognition Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-polycor 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-polycor 

%description
Tools associated with General Recognition Theory (Townsend & Ashby, 1986),
including Gaussian model fitting of 2x2 and more general designs,
associated plotting and model comparison tools, and tests of marginal
response invariance and report independence.

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
