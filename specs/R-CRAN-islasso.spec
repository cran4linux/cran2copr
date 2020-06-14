%global packname  islasso
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          The Induced Smoothed Lasso

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-Matrix 

%description
An implementation of the induced smoothing (IS) idea to lasso
regularization models to allow estimation and inference on the model
coefficients (currently hypothesis testing only). Linear, logistic,
Poisson and gamma regressions with several link functions are implemented.
The algorithm is described in the original paper: Cilluffo, G., Sottile,
G., La Grutta, S. and Muggeo, V. (2019) The Induced Smoothed lasso: A
practical framework for hypothesis testing in high dimensional regression.
<doi:10.1177/0962280219842890>, and discussed in a tutorial: Sottile, G.,
Cilluffo, G., and Muggeo, V. (2019) The R package islasso: estimation and
hypothesis testing in lasso regression. <doi:10.13140/RG.2.2.16360.11521>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
