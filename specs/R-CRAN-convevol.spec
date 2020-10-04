%global packname  convevol
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Analysis of Convergent Evolution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-geiger 
Requires:         R-CRAN-phytools 
Requires:         R-MASS 
Requires:         R-CRAN-ape 
Requires:         R-cluster 
Requires:         R-CRAN-geiger 

%description
Quantifies and assesses the significance of convergent evolution using two
different methods (and 5 different measures) as described in Stayton
(2015) <DOI: 10.1111/evo.12729>.  Also displays results in a
phylomorphospace framework.

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
