%global packname  nnGarrote
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
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
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-multicool 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mvnfast 

%description
Functions to compute the non-negative garrote estimator as proposed by
Breiman (1995) <https://www.jstor.org/stable/1269730> with the penalized
initial estimators extension as proposed by Yuan and Lin (2007)
<https://www.jstor.org/stable/4623260>.

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
