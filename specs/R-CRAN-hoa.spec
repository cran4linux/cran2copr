%global packname  hoa
%global packver   2.1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4.1
Release:          3%{?dist}
Summary:          Higher Order Likelihood Inference

License:          GPL (>= 2) | file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-utils 

%description
Performs likelihood-based inference for a wide range of regression models.
Provides higher-order approximations for inference based on extensions of
saddlepoint type arguments as discussed in the book Applied Asymptotics:
Case Studies in Small-Sample Statistics by Brazzale, Davison, and Reid
(2007).

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/margdemo.R
%{rlibdir}/%{packname}/INDEX
