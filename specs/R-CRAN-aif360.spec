%global packname  aif360
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Help Detect and Mitigate Bias in Machine Learning Models

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rstudioapi 

%description
The 'AI Fairness 360' <https://aif360.mybluemix.net/> toolkit is an
open-source library to help detect and mitigate bias in machine learning
models. The AI Fairness 360 R package includes a comprehensive set of
metrics for datasets and models to test for biases, explanations for these
metrics, and algorithms to mitigate bias in datasets and models.

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
