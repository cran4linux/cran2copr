%global packname  penalizedSVM
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Feature Selection SVM using Penalty Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-lhs 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mlegp 
Requires:         R-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-lhs 

%description
Support Vector Machine (SVM) classification with simultaneous feature
selection using penalty functions is implemented. The smoothly clipped
absolute deviation (SCAD), 'L1-norm', 'Elastic Net' ('L1-norm' and
'L2-norm') and 'Elastic SCAD' (SCAD and 'L2-norm') penalties are
available. The tuning parameters can be found using either a fixed grid or
a interval search.

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
%{rlibdir}/%{packname}/INDEX
