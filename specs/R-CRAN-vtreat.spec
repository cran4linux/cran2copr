%global packname  vtreat
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          A Statistically Sound 'data.frame' Processor/Conditioner

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wrapr >= 1.9.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-wrapr >= 1.9.6
Requires:         R-stats 
Requires:         R-CRAN-digest 

%description
A 'data.frame' processor/conditioner that prepares real-world data for
predictive modeling in a statistically sound manner. 'vtreat' prepares
variables so that data has fewer exceptional cases, making it easier to
safely use models in production. Common problems 'vtreat' defends against:
'Inf', 'NA', too many categorical levels, rare categorical levels, and new
categorical levels (levels seen during application, but not during
training). Reference: "'vtreat': a data.frame Processor for Predictive
Modeling", Zumel, Mount, 2016, <DOI:10.5281/zenodo.1173313>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unit_tests
%{rlibdir}/%{packname}/INDEX
