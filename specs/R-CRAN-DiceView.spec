%global packname  DiceView
%global packver   2.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Methods for Visualization of Computer Experiments Design andSurrogate

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-DiceEval 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-geometry 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-DiceEval 
Requires:         R-CRAN-DiceDesign 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-geometry 

%description
View 2D/3D sections, contour plots, mesh of excursion sets for computer
experiments designs, surrogates or test functions.

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
