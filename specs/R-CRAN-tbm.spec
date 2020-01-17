%global packname  tbm
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Transformation Boosting Machines

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost >= 2.8.2
BuildRequires:    R-CRAN-mlt >= 1.0.6
BuildRequires:    R-CRAN-variables 
BuildRequires:    R-CRAN-basefun 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-methods 
Requires:         R-CRAN-mboost >= 2.8.2
Requires:         R-CRAN-mlt >= 1.0.6
Requires:         R-CRAN-variables 
Requires:         R-CRAN-basefun 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-coneproj 
Requires:         R-methods 

%description
Boosting the likelihood of conditional and shift transformation models.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/applications
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/README.txt
%doc %{rlibdir}/%{packname}/simulations
%{rlibdir}/%{packname}/INDEX
