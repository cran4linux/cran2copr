%global packname  obliqueRF
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Oblique Random Forests from Recursive Linear Model Splits

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-e1071 
Requires:         R-stats 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-e1071 

%description
Random forest with oblique decision trees for binary classification tasks.
Discriminative node models in the tree are based on: ridge regression,
partial least squares regression, logistic regression, linear support
vector machines, or random coefficients.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
