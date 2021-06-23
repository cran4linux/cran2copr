%global __brp_check_rpaths %{nil}
%global packname  erer
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Empirical Research in Economics with R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-systemfit 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-urca 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-systemfit 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-urca 

%description
Functions, datasets, and sample codes related to the book of 'Empirical
Research in Economics: Growing up with R' by Dr. Changyou Sun are
included. Marginal effects for binary or ordered choice models can be
calculated. Static and dynamic Almost Ideal Demand System (AIDS) models
can be estimated. A typical event analysis in finance can be conducted
with several functions included.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
