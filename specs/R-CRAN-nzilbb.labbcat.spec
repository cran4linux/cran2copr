%global packname  nzilbb.labbcat
%global packver   0.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Accessing Data Stored in 'LaBB-CAT' Instances

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-rstudioapi 

%description
'LaBB-CAT' is a web-based language corpus management system developed by
the New Zealand Institute of Language, Brain and Behaviour (NZILBB) - see
<https://labbcat.canterbury.ac.nz>. This package defines functions for
accessing corpus data in a 'LaBB-CAT' instance. You must have at least
version 20200608.1507 of 'LaBB-CAT' to use this package. For more
information about 'LaBB-CAT', see Robert Fromont and Jennifer Hay (2008)
<doi:10.3366/E1749503208000142> or Robert Fromont (2017)
<doi:10.1016/j.csl.2017.01.004>.

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
