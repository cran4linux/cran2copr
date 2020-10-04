%global packname  glmnet
%global packver   4.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Lasso and Elastic-Net Regularized Generalized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-Matrix >= 1.0.6
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-survival 
Requires:         R-Matrix >= 1.0.6
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-shape 
Requires:         R-survival 

%description
Extremely efficient procedures for fitting the entire lasso or elastic-net
regularization path for linear regression, logistic and multinomial
regression models, Poisson regression, Cox model, multiple-response
Gaussian, and the grouped multinomial regression. There are two new and
important additions. The family argument can be a GLM family object, which
opens the door to any programmed family. This comes with a modest
computational cost, so when the built-in families suffice, they should be
used instead.  The other novelty is the relax option, which refits each of
the active sets in the path unpenalized. The algorithm uses cyclical
coordinate descent in a path-wise fashion, as described in the papers
listed in the URL below.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/mortran
%doc %{rlibdir}/%{packname}/testscripts
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
