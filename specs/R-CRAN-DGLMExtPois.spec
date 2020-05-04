%global packname  DGLMExtPois
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Double Generalized Linear Models Extending Poisson Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr >= 1.2.1
BuildRequires:    R-CRAN-COMPoissonReg 
BuildRequires:    R-CRAN-progress 
Requires:         R-CRAN-nloptr >= 1.2.1
Requires:         R-CRAN-COMPoissonReg 
Requires:         R-CRAN-progress 

%description
Model estimation, dispersion testing and diagnosis of hyper-Poisson
Saez-Castillo, A.J. and Conde-Sanchez, A. (2013)
<doi:10.1016/j.csda.2012.12.009> and Conway-Maxwell-Poisson Huang, A.
(2017) <doi:10.1177/1471082X17697749> regression models.

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
%{rlibdir}/%{packname}/INDEX
