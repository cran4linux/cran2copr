%global __brp_check_rpaths %{nil}
%global packname  lass0
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Lasso-Zero for (High-Dimensional) Linear Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve >= 5.6.13
BuildRequires:    R-CRAN-doRNG >= 1.7.1
BuildRequires:    R-CRAN-ismev >= 1.42
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-lpSolve >= 5.6.13
Requires:         R-CRAN-doRNG >= 1.7.1
Requires:         R-CRAN-ismev >= 1.42
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-stats 
Requires:         R-graphics 

%description
Model selection for the (possibly high-dimensional) linear regression
model with Lasso-Zero, an L1-based methodology relying on the repeated use
of noise dictionaries, as described by Descloux, P. and Sardy, S. (2018)
<arXiv:1805.05133>.

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
%{rlibdir}/%{packname}/INDEX
