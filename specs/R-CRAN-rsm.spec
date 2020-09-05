%global packname  rsm
%global packver   2.10.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.10.2
Release:          1%{?dist}%{?buildtag}
Summary:          Response-Surface Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-estimability 
Requires:         R-CRAN-estimability 

%description
Provides functions to generate response-surface designs, fit first- and
second-order response-surface models, make surface plots, obtain the path
of steepest ascent, and do canonical analysis. A good reference on these
methods is Chapter 10 of Wu, C-F J and Hamada, M (2009) "Experiments:
Planning, Analysis, and Parameter Design Optimization" ISBN
978-0-471-69946-0.

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
