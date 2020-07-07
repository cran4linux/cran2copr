%global packname  EMSNM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          EM Algorithm for Sigmoid Normal Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
It provides a method based on EM algorithm to estimate the parameter of a
mixture model, Sigmoid-Normal Model, where the samples come from several
normal distributions (also call them subgroups) whose mean is determined
by co-variable Z and coefficient alpha while the variance are homogeneous.
Meanwhile, the subgroup each item belongs to is determined by co-variables
X and coefficient eta through Sigmoid link function which is the extension
of Logistic Link function. It uses bootstrap to estimate the standard
error of parameters. When sample is indeed separable, removing estimation
with abnormal sigma, the estimation of alpha is quite well. I used this
method to explore the subgroup structure of HIV patients and it can be
used in other domains where exists subgroup structure.

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
