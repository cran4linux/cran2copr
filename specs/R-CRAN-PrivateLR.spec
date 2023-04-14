%global __brp_check_rpaths %{nil}
%global packname  PrivateLR
%global packver   1.2-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.22
Release:          3%{?dist}%{?buildtag}
Summary:          Differentially Private Regularized Logistic Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements two differentially private algorithms for estimating
L2-regularized logistic regression coefficients. A randomized algorithm F
is epsilon-differentially private (C. Dwork, Differential Privacy, ICALP
2006 <DOI:10.1007/11681878_14>), if |log(P(F(D) in S)) - log(P(F(D') in
S))| <= epsilon for any pair D, D' of datasets that differ in exactly one
record, any measurable set S, and the randomness is taken over the choices
F makes.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
