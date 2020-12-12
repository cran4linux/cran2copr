%global packname  FactoInvestigate
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Description of Factorial Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-FactoMineR 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-rmarkdown 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 

%description
Brings a set of tools to help and automatically realise the description of
principal component analyses (from 'FactoMineR' functions). Detection of
existing outliers, identification of the informative components, graphical
views and dimensions description are performed threw dedicated functions.
The Investigate() function performs all these functions in one, and
returns the result as a report document (Word, PDF or HTML).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
