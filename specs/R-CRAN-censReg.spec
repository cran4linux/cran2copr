%global packname  censReg
%global packver   0.5-30
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.30
Release:          1%{?dist}
Summary:          Censored Regression (Tobit) Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.2.6
BuildRequires:    R-stats >= 2.15.0
BuildRequires:    R-CRAN-glmmML >= 0.81.6
BuildRequires:    R-CRAN-maxLik >= 0.7.3
BuildRequires:    R-CRAN-miscTools >= 0.6.11
BuildRequires:    R-CRAN-plm 
Requires:         R-CRAN-sandwich >= 2.2.6
Requires:         R-stats >= 2.15.0
Requires:         R-CRAN-glmmML >= 0.81.6
Requires:         R-CRAN-maxLik >= 0.7.3
Requires:         R-CRAN-miscTools >= 0.6.11
Requires:         R-CRAN-plm 

%description
Maximum Likelihood estimation of censored regression (Tobit) models with
cross-sectional and panel data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
