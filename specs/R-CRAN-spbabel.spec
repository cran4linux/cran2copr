%global packname  spbabel
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Convert Spatial Data Using Tidy Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
Tools to convert from specific formats to more general forms of spatial
data. Using tables to store the actual entities present in spatial data
provides flexibility, and the functions here deliberately minimize the
level of interpretation applied, leaving that for specific applications.
Includes support for simple features, round-trip for 'Spatial' classes and
long-form tables, analogous to 'ggplot2::fortify'. There is also a more
'normal form' representation that decomposes simple features and their kin
to tables of objects, parts, and unique coordinates.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/devignette
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/sf_convert.r
%doc %{rlibdir}/%{packname}/sf_convert2.r
%{rlibdir}/%{packname}/INDEX
