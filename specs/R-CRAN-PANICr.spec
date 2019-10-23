%global packname  PANICr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          PANIC Tests of Nonstationarity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-coda 

%description
A methodology that makes use of the factor structure of large dimensional
panels to understand the nature of nonstationarity inherent in data. This
is referred to as PANIC, Panel Analysis of Nonstationarity in
Idiosyncratic and Common Components. PANIC
(2004)<doi:10.1111/j.1468-0262.2004.00528.x> includes valid pooling
methods that allow panel tests to be constructed. PANIC (2004) can detect
whether the nonstationarity in a series is pervasive, or variable
specific, or both. PANIC (2010) <doi:10.1017/s0266466609990478> includes
two new tests on the idiosyncratic component that estimates the pooled
autoregressive coefficient and sample moment, respectively. The PANIC
model approximates the number of factors based on Bai and Ng (2002)
<doi:10.1111/1468-0262.00273>.

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
%{rlibdir}/%{packname}/test_data
%{rlibdir}/%{packname}/INDEX
