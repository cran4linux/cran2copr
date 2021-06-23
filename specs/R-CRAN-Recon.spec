%global __brp_check_rpaths %{nil}
%global packname  Recon
%global packver   0.3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computational Tools for Economics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 

%description
Implements solutions to canonical models of Economics such as Monopoly
Profit Maximization, Cournot's Duopoly, Solow (1956,
<doi:10.2307/1884513>) growth model and Mankiw, Romer and Weil (1992,
<doi:10.2307/2118477>) growth model.

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
