%global packname  SMLE
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Joint Feature Screening via Sparse MLE

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-glmnet >= 4.0
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mvnfast 
Requires:         R-CRAN-doParallel 

%description
Variable selection techniques are essential tools for model selection and
estimation in high-dimensional statistical models. Sparse Maximal
Likelihood Estimator (SMLE) (Xu and Chen
(2014)<doi:10.1080/01621459.2013.879531>) provides an efficient
implementation for the joint feature screening method on high-dimensional
generalized linear models. It also conducts a post-screening selection
based on a user-specified selection criterion. The algorithm uses
iterative hard thresholding along with parallel computing.

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

%files
%{rlibdir}/%{packname}
