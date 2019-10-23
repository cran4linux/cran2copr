%global packname  BCA
%global packver   0.9-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Business and Customer Analytics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.1.0
BuildRequires:    R-CRAN-car >= 2.0.21
BuildRequires:    R-CRAN-RcmdrMisc >= 1.0.1
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-clv 
Requires:         R-CRAN-Rcmdr >= 2.1.0
Requires:         R-CRAN-car >= 2.0.21
Requires:         R-CRAN-RcmdrMisc >= 1.0.1
Requires:         R-rpart 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-clv 

%description
Underlying support functions for RcmdrPlugin.BCA and a companion to the
book Customer and Business Analytics: Applied Data Mining for Business
Decision Making Using R by Daniel S. Putler and Robert E. Krider

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
%doc %{rlibdir}/%{packname}/CHANGES
%{rlibdir}/%{packname}/INDEX
