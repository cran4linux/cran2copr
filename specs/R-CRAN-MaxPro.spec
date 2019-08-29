%global packname  MaxPro
%global packver   4.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.2
Release:          1%{?dist}
Summary:          Maximum Projection Designs

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-nloptr 

%description
Generate maximum projection (MaxPro) designs for quantitative and/or
qualitative factors. Details of the MaxPro criterion can be found in: (1)
Joseph, Gul, and Ba. (2015) "Maximum Projection Designs for Computer
Experiments", Biometrika, 102, 371-380, and (2) Joseph, Gul, and Ba.
(2018) "Designing Computer Experiments with Multiple Types of Factors: The
MaxPro Approach", Journal of Quality Technology, to appear.

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
%{rlibdir}/%{packname}/libs
