%global __brp_check_rpaths %{nil}
%global packname  PredictionR
%global packver   1.0-12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          3%{?dist}%{?buildtag}
Summary:          Prediction for Future Data from any Continuous Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-Renext 
Requires:         R-stats 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-Renext 

%description
Functions to get prediction intervals and prediction points of future
observations from any continuous distribution.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
