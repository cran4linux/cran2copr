%global packname  TFisher
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Optimal Thresholding Fisher's P-Value Combination Method

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-Matrix 

%description
We provide the cumulative distribution function (CDF), quantile, and
statistical power calculator for a collection of thresholding Fisher's
p-value combination methods, including Fisher's p-value combination
method, truncated product method and, in particular, soft-thresholding
Fisher's p-value combination method which is proven to be optimal in some
context of signal detection. The p-value calculator for the omnibus
version of these tests are also included. For reference, please see Hong
Zhang and Zheyang Wu. "TFisher Tests: Optimal and Adaptive Thresholding
for Combining p-Values", submitted.

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
