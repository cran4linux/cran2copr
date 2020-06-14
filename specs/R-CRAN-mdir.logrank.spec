%global packname  mdir.logrank
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          2%{?dist}
Summary:          Multiple-Direction Logrank Test

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-stats 
Requires:         R-MASS >= 7.3.47
Requires:         R-stats 

%description
Implemented are the one-sided and two-sided multiple-direction logrank
test for two-sample right censored data. In addition to the statistics
p-values are calculated: 1. For the one-sided testing problem one p-value
based on a wild bootstrap approach is determined. 2. In the two-sided case
one p-value based on a chi-squared approximation and a second p-values
based on a permutation approach are calculated. Ditzhaus, M. and
Friedrich, S. (2018) <arXiv:1807.05504>. Ditzhaus, M. and Pauly, M. (2018)
<arXiv:1808.05627>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
