%global packname  MultiPhen
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          A Package to Test for Multi-Trait Association

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-HardyWeinberg 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-MASS 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-HardyWeinberg 
Requires:         R-CRAN-RColorBrewer 

%description
Performs genetic association tests between SNPs (one-at-a-time) and
multiple phenotypes (separately or in joint model).

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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
