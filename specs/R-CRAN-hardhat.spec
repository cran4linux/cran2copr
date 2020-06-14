%global packname  hardhat
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Construct Modeling Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tibble 

%description
Building modeling packages is hard. A large amount of effort generally
goes into providing an implementation for a new method that is efficient,
fast, and correct, but often less emphasis is put on the user interface. A
good interface requires specialized knowledge about S3 methods and
formulas, which the average package developer might not have. The goal of
'hardhat' is to reduce the burden around building new modeling packages by
providing functionality for preprocessing, predicting, and validating
input.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
