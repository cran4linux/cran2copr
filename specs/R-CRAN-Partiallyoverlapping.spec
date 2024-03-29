%global __brp_check_rpaths %{nil}
%global packname  Partiallyoverlapping
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Partially Overlapping Samples Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Tests for a comparison of two partially overlapping samples. A comparison
of means using the partially overlapping samples t-test: See Derrick,
Russ, Toher and White (2017), Test statistics for the comparison of means
for two samples which include both paired observations and independent
observations, Journal of Modern Applied Statistical Methods, 16(1). A
comparison of proportions using the partially overlapping samples z-test:
See Derrick, Dobson-Mckittrick, Toher and White (2015), Test statistics
for comparing two proportions with partially overlapping samples. Journal
of Applied Quantitative Methods, 10(3).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
