%global packname  cem
%global packver   1.1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.20
Release:          3%{?dist}
Summary:          Coarsened Exact Matching

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-nlme 
Requires:         R-tcltk 
Requires:         R-lattice 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-randomForest 
Requires:         R-nlme 

%description
Implementation of the Coarsened Exact Matching algorithm.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/makeLelonde.R
%{rlibdir}/%{packname}/INDEX
