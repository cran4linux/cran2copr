%global packname  nnGarrote
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Non-Negative Garrote Estimation with Penalized InitialEstimators

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multicool 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 

%description
Functions to compute the non-negative garrote estimator as proposed by
Breiman (1995) <https://www.jstor.org/stable/1269730> with the penalized
initial estimators extension as proposed by Yuan and Lin (2007)
<https://www.jstor.org/stable/4623260>.

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
