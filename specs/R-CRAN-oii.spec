%global packname  oii
%global packver   1.0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Crosstab and Statistical Tests for OII MSc Stats Course

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rapportools 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-Deducer 
Requires:         R-CRAN-rapportools 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-Deducer 

%description
Provides simple crosstab output with optional statistics (e.g.,
Goodman-Kruskal Gamma, Somers' d, and Kendall's tau-b) as well as two-way
and one-way tables. The package is used within the statistics component of
the Masters of Science (MSc) in Social Science of the Internet at the
Oxford Internet Institute (OII), University of Oxford, but the functions
should be useful for general data analysis and especially for analysis of
categorical and ordinal data.

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
%{rlibdir}/%{packname}/INDEX
