%global packname  analogue
%global packver   0.17-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.3
Release:          1%{?dist}
Summary:          Analogue and Weighted Averaging Methods for Palaeoecology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-vegan >= 2.2.0
BuildRequires:    R-CRAN-princurve >= 2.0.2
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-lattice 
Requires:         R-CRAN-vegan >= 2.2.0
Requires:         R-CRAN-princurve >= 2.0.2
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-brglm 
Requires:         R-lattice 

%description
Fits Modern Analogue Technique and Weighted Averaging transfer function
models for prediction of environmental data from species data, and related
methods used in palaeoecology.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ONEWS.Rd
%doc %{rlibdir}/%{packname}/THANKS
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
