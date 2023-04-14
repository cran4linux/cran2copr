%global __brp_check_rpaths %{nil}
%global packname  CADFtest
%global packver   0.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          A Package to Perform Covariate Augmented Dickey-Fuller Unit RootTests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dynlm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
Requires:         R-CRAN-dynlm 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 

%description
Hansen's (1995) Covariate-Augmented Dickey-Fuller (CADF) test. The only
required argument is y, the Tx1 time series to be tested. If no stationary
covariate X is passed to the procedure, then an ordinary ADF test is
performed. The p-values of the test are computed using the procedure
illustrated in Lupi (2009).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
