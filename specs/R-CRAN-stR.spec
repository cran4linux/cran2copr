%global __brp_check_rpaths %{nil}
%global packname  stR
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          STR Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgl 
Requires:         R-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-rgl 

%description
Methods for decomposing seasonal data: STR (a Seasonal-Trend decomposition
procedure based on Regression) and Robust STR. In some ways, STR is
similar to Ridge Regression and Robust STR can be related to LASSO. They
allow for multiple seasonal components, multiple linear covariates with
constant, flexible and seasonal influence. Seasonal patterns (for both
seasonal components and seasonal covariates) can be fractional and
flexible over time; moreover they can be either strictly periodic or have
a more complex topology. The methods provide confidence intervals for the
estimated components. The methods can be used for forecasting.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
