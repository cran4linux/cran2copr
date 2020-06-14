%global packname  IndependenceTests
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          2%{?dist}
Summary:          Non-Parametric Tests of Independence Between Random Vectors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.0
Requires:         R-core >= 2.3.0
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Runuran 
BuildRequires:    R-parallel 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-MASS 
Requires:         R-CRAN-Runuran 
Requires:         R-parallel 

%description
Functions for non-parametric tests of independence (mutual or serial)
between some quantitative random vectors.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/HISTORY
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
