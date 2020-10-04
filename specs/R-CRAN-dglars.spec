%global packname  dglars
%global packver   2.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Differential Geometric Least Angle Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Differential geometric least angle regression method for fitting sparse
generalized linear models. In this version of the package, the user can
fit models specifying Gaussian, Poisson, Binomial, Gamma and Inverse
Gaussian family. Furthermore, several link functions can be used to model
the relationship between the conditional expected value of the response
variable and the linear predictor. The solution curve can be computed
using an efficient predictor-corrector or a cyclic coordinate descent
algorithm, as described in the paper linked to via the URL below.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
