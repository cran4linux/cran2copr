%global packname  lgr
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          3%{?dist}
Summary:          A Fully Featured Logging Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-R6 >= 2.4.0

%description
A flexible, feature-rich yet light-weight logging framework based on 'R6'
classes. It supports hierarchical loggers, custom log levels, arbitrary
data fields in log events, logging to plaintext, 'JSON', (rotating) files,
memory buffers, and databases, as well as email and push notifications.
For a full list of features with examples please refer to the package
vignette.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/benchmarks
%doc %{rlibdir}/%{packname}/configs
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/draft_vignettes
%doc %{rlibdir}/%{packname}/logger_comparison
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
