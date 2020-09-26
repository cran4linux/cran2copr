%global packname  ftsa
%global packver   5.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.9
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Time Series Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-rainbow 
BuildRequires:    R-CRAN-sde 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-pdfCluster 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-rainbow 
Requires:         R-CRAN-sde 
Requires:         R-CRAN-colorspace 
Requires:         R-MASS 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-pdfCluster 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-e1071 

%description
Functions for visualizing, modeling, forecasting and hypothesis testing of
functional time series.

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
