%global packname  quantreg.nonpar
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Nonparametric Series Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-Rearrangement 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-Rearrangement 

%description
Implements the nonparametric quantile regression method developed by
Belloni, Chernozhukov, and Fernandez-Val (2011) to partially linear
quantile models. Provides point estimates of the conditional quantile
function and its derivatives based on series approximations to the
nonparametric part of the model. Provides pointwise and uniform confidence
intervals using analytic and resampling methods.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
