%global __brp_check_rpaths %{nil}
%global packname  SOR
%global packver   0.23.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.23.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation using Sequential Offsetted Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-stats 

%description
Estimation for longitudinal data following outcome dependent sampling
using the sequential offsetted regression technique.  Includes support for
binary, count, and continuous data.  The first regression is a logistic
regression, which uses a known ratio (the probability of being sampled
given that the subject/observation was referred divided by the probability
of being sampled given that the subject/observation was no referred) as an
offset to estimate the probability of being referred given outcome and
covariates.  The second regression uses this estimated probability to
calculate the mean population response given covariates.

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
