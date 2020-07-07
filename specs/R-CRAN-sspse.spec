%global packname  sspse
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          3%{?dist}
Summary:          Estimating Hidden Population Size using Respondent DrivenSampling Data

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RDS 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-coda 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-RDS 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-coda 

%description
Estimate the size of a networked population based on respondent-driven
sampling data. The package is part of the "RDS Analyst" suite of packages
for the analysis of respondent-driven sampling data. See Handcock, Gile
and Mar (2014) <doi:10.1214/14-EJS923> and Handcock, Gile and Mar (2015)
<doi:10.1111/biom.12255>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
