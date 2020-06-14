%global packname  funGp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Gaussian Process Models for Scalar and Functional Inputs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
Requires:         R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 

%description
Construction and smart selection of Gaussian process models with emphasis
on treatment of functional inputs. This package offers: (i) flexible
modeling of functional-input regression problems through the fairly
general Gaussian process model; (ii) built-in dimension reduction for
functional inputs; (iii) heuristic optimization of the structural
parameters of the model (e.g., active inputs, kernel function, type of
distance). Metamodeling background is provided in Betancourt et al. (2020)
<doi:10.1016/j.ress.2020.106870>. The algorithm for structural parameter
optimization is described in
<https://hal.archives-ouvertes.fr/hal-02532713>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
