%global packname  SSLR
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Supervised Classification and Regression Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-RSSL 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-stats 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-proxy 
Requires:         R-methods 
Requires:         R-CRAN-generics 
Requires:         R-utils 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-RSSL 

%description
Providing a collection of techniques for semi-supervised classification
and regression. In semi-supervised problem, both labeled and unlabeled
data are used to train a classifier. The package includes a collection of
semi-supervised learning techniques: self-training, co-training,
democratic, decision tree, random forest, 'S3VM' ... etc, with a fairly
intuitive interface that is easy to use.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
