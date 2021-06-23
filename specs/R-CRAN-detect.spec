%global __brp_check_rpaths %{nil}
%global packname  detect
%global packver   0.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analyzing Wildlife Data with Detection Error

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-Formula 
Requires:         R-stats4 
Requires:         R-CRAN-pbapply 
Requires:         R-Matrix 

%description
Models for analyzing site occupancy and count data models with detection
error, including single-visit based models, conditional distance sampling
and time-removal models. Package development was supported by the Alberta
Biodiversity Monitoring Institute (<https://www.abmi.ca>) and the Boreal
Avian Modelling Project (<https://borealbirds.ualberta.ca>).

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
