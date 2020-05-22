%global packname  car
%global packver   3.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.8
Release:          1%{?dist}
Summary:          Companion to Applied Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-carData >= 3.0.0
BuildRequires:    R-CRAN-pbkrtest >= 0.4.4
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-nlme 
Requires:         R-CRAN-carData >= 3.0.0
Requires:         R-CRAN-pbkrtest >= 0.4.4
Requires:         R-CRAN-abind 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-nnet 
Requires:         R-CRAN-quantreg 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-lme4 
Requires:         R-nlme 

%description
Functions to Accompany J. Fox and S. Weisberg, An R Companion to Applied
Regression, Third Edition, Sage, 2019.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
