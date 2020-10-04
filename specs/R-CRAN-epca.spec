%global packname  epca
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Exploratory Principal Component Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-GPArotation 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-matlab 
Requires:         R-Matrix 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-GPArotation 

%description
Exploratory principal component analysis for large-scale dataset,
including sparse principal component analysis and sparse matrix
approximation.

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
