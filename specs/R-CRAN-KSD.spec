%global packname  KSD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests using Kernelized Stein Discrepancy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-pryr 
Requires:         R-graphics 
Requires:         R-stats 

%description
An adaptation of Kernelized Stein Discrepancy, this package provides a
goodness-of-fit test of whether a given i.i.d. sample is drawn from a
given distribution. It works for any distribution once its score function
(the derivative of log-density) can be provided. This method is based on
"A Kernelized Stein Discrepancy for Goodness-of-fit Tests and Model
Evaluation" by Liu, Lee, and Jordan, available at
<http://arxiv.org/abs/1602.03253>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
