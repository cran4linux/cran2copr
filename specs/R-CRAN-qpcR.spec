%global __brp_check_rpaths %{nil}
%global packname  qpcR
%global packver   1.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Modelling and Analysis of Real-Time PCR Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-MASS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-robustbase 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Model fitting, optimal model selection and calculation of various features
that are essential in the analysis of quantitative real-time polymerase
chain reaction (qPCR).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/add01
%doc %{rlibdir}/%{packname}/add02
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
