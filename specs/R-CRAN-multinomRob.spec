%global __brp_check_rpaths %{nil}
%global packname  multinomRob
%global packver   1.8-6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Estimation of Overdispersed Multinomial Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.7.1
Requires:         R-core >= 1.7.1
BuildRequires:    R-MASS >= 7.1.8
BuildRequires:    R-CRAN-rgenoud >= 2.9
BuildRequires:    R-CRAN-mvtnorm >= 0.6.3
Requires:         R-MASS >= 7.1.8
Requires:         R-CRAN-rgenoud >= 2.9
Requires:         R-CRAN-mvtnorm >= 0.6.3

%description
MNL and overdispersed multinomial regression using robust (LQD and tanh)
estimation

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
