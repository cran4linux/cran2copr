%global packname  SimplifyStats
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Simplifies Pairwise Statistical Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4.2
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-broom >= 0.4.4
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-moments >= 0.14
Requires:         R-CRAN-tibble >= 1.4.2
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-broom >= 0.4.4
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-moments >= 0.14

%description
Pairwise group comparisons are often performed. While there are many
packages that can perform these analyses, often it is the case that only a
subset of comparisons are desired. 'SimplifyStats' performs pairwise
comparisons and returns the results in a tidy fashion.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
