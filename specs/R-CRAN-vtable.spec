%global packname  vtable
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Variable Table for Variable Documentation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-sjlabelled 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-sjlabelled 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-knitr 

%description
Automatically generates HTML variable documentation including variable
names, labels, classes, value labels (if applicable), value ranges, and
summary statistics. See the vignette "vtable" for a package overview.

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
