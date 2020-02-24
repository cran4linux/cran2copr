%global packname  fakemake
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}
Summary:          Mock the Unix Make Utility

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MakefileR 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-callr 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MakefileR 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Use R as a minimal build system. This might come in handy if you are
developing R packages and can not use a proper build system. Stay away if
you can (use a proper build system).

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
%doc %{rlibdir}/%{packname}/runit_tests
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
