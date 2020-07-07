%global packname  lss2
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          The Accelerated Failure Time Model to Right Censored Data Basedon Least-Squares Principle

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-quantreg 

%description
Due to lack of proper inference procedure and software, the ordinary
linear regression model is seldom used in practice for the analysis of
right censored data. This paper presents an S-Plus/R program that
implements a recently developed inference procedure (Jin, Lin and Ying,
2006) <doi:10.1093/biomet/93.1.147> for the accelerated failure time model
based on the least-squares principle.

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
