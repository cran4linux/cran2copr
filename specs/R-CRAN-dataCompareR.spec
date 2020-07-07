%global packname  dataCompareR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}
Summary:          Compare Two Data Frames and Summarise the Difference

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-markdown 
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-markdown 

%description
Easy comparison of two tabular data objects in R. Specifically designed to
show differences between two sets of data in a useful way that should make
it easier to understand the differences, and if necessary, help you work
out how to remedy them. Aims to offer a more useful output than
all.equal() when your two data sets do not match, but isn't intended to
replace all.equal() as a way to test for equality.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/css
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
